// Virtual Physics code, header file
// Code by Brygg Ullmer, begun 05/16/1993
// Intended especially but not exclusively for the Inventor environment
// Standard library class/function prefix is Vp (Virtual Physics)

#ifndef __VIRT_PHYS__
#define __VIRT_PHYS__

#include <stdio.h>
#include <iostream.h>
#include <math.h>
#include "list.h" //Includes list, queue, stack types
#include "geom.h"

#ifdef INVENTOR

//Inventor includes and defines

#include <Inventor/SoSensor.h>
#include <Inventor/nodes/SoSeparator.h>
#include <Inventor/SoXt.h>
#include <Inventor/SoXtRenderArea.h>
#include <Inventor/SbTime.h>

//SoXt shouldn't be included here in the long term, methinks... belongs
// in vis.h

#define VpScheduler SoTimerSensor
#define VpSchedulerBase SoSensor

#else

#define VpScheduler VpSysScheduler

#endif

//// Class VpObjectBase ////
// Contains basic location and velocity parameters, but no forces or object
// properties

class VpObjectBase : public VpgPoint
{ protected:
    VpVec CurrentVelocity;

  public:
    VpObjectBase();
    VpObjectBase(VpVec &newloc, VpVec &newvel);

    virtual void ApplyLoc(VpVec a) { VpgPoint::setLoc(a); }
    virtual void ApplyVel(VpVec &a);

    void setVel(VpVec &a) {ApplyVel(a);}

    VpVec& GetVel();
    VpVec GetLoc() { return VpgPoint::getLoc(); }
};

class VpForces; //Forward declarations
class VpTime;
class VpTime;  //But relative to *what*?  Some other Time... how about 

#ifdef OLDSTUFF

typedef int VpPropertyID;
typedef char VpPropertyDescriptor;

//The above should probably be redefined to something else, but for the moment
// int will do.

class VpProperty
{ protected:
    VpPropertyID ID;
    VpPropertyDescriptor *Descriptor;

  public:
    
    VpPropertyID getID() 
	{return ID;}

    VpPropertyDescriptor* getVal() 
	{return Descriptor;}

};

class VpProperties
{ public:
    float operator [] (VpPropertyID pid);
};

#endif OLDSTUFF

/*
//The following was considered as a parent class to VpObjProp, but was
//temporarily eliminated as an unnecessary stage which did not lend
//a great deal in the way of extensibility.  We may change our mind,
//though...

class VpAssociation
{ protected:
    void **assoc;

  public:
    void  SetComponent(int num, void *data);
    void* GetComponent(int num);
    virtual int GetNum();
    virtual int GetSizeComponent(int num);
};
*/

class VpProperties;
class VpForce;

class VpObject : public VpObjectBase
{ protected:
    VpForces *Forces;

    VpVec Acceleration;
    VpProperties *Properties;
    VpVecList *RelativePos;
    VpTime *Time;
    float power; //Should be more closely affiliated with forces; normally 2
    void init();

  public:
    VpObject();
    VpObject(VpVec &loc, VpVec &vel);
    void DeriveParams();
    void SetTimeSource(VpTime *TimeSource);

    inline void AccumulateAccel(VpVec a);
    VpVec GetAccel();
    void ZeroAccel();

    float* setProperty(VpForce *force, float val, int affectedBy = 0);
       //affectedBy == 0: affects and is affected by.
       //  ==  1: affects, not affected by
       //  == -1: affected by, doesn't affect others.
       //returns pointer to internal value location
    VpProperties* getProperties()
      {return Properties;}

};

MakeList(VpObject, VpObjects);

//// Class VpObjGroup /////
// Inherits from VpObject; permits groups of VpObjects and VpObject
// descendants, including other VpObjGroups

class VpObjGroup : public VpObject
{ protected:
    VpObjects MemberList;

  public:
    VpObjGroup();

    AddMember();
    DeleteMember();
};

class VpObjProp // : public VpAssociation
{ protected:
    VpObject *obj;
    VpForce *force;
    float data; //This perhaps should be generalized

  public:
    VpObjProp(VpObject *nobj, VpForce *nforce, float ndata);

    inline void SetFields(VpObject *nobj, VpForce *nforce, float ndata);
    inline void SetQuant(float ndata);
    inline void SetObj(VpObject *nobj);
    inline void SetForce(VpForce *force);

