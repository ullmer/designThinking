//// 3wish Tcl Code ////
//// Brygg Ullmer, MIT Media Lab VLW 
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Kit code added 03/23/1996

#include <stdio.h>
#include <stdarg.h>
#include <ctype.h>

#include "w3kit.h"

#include <Inventor/nodes/SoDirectionalLight.h>
#include <Inventor/nodes/SoPointLight.h>
#include <Inventor/nodes/SoSpotLight.h>

extern SoSelection *root;
extern SoXtViewer *myViewer;
extern Tcl_Interp *interp;

//////////////////////////  Add Named Kit //////////////////////////
/// Push passed text Iv Obj onto space as a named object
// addNKit name kittype settings

int TclAddNKit(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
   if (argc < 4) {
     interp->result = "bad # args; addNKit name kittype settings";
     return TCL_ERROR;
   }

   int pre=0; //append, don't prepend

   if (argc > 4 && strcmp(argv[4], "pre")) {pre=1;} //prepend

   char *name     = argv[1];
   char *kittype  = argv[2];
   char *settings = argv[3];
   SoSeparator *parent = getParentFrame(name);

   if (parent==NULL) {
     sprintf(interp->result, 
       "addNFrame error: \"%s\" does not have a valid parent frame!", name);
     return TCL_ERROR;
   }

   tclIvKitObj *kitObj = new tclIvKitObj;
   kitObj->createType(kittype);
   kitObj->set(settings);

   SoBaseKit *kit = kitObj->getKit();
   kit->setName(name);

   if (!pre) {
     parent->addChild(kit);
   } else {
     parent->insertChild(kit, 0);
   }

   ///Create Tcl callback to self
   Tcl_CreateCommand(interp, name, tclIvKitObj::ivkitTclEval, (ClientData)
      kitObj, (Tcl_CmdDeleteProc *)NULL);


   return TCL_OK;
}

////////////////////////// tclIvKitObj:: setType //////////////////////////

void tclIvKitObj::createType(char *type) 
{

  if (strcasecmp(type, "base")==0) {
    kittype = BASE; kit = new SoBaseKit();
  }

  if (strcasecmp(type, "light")==0) {
    kittype = LIGHT; kit = new SoLightKit();
  }

  if (strcasecmp(type, "scene")==0) {
    kittype = SCENE; kit = new SoSceneKit();
  }

  if (strcasecmp(type, "separator")==0) {
    kittype = SEP; kit = new SoSeparatorKit();
  }

  if (strcasecmp(type, "shape")==0) {
    kittype = SHAPE; kit = new SoShapeKit();
  }

  if (strcasecmp(type, "wrapper")==0) {
    kittype = WRAPPER; kit = new SoWrapperKit();
  }

  if (strcasecmp(type, "appearance")==0) {
    kittype = APPEARANCE; kit = new SoAppearanceKit();
  }
}

////////////////////////// tclIvKitObj:: set //////////////////////////

void tclIvKitObj::set(char *args) 
{
  switch (kittype) {
    case BASE: ((SoBaseKit *)kit)->set(args); break;
    case LIGHT: ((SoLightKit *)kit)->set(args); break;
    case SCENE: ((SoSceneKit *)kit)->set(args); break;
    case SEP: ((SoSeparatorKit *)kit)->set(args); break;
    case SHAPE: ((SoShapeKit *)kit)->set(args); break;
    case WRAPPER: ((SoWrapperKit *)kit)->set(args); break;
    case APPEARANCE: ((SoAppearanceKit *)kit)->set(args); break;
    default: ((SoBaseKit *)kit)->set(args); break;
  }
}

////////////////////////// tclIvKitObj:: set //////////////////////////

void tclIvKitObj::setPart(char *partname, char *parttype)
{ SoNode *node;

  if (strcmp(parttype, "DirectionalLight")==0) 
    {node = new SoDirectionalLight;}

  if (strcmp(parttype, "SpotLight")==0) 
    {node = new SoSpotLight;}

  if (strcmp(parttype, "PointLight")==0) 
    {node = new SoPointLight;}
/*
  if (strcmp(parttype, "")==0) 
    {node == new So;}

  if (strcmp(parttype, "")==0) 
    {node == new So;}
*/
}

//////////////////////// tclIvKitObj::ivkitTclEval ////////////////////////

int tclIvKitObj::ivkitTclEval(void *ClientData, Tcl_Interp *interp,
      int argc, char *argv[])
{
  tclIvKitObj *t = (tclIvKitObj *)ClientData;

  return t->tclEval(ClientData, interp, argc, argv);

}

//////////////////////// tclIvKitObj::ivkitTclEval ////////////////////////

int tclIvKitObj::tclEval(void *ClientData, Tcl_Interp *interp,
      int argc, char *argv[])
{
   char *funcname = argv[0];

   if (argc < 3) {
     sprintf(interp->result, "Bad args; %s [set/get] argstr", funcname);
     return TCL_ERROR;
   }

   char *command = argv[1];
   char *argstr  = argv[2];

   if (strcasecmp(command, "set") == 0) { 
     printf("%s is called with set command on %s\n", funcname, argstr); 
     set(argstr); 
   }

   if (strcasecmp(command, "setPart") == 0) {
     char *argstr2  = argv[3];
     printf("%s is called with setPart command on %s\n", funcname, argstr);
     setPart(argstr, argstr2);
   }

   if (strcasecmp(command, "get") == 0) {
     printf("%s is called with getcommand on %s; not yet handled\n", 
       funcname, argstr);
   }

  return TCL_OK;
}

