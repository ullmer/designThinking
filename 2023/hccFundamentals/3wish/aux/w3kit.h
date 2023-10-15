// 3wish terminal window
// First-pass implementation begun 1/1/96
// Brygg Ullmer, MIT Media Lab VLW  ullmer@media.mit.edu

#ifndef __W3_KIT__
#define __W3_KIT__

#include "3wish.h"

#include <Inventor/nodekits/SoBaseKit.h>
#include <Inventor/nodekits/SoLightKit.h>
#include <Inventor/nodekits/SoNodeKit.h>
#include <Inventor/nodekits/SoSceneKit.h>
#include <Inventor/nodekits/SoSeparatorKit.h>
#include <Inventor/nodekits/SoShapeKit.h>
#include <Inventor/nodekits/SoWrapperKit.h>
#include <Inventor/nodekits/SoAppearanceKit.h>

#include <string.h>

////////////////////////// tclIvKitObj //////////////////////////////

class tclIvKitObj {

  public:
    void createType(char *type);

    void set(char *args);
    void setPart(char *partName, char *partType);

    SoBaseKit *getKit() {return kit;}

    static int ivkitTclEval(void *ClientData, Tcl_Interp *interp,
      int argc, char *argv[]);

    int tclEval(void *ClientData, Tcl_Interp *interp,
	  int argc, char *argv[]);

  protected:

    typedef enum {
      BASE, LIGHT, SCENE, SEP, SHAPE, WRAPPER, APPEARANCE
    } IvKitType;

    IvKitType kittype;

    SoBaseKit *kit;
};

#endif

