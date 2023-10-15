//// 3Wish: flock headers ////
//// Brygg Ullmer, MIT Media Lab VLW 
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// libFlock links -- 03/05/1996 
//// Disaggregated from bulk 3wish aggregation 11/14/1996

#ifndef __3WISH_FLOCK__
#define __3WISH_FLOCK__

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

#include "Flock.hxx"
#include <math.h>

int TclInitFlock(ClientData , Tcl_Interp *interp, int argc, char *argv[]); 
int TclCloseFlock(ClientData , Tcl_Interp *interp, int argc, char *argv[]);
int TclGetFlockPos(ClientData , Tcl_Interp *interp, int argc, char *argv[]); 
int TclGetFlockOrient(ClientData , Tcl_Interp *interp, int argc, 
    char *argv[]); 
int TclGetFlockVecOrient(ClientData , Tcl_Interp *interp, int argc, 
    char *argv[]); 

#endif

