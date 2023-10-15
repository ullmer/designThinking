//// 3Wish Time core Code ////
//// Brygg Ullmer, MIT Media Lab TMG
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Disaggregated from tcl_examp3 11/24/95
//// Disaggregated from w3core.cxx 11/04/96

#include "w3time.h"

extern SoSelection *root;
extern SoXtViewer *myViewer;
extern Tcl_Interp *interp;

////////////////////////// Tcl TiAfter //////////////////////////
// Since "after" won't work when Tcl's mainloop isn't active,
// this uses an Inventor one-shot sensor to trigger the execution
// of some Tcl code.

int TclTiAfter(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 

{

  float time = atof(argv[1]);
  char *command = new char[strlen(argv[2])+2];

  strcpy(command, argv[2]);

  SoAlarmSensor *alarm = new SoAlarmSensor(exectclCallback, command);

  alarm->setTimeFromNow(time);
  alarm->schedule();

  return TCL_OK;
}

////////////////////////// Tcl TiPeriodic //////////////////////////
// Since "after" won't work when Tcl's mainloop isn't active,
// this uses an Inventor one-shot sensor to trigger the execution
// of some Tcl code.

int TclTiPeriodic(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 

{

  float time = atof(argv[1]);
  char *command = new char[strlen(argv[2])+2];

  strcpy(command, argv[2]);

  SoTimerSensor *timer = new SoTimerSensor(exectclCallback, command);

  timer->setInterval(time);
  timer->schedule();

  return TCL_OK;
}

////////////////////////// Tcl TiIdle //////////////////////////
// Invokes bound code repetitively with the idle sensor

typedef struct {
  char *str;
  SoIdleSensor *idlesensor;
 } w3_idleStruct;

int TclTiIdle(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 

{
   if (argc != 2) {
     interp->result = "TiIdle: bad # args";
     return TCL_ERROR;
   }

  char *ncommand = argv[1];

  char *command = new char[strlen(ncommand)+1];

  strcpy(command, ncommand);

  SoIdleSensor *idler = new SoIdleSensor;

  w3_idleStruct *istruct = new w3_idleStruct;
  istruct->str = command;
  istruct->idlesensor = idler;

  idler->setFunction(iexectclCallback);
  idler->setData(istruct);

  idler->schedule();

  return TCL_OK;
}

//////////////////////// iexectclCallback ////////////////////////
//Idle equiv of exectclCallback

void iexectclCallback(void *data, SoSensor *)
{
   w3_idleStruct *istruct = (w3_idleStruct *)data;
   char *command =        istruct->str;
   SoIdleSensor *sensor = istruct->idlesensor;

   int code = Tcl_Eval(interp, command);
   if (code) {w3_error("exectclCallback","Tcl result %i: %s\n", code, interp->result);}

   sensor->schedule();
}

//////////////////////// exectclCallback ////////////////////////
//Assumes data is a tcl character stream, and executes it!

void exectclCallback(void *data, SoSensor *)
{
   char *command = (char *)data;

   int code = Tcl_Eval(interp, command);
   if (code) {w3_error("exectclCallback","Tcl result %i: %s\n", code, interp->result);}

//   delete command; //not for tiPeriodic
}

