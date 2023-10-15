//// 3Wish: w3util headers ////
//// Brygg Ullmer, MIT Media Lab TMG
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Disaggregated from bulk 3wish aggregation 11/14/1996

#ifndef __3WISH_UTIL__
#define __3WISH_UTIL__

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


int TclGetCamPos(ClientData , Tcl_Interp *interp, int argc, char *argv[]); 
int TclInvRotz(ClientData , Tcl_Interp *interp, int argc, char *argv[]); 
int TclSaveImage(ClientData , Tcl_Interp *interp, int argc, char *argv[]); 
int TclgetBBox(ClientData , Tcl_Interp *interp, int argc, char *argv[]); 
int TclgetNObjTransf(ClientData , Tcl_Interp *interp, int argc, char *argv[]);
int TclTweakDrawstyle(ClientData , Tcl_Interp *interp, int argc, 
   char *argv[]); 

SbVec3f *convTcl2Iv_vert(char *list);
SbVec3f *convTcl2Iv_vertlist(Tcl_Interp *interp, char *list, 
  int *numverts=NULL);

#ifndef WIN32
int TclW3Die(ClientData , Tcl_Interp *interp, int argc, char *argv[]); 
#endif WIN32

#endif

