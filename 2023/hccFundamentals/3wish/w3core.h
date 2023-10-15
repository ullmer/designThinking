//// 3Wish: w3core headers ////
//// Brygg Ullmer, MIT Media Lab TMG
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Disaggregated from tcl_examp3 11/24/95
//// Disaggregated from bulk 3wish aggregation

#ifndef __3WISH_CORE__
#define __3WISH_CORE__

#include <stdio.h>
#include <stdarg.h>
#include <math.h>
#include <strings.h>
#include <tcl.h>

#include <Inventor/SoInput.h>
#include <Inventor/SoDB.h>

#include <Inventor/Xt/SoXt.h> 
#include <Inventor/Xt/viewers/SoXtExaminerViewer.h> 

#include <Inventor/nodes/SoSeparator.h> 
#include <Inventor/Xt/viewers/SoXtViewer.h>

#include <Inventor/actions/SoWriteAction.h>
#include <Inventor/actions/SoSearchAction.h>
#include <Inventor/actions/SoGLRenderAction.h>
#include <Inventor/actions/SoGetBoundingBoxAction.h>
#include <Inventor/actions/SoGetMatrixAction.h>
#include <Inventor/sensors/SoIdleSensor.h>

#include <Inventor/nodes/SoTexture2.h>  
#include <Inventor/nodes/SoTranslation.h>
#include <Inventor/nodes/SoTransform.h>
#include <Inventor/nodes/SoMaterial.h>
#include <Inventor/nodes/SoCoordinate3.h>
#include <Inventor/nodes/SoFaceSet.h>
#include <Inventor/nodes/SoCamera.h>
#include <Inventor/nodes/SoSelection.h>
#include <Inventor/nodes/SoEventCallback.h>
#include <Inventor/nodes/SoCallback.h> 

#include <Inventor/SoOutput.h>
#include <Inventor/SoOffscreenRenderer.h>
#include <Inventor/SbViewportRegion.h>

#define HIERSEP_CHAR ':'

SoNode *getNamedNode(char *name);
SoPath *getNamedNodePath (char *name);
SoSeparator *getParentFrame(char *name);

int TclAddObj(ClientData , Tcl_Interp *interp, int argc, char *argv[]);
int TclAddNInlineObj(ClientData , Tcl_Interp *interp, int argc, char *argv[]);
int TclAddNObj(ClientData , Tcl_Interp *interp, int argc, char *argv[]);
int TclAddNFrame(ClientData , Tcl_Interp *interp, int argc, char *argv[]);
int TclDelNObj(ClientData , Tcl_Interp *interp, int argc, char *argv[]);
int TclTweakNObj(ClientData , Tcl_Interp *interp, int argc, char *argv[]);
int TclGetNObj(ClientData , Tcl_Interp *interp, int argc, char *argv[]);

void w3_error(char *function_name, char *format, ...);

#endif

