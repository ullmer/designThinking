//// 3Wish: w3math headers ////
//// Brygg Ullmer, MIT Media Lab TMG
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Disaggregated from bulk 3wish aggregation 11/14/1996

#ifndef __3WISH_MATH__
#define __3WISH_MATH__

#include <stdio.h>
#include <stdarg.h>
#include <math.h>
#include <strings.h>
#include <tcl.h>

#include <Inventor/SbLinear.h>

int TclDist3D(ClientData , Tcl_Interp *interp, int argc, char *argv[]); 
int TclDiff3D(ClientData , Tcl_Interp *interp, int argc, char *argv[]); 
int TclAdd3D(ClientData , Tcl_Interp *interp, int argc, char *argv[]); 

#endif


