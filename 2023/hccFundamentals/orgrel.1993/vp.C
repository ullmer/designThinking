// Virtual Physics code, code file
// Code by Brygg Ullmer, begun 05/16/1993
// Intended especially but not exclusively for the Inventor environment
// Standard library class/function prefix is Vp (Virtual Physics)

#include "vp.h"

//// Class VpObjectBase ////

VpObjectBase::VpObjectBase()
{ VpVec Zero(0,0,0);
  ApplyLoc(Zero); ApplyVel(Zero); } //Add special support for NULL's

VpObjectBase::VpObjectBase(VpVec &newloc, VpVec &newvel)
{ ApplyLoc(newloc); ApplyVel(newvel); }

void VpObjectBase::ApplyVel(VpVec &a)
{ CurrentVelocity = a; 
}

VpVec& VpObjectBase::GetVel()
{ return CurrentVelocity; }

//// VpObject ////

void VpObject::init()
{ power = 2; Forces = new VpForces; Properties = new VpProperties; 
  ZeroAccel(); 
}

VpObject::VpObject()
{ init(); }

VpObject::VpObject(VpVec &newloc, VpVec &newvel)
{ init(); ApplyLoc(newloc); ApplyVel(newvel); }

void VpObject::AccumulateAccel(VpVec a)
{ Acceleration += a; }

VpVec VpObject::GetAccel()
{ return Acceleration; }

void VpObject::ZeroAccel()
{ Acceleration.setValue(0,0,0); }
 
void VpObject::DeriveParams()
{ VpVec newpos, newvel;

#ifdef BDEBUG
  float x,z;

  Acceleration.getValue(x,x,z);

  printf("DeltaT: %f, Current: %f, AccZ: %f\n",
	 Time->GetDeltaT(), Time->GetTime(), z);
#endif BDEBUG

  newvel = CurrentVelocity + (Acceleration * Time->GetDeltaT());
  newpos = getLoc() + CurrentVelocity * Time->GetDeltaT() +
    0.5 * (Acceleration * pow(Time->GetDeltaT(),power));

  ApplyVel(newvel); ApplyLoc(newpos);
}

void VpObject::SetTimeSource(VpTime *TimeSource)
{ Time = TimeSource; }

float* VpObject::setProperty(VpForce *force, float val, int affectedBy)
{ return Properties->SetProperty(force, this, val, affectedBy); }

//// VpForce ////

VpForce::VpForce()
{ AffectedObjs = new VpObjProps;
  SourceObjs = new VpObjProps;
}

VpVec VpForce::Apply(VpObject *, VpObject *)
{ VpVec nuttin;
  return nuttin;
}

void VpForce::Calc()
{
  SourceObjs->resetMarker();

  if (SourceObjs->length() < 1 || AffectedObjs->length() < 1) return;

  VpObjProp *ptr = SourceObjs->first(), *scanner;

  while (ptr != NULL)
    { AffectedObjs->resetMarker();
      scanner = AffectedObjs->first();
      
      while (scanner != NULL)
	{ if (scanner != ptr) 
	    { (ptr->GetObj())->AccumulateAccel(Apply(ptr->GetObj(),
						     scanner->GetObj())
					       / ptr->GetQuant());
	      //F=ma -> a = F/m, abstracted
	      
#ifdef BDEBUG
	      printf("Booga <%f>\n", ptr->GetObj()->GetAccel().length());
#endif BDEBUG
	    }
	  scanner = AffectedObjs->next();
	}

      ptr = SourceObjs->next();
    }
}

//// VpTime ////

VpTime::VpTime(float BeginTime, int start)
{ 
  Scheduler = NULL;
  UserCallBack = NULL;
  UserCallingFunc = NULL;

  SetScale(1.);
  UserCallBackInterval = 1.;
  SimCallBackInterval = 1.;

  if (start) StartTime(BeginTime);
  else SetTime(BeginTime);
}

VpTime::~VpTime()
{ if (Scheduler != NULL)
    Scheduler->unschedule();
}

