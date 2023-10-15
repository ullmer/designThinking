//// 3Wish: w3bind headers 
//// Brygg Ullmer, MIT Media Lab TMG
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Disaggregated from tcl_examp3 11/24/95
//// Disaggregated from bulk 3wish aggregation

#ifndef __3WISH_BIND__
#define __3WISH_BIND__

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

#include <Inventor/nodes/SoSelection.h>
#include <Inventor/nodes/SoEventCallback.h>
#include <Inventor/nodes/SoCallback.h> 

#include <Inventor/SbViewportRegion.h>

void selectionCB(void *userData, SoPath *path);
void keyboardCB(void *userData, SoEventCallback *eventCB);

#endif

    