    float GetQuant()
      {return data;}
    VpObject* GetObj()
      {return obj;}
    VpForce* GetForce()
      {return force;}

    //The following is not a good long-term measure; for the moment, it
    //  gives me a handle which allows rapid attachment of mass properties
    //  to widget-based control

    float* getValPtr() 
      {return &data;}
};

MakeList(VpObjProp, VpObjProps);

class VpProperties
{ protected:
    VpObjProps *ops;
  public:
    VpProperties();
    float* SetProperty(VpForce *force, VpObject *obj, float Value, 
		     int affected=1);
    float getProp(VpForce *force);
};

class VpTime //Collapsed class.  Pretty ugly... structure expression more
{public:
  VpTime(float StartTime=0, int start=0);
  ~VpTime();
  
  //Frequency:  Number of times per second process is invoked 
  //Marked in user time (not simulation time)
  virtual void SetFrequency(float BeatsPerSec);
  virtual void StartTime(float StartTime);
  virtual void StartTime();
  virtual void StopTime();
  virtual void ResumeTime()
    {StartTime();} //We leave as a separate function in case later mods needed
  
  void SetTime(float NewTime);
  float GetTime()
    {return CurTime;}
  float GetDeltaT() //Get Time since last callback, *Simulation Time*
    {return SimCallBackInterval;}
  
  void SetScale(float NewScale, VpTime *NewDependency=NULL); 
     //TimeScale, that is number of simulation seconds per user second
  float GetScale();

  virtual void AssertCallback(void (*NewCallback)(void *data, 
		  VpSchedulerBase *sensor), void *CallingFunc=NULL);
  
  void incTime();
  void execUserFunc(VpSchedulerBase *sensor);

 protected:

  void (*UserCallBack)(void *data, SoSensor *);
  void *UserCallingFunc;

  VpTime *WithRelationTo; //NULL if carries no dependencies
  VpScheduler *Scheduler;

  float ScalingConstant, CurTime;
  float UserCallBackInterval, SimCallBackInterval;

  static void PassedCallback(void *data, VpSchedulerBase *sensor);

};

class VpTimeDesc //Add descendants later
{  

// We'll have some carry-over dependencies here, but as of evening 5/28 I
// don't have those fully envisioned.
// 
// Morning 5/29 -- Here we'll add stats monitoring world time vs. virtual
// environment time.  VpTime should perhaps reschedule itself to remain
// as constant as possible, while object update callbacks scaled down to
// match.  Better yet, we normally have a given callback and a given step
// of time this is to represent.  If watching the system clock reveals
// we're being delayed, schedule the next callback for the same amount of
// time it took the current callback, scaling the time step with linear
// dependence, and continually try to reduce the less frequent callback
// incrementally to the original desired, maintaining the same delay
// process throughout.  See how it works...

};

class VpForce

// How are forces handled between objects in different time-domains?  By
// maintaining our velocity-independent sence of variable time domains
// (independent from relativisitic velocities), we may have set ourselves
// up for a bit of a problem...  probably handle in similar fashion to
// shared properties, perhaps in first-generation form with objects only
// experiencing forces from other objects in same reference/time frame.

{ protected:
    VpObjProps *AffectedObjs;
    VpObjProps *SourceObjs;
      // Allows object to gravitationally influence other object, for instance,
      // without being influenced itself.  Gives flexibility at minimum cost...

  public:
    VpForce();
    virtual VpVec Apply(VpObject *host, VpObject *applied) = 0;
    virtual void Calc();
    void SubmitSource(VpObjProp *op)
      { SourceObjs->append(op); } 
    void SubmitAffected(VpObjProp *op)
      { AffectedObjs->append(op); }
};

MakeList(VpForce, VpForces);

class VpEnvironment
{ protected:
    VpForces *ForceList;
    VpObjects *ObjectList;
    VpTime SystemTime;

  public:
    VpEnvironment();
     
    virtual void AssertObject(VpObject *Object);
    virtual void RetractPObject(VpObject *Object); //Add later
    virtual void AssertForce(VpForce *Force);
    
    VpTime* getTime() 
      {return &SystemTime;}

    VpObjects* getObjects() 
      {return ObjectList; }

};

//class SimpleEnvironment : public VpEnvironment
//{};

#define SQ(x) ((x)*(x))
//Temporary...

#endif
