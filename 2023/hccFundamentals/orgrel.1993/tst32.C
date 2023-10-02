//Test of SimpleVisualEnvironment with sparsely populated first-trial sim.
//Brygg Ullmer; 06/04/1993

//Operational 06/15
// Bubbles cubes from background.

#include "vp.h"
#include "vis.h"
#include "visenv.h"
#include "visobj.h"
#include "forces.h"
#include "objects.h"
#include <stdlib.h>

VpveEvent Env;

VpfGravity gravity;
VpfBand band;

VpVec PrimaryDirection;

inline float frand() //Returns a float from 0 to 1
{ return (float) rand() / (float) RAND_MAX; }

static int objNum = 0;

SoRotation *spin;
float spinVal=0, spinInc=0.04;
VpVec vertical(0,1,0);

void spinner(void *, SoSensor *)
{ spinVal += spinInc;
  spin->rotation.setValue(vertical, spinVal);
}

SoSeparator *constructTitle()
{ SoSeparator *master = new SoSeparator;
  master->ref();

  SoFont *font = new SoFont;
  font->name.setValue("Times-Roman");
  font->size.setValue(3);
  master->addChild(font);

  SoMaterial *material = new SoMaterial;
  material->diffuseColor.setValue(1,.75,.25);
  material->shininess.setValue(0.50);
  master->addChild(material);

  SoRotation *rot = new SoRotation;
  VpVec axis(1,0,0);
  rot->rotation.setValue(axis, -.5);
  master->addChild(rot);

  spin = new SoRotation;
  spin->rotation.setValue(vertical, spinVal);
  master->addChild(spin);

  SoText3 *text = new SoText3;
  text->justification.setValue(SoText3::CENTER);
  //text->parts.setValue(SoText3::FRONT); //Front only
  static char *title[] = {"modelled",
			  "Physically-               Environments",
			  "for User Interaction",
			  "with Dynamic Information Spaces"};

  char **title2 = new char*[3];
  for(int i=1; i<4; i++) title2[i-1] = title[i];

  text->string.setValues(1,1,title);
  master->addChild(text);

  SoTranslation *trans = new SoTranslation;
  VpVec Down(0.5, -3.3, 0);
  trans->translation.setValue(Down);
   master->addChild(trans);

  font = new SoFont;
  font->name.setValue("Times-Roman");
  font->size.setValue(60);
  master->addChild(font);

  SoText2 *text2 = new SoText2;
  text2->justification.setValue(SoText2::CENTER);
  text2->string.setValues(0,3,title2);
  master->addChild(text2);

//  master->setGLRenderCaching(TRUE); //First time to try this out

  return master;
}

main()
{
///Environmental parameters
  Env.getTime()->SetScale(1);
  Env.getTime()->SetFrequency(15);
  Env.AssertForce(&gravity);
  Env.AssertForce(&band);

  gravity.setPower(0.75);


///Assert central object;
  VpVec Loc(0,0,-50);

  VpObject *centerObj = new VpObject;
  centerObj->setLoc(Loc);
  centerObj->setProperty(&gravity, 700, 1);

  VpvShaped *shaped = new VpvShaped(centerObj, constructTitle());
  Env.AssertVpvObject(shaped);

///Assert rotation

  SoRotation *rot = new SoRotation;
  VpVec axis(1,1,1);
  rot->rotation.setValue(axis, 0.6);
//  Env.getShell()->addChild(rot);
		
///Assert spinning cubes
  VpVec loc(0,-5,-50), vel(1,1,-1);
  VpObject *obj = new VpObject(loc, vel);
  obj->setProperty(&gravity, 10);
  VpvCoCube *cube = new VpvCoCube(obj, 1,0,0);
  Env.AssertVpvObject(cube);

  loc.setValue(-2, 3, -52); vel.setValue(1,-1,1);
  obj = new VpObject(loc, vel);
  obj->setProperty(&gravity, 10);
  obj->setProperty(&band, 80);
  cube = new VpvCoCube(obj, 0,0,1);
  Env.AssertVpvObject(cube);

  loc.setValue(-3, 4, -52); vel.setValue(1,-1,1);
  VpObject *obj2 = new VpObject(loc, vel);
  obj2->setProperty(&gravity, 10);
  obj2->setProperty(&band, 80);
  cube = new VpvCoCube(obj2, .2, .2, 1);
  Env.AssertVpvObject(cube);

  Env.AssertLink(obj, obj2);
  

///Assert rotation engine
  VpTime timer;
  timer.AssertCallback(spinner);
  timer.SetFrequency(15);
  timer.StartTime();

///Window size

  SbVec2s winsize(1280, 1000);
  SoXt::setWidgetSize(*(Env.getWindow()), winsize);

///Go

  Env.StartVis();
  Env.StartSim();
}