void VpTime::SetFrequency(float BeatsPerSec)
{ UserCallBackInterval = 1/BeatsPerSec;
  SimCallBackInterval = ScalingConstant * UserCallBackInterval;

  if (Scheduler != NULL)
    StartTime(); //Will automatically stop time, 
      //and will resync on current UserCallBackInterval
}

void VpTime::StopTime()
{ if (Scheduler != NULL)
    { Scheduler->unschedule(); 
      Scheduler = NULL;
    }
}


void VpTime::incTime()
{ CurTime += SimCallBackInterval; }

void VpTime::execUserFunc(VpSchedulerBase *sensor)
{ if (UserCallBack != NULL)
    (*UserCallBack)(UserCallingFunc, sensor);
}

void VpTime::PassedCallback(void *data, VpSchedulerBase *sensor)
{ VpTime *t = (VpTime *)data; 

  t->incTime();
  t->execUserFunc(sensor);
}

void VpTime::StartTime()
{ if (Scheduler != NULL)
    StopTime();
  
  Scheduler = new VpScheduler(&VpTime::PassedCallback, (void *)this);
  Scheduler->schedule(SbTime((double)UserCallBackInterval));

//#define DEPENDENCY
//SbTime dependency follows; darn.
//  SbTime tmp(UserCallBackInterval));

}

void VpTime::StartTime(float NewStartTime)
{ SetTime(NewStartTime);
  StartTime();
}

void VpTime::SetTime(float NewTime)
{ CurTime = NewTime; } //Will need semaphores if we go parallel

void VpTime::SetScale(float NewScale, VpTime *NewDependency)
{ WithRelationTo = NewDependency;
  ScalingConstant = NewScale;
}

float VpTime::GetScale()
{ if (WithRelationTo == NULL) return ScalingConstant;
  return ScalingConstant * WithRelationTo->GetScale();
}

//// VpTime //// Old division...

void VpTime::AssertCallback(void (*NewCallback)(void *data, 
			VpSchedulerBase *sensor), void *CallingFunc)
{ UserCallBack = NewCallback; UserCallingFunc = CallingFunc; }


//// VpEnvironment ////

VpEnvironment::VpEnvironment()
{ ForceList = new VpForces;
  ObjectList = new VpObjects;
}

void VpEnvironment::AssertObject(VpObject *Object)
{ ObjectList->append(Object);
  Object->SetTimeSource(&SystemTime); //This might not always be desired
}

void VpEnvironment::AssertForce(VpForce *Force)
{ ForceList->append(Force);
}

void VpEnvironment::RetractPObject(VpObject *Object)
{ ObjectList->del(Object);

  //The following delete used to be commented out; perhaps there was a good
  //reason for this (perhaps not)

  // delete Object;

  // Ah... not deleted, as it may be added to other visual environments
}

//// VpObjProp ////

VpObjProp::VpObjProp(VpObject *nobj, VpForce *force, float ndata)
{ SetFields(nobj, force, ndata); }

void VpObjProp::SetFields(VpObject *nobj, VpForce *force, float ndata)
{ SetQuant(ndata); SetObj(nobj); SetForce(force); }

void VpObjProp::SetQuant(float ndata)
{ data = ndata; }

void VpObjProp::SetObj(VpObject *nobj)
{ obj = nobj; }

void VpObjProp::SetForce(VpForce *nforce)
{ force = nforce; }

//// VpProperties ////

VpProperties::VpProperties()
{ops = new VpObjProps; 
}

float* VpProperties::SetProperty(VpForce *force, VpObject *obj, float val, 
			       int affected)

{ VpObjProp *op = new VpObjProp(obj, force, val);
  ops->append(op);
  if (affected !=  1) force->SubmitSource(op);
  if (affected != -1) force->SubmitAffected(op);

  return op->getValPtr();
}

float VpProperties::getProp(VpForce *force)
{ ops->resetMarker();

  if (ops->length() > 0)
    { VpObjProp *ptr = ops->first();

      while (ptr!= NULL && (ptr->GetForce() != force)) ptr=ops->next();

      if (ops == NULL) return 0.;
      return ptr->GetQuant();
    }
  return 0.;
}

