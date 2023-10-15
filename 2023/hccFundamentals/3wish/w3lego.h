//3wish wrappers around Dave Small's Lego Dacta ControlLab libraries
// CONTROLLAB LIBRARIES NOT FOR EXPORT OUT OF MEDIA LAB; made under
//   special arrangement with LEGO.  Contact Dave Small for details

// Brygg Ullmer, MIT Media Lab Tangible Media Group
// Begun 10/05/1996

// Inherits a tad from start by Matt Sakai, 08/28/1996

#include "3wish.h"

#include <Performer/pf.h>
#include <Performer/pr.h>
#include <Performer/prmath.h>

#include <gl/gl.h>
#include <gl/device.h>

#include "libControlLab/ControlLab.hxx"

extern SoSelection *root;
extern SoXtViewer *myViewer;
extern Tcl_Interp *interp;

////////////////////// Tcl Init LegoDacta ////////////////////////

ControlLab *controlLab;

int TclInitLegoDacta(ClientData, Tcl_Interp *interp,
  int argc, char *argv[]) {
  if (argc != 2) {
    interp->result = "bad # args; use /dev/ttyd? as arg";
    return TCL_ERROR;
    }

  char *labport = argv[1];

  pfInit();
  pfMultiprocess(PFMP_APPCULLDRAW);
  pfConfig();

  controlLab = new ControlLab(labport);
//  controlLab = new ControlLab();
  return TCL_OK;
}


////////////////////// Tcl Close LegoDacta ////////////////////////

int TclCloseLegoDacta(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{

  delete controlLab;
  pfExit();
  return TCL_OK;
}

////////////////////// Tcl Get Analog Data ////////////////////////

int TclGetLegoAnalogData(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
  if (argc != 2) {
    interp->result = "bad # args; call as getLegoAnalogData [port=1..8]";
    return TCL_ERROR;
  }

  int data[8], result;

  char *whichport = argv[1]; //1..8
  int portnum = atoi(whichport);

  controlLab->GetAnalogData(data);
  result = data[portnum-1];

  sprintf(interp->result, "%i", result);
  return TCL_OK;
}

////////////////////// Tcl Get Relative Rot ////////////////////////

int TclGetLegoRelativeRot(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
  if (argc != 2) {
    interp->result = "bad # args; call as getLegoAbsoluteRot [port=1..4]";
    return TCL_ERROR;
  }

  int data[8], result;

  char *whichport = argv[1]; //5..8
  int portnum = atoi(whichport);

  controlLab->GetRelativeRotation(data);
  result = data[portnum-1];

  sprintf(interp->result, "%i", result);
  return TCL_OK;
}

////////////////////// Tcl Get Absolute Rot ////////////////////////

int TclGetLegoAbsoluteRot(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
  if (argc != 2) {
    interp->result = "bad # args; call as getLegoAbsoluteRot [port=1..4]";
    return TCL_ERROR;
  }

  int data[8], result;

  char *whichport = argv[1]; //5..8
  int portnum = atoi(whichport);

  controlLab->GetAbsoluteRotation(data);
  result = data[portnum-1];

  sprintf(interp->result, "%i", result);
  return TCL_OK;
}

////////////////////// Tcl Lego MotorOn ////////////////////////

int TclSetLegoMotorOn(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
  if (argc != 3) {
    interp->result = "bad # args; call as setLegoMotorOn [port=a..h] [direction=1]";
    return TCL_ERROR;
  }


  char *whichport = argv[1]; //a..h
  char *whichdirection = argv[2]; //0 or 1
  
  char port=whichport[0];
  int direction = atoi(whichdirection);

  controlLab->MotorOn(port, direction);

  return TCL_OK;
}

////////////////////// Tcl Lego MotorOff ////////////////////////

int TclSetLegoMotorOff(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
  if (argc != 2) {
    interp->result = "bad # args; call as setLegoMotorOff [port=a..h]";
    return TCL_ERROR;
  }


  char *whichport = argv[1]; //a..h
  
  char port=whichport[0];

  controlLab->MotorOff(port);

  return TCL_OK;
}

///END///


