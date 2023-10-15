//// 3wish Tcl Code ////
//// Brygg Ullmer, MIT Media Lab VLW 
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// libFlock links -- 03/05/1996

#include "w3flock.h"

#include "Flock.hxx"
#include <math.h>

extern SoSelection *root;
extern SoXtViewer *myViewer;
extern Tcl_Interp *interp;

////////////////////// Tcl Init Flock ////////////////////////

Flock *birdFlock;
//char flockPort[] = "/dev/ttyd2";

int TclInitFlock(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
  if (argc != 2) {
    interp->result = "bad # args; use /dev/ttyd? as arg";
    return TCL_ERROR;
  }

  char *flockport = argv[1];

  pfInit();
  pfMultiprocess(PFMP_APPCULLDRAW);
  pfConfig();

  birdFlock = new Flock(flockport);
  return TCL_OK;
}

////////////////////// Tcl Close Flock ////////////////////////

int TclCloseFlock(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{

  delete birdFlock;
//  pfExit();
  return TCL_OK;
}

////////////////////// Tcl Close Flock ////////////////////////

int TclGetFlockPos(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
  if (argc != 2) {
    interp->result = "bad # args";
    return TCL_ERROR;
  }

  char *whichbird = argv[1];
  int birdnum = atoi(whichbird);

  pfVec3 pos;
  birdFlock->GetBirdPos(birdnum, pos);

  sprintf(interp->result, "%f %f %f", pos[0], pos[1], pos[2]);
  return TCL_OK;
}

////////////////////// Tcl Close Flock ////////////////////////

int TclGetFlockOrient(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
  if (argc != 2) {
    interp->result = "bad # args";
    return TCL_ERROR;
  }

  char *whichbird = argv[1];
  int birdnum = atoi(whichbird);

  pfVec3 hpr;
  birdFlock->GetBirdOrient(birdnum, hpr);

  sprintf(interp->result, "%f %f %f", hpr[0], hpr[1], hpr[2]);
  return TCL_OK;
}

////////////////////// Tcl Close Flock ////////////////////////

int TclGetFlockVecOrient(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{

  if (argc != 2) {
    interp->result = "bad # args";
    return TCL_ERROR;
  }

  char *whichbird = argv[1];
  int birdnum = atoi(whichbird);

  pfVec3 hpr;
  birdFlock->GetBirdOrient(birdnum, hpr);

  hpr[0] *= M_PI/180;  // convert to radian space from degree space
  hpr[1] *= M_PI/180;
  hpr[2] *= M_PI/180;

  SbRotation *rot = hprToRot(hpr[0], hpr[1], hpr[2]);

  SbVec3f base(1,0,0), result;

  rot->multVec(base,result);

  sprintf(interp->result, "%f %f %f", result[0], result[1], result[2]);
  return TCL_OK;
}

///END///

