//// 3Wish Tcl Code ////
//// Brygg Ullmer, MIT Media Lab VLW 
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Begin 10/27/95
//// Disaggregated from tcl_examp3 11/24/95

#include "3wish.h"
#include "w3err.h"
#include <tcl.h>
#include <tk.h>
#include <tclExtend.h>
//#include <itcl.h>

#include <Inventor/Xt/viewers/SoXtViewer.h>
#include <Inventor/Xt/viewers/SoXtFullViewer.h>
#include <Inventor/Xt/viewers/SoXtExaminerViewer.h>
#include <Inventor/Xt/viewers/SoXtWalkViewer.h>
#include <Inventor/Xt/viewers/SoXtFlyViewer.h>
#include <Inventor/Xt/viewers/SoXtPlaneViewer.h>

#include <Inventor/sensors/SoIdleSensor.h>

//Globally accessable variables

Tcl_Interp *interp;
SoSelection *root;
SoXtViewer *myViewer;

static int XErrorProc(ClientData data, XErrorEvent *errEventPtr);
void idleCallback(void *data, SoSensor *);
SoIdleSensor *idle;

// Main code

void
main(int argc, char **argv) {    
   Widget myWindow = SoXt::init(argv[0]);    
   if(myWindow == NULL) exit(1);     
   
   root = new SoSelection; root->ref();
   root->setName("root");
//   root->addSelectionCallback(selectionCB, NULL);
  
   if (argc < 2) {
     w3_error("main", "Bogus arguments -- require ptr to Tcl source file\n");
     exit(-1);
   }

// Add Tcl elements

    interp = Tcl_CreateInterp();

// init Tk
/*
    static char *display = NULL;
    Tk_Window mainWindow;

    mainWindow = Tk_CreateMainWindow(interp, display, "3wish", "3wish");
    if (mainWindow == NULL) {
      w3_error("Tk init", "%s\n", interp->result);
      return;
    }

#ifndef WIN32
    Tk_CreateErrorHandler(Tk_Display(mainWindow),-1,-1,-1,XErrorProc,
      (ClientData)mainWindow);
#endif WIN32

    Tk_GeometryRequest(mainWindow, 200, 200);
    Tk_SetWindowBackground(mainWindow,
       WhitePixelOfScreen(Tk_Screen(mainWindow)));
*/
// call other app Inits

    if (Tcl_Init(interp) == TCL_ERROR) {
	w3_error("main", "tcl init error");
        return;
    }
    
    if (Tk_Init(interp) == TCL_ERROR) {
	w3_error("main", "tk init error");
        return;
    }
    
#ifndef WIN32
    //if (TclX_Init(interp) == TCL_ERROR) {

    if (Tclx_Init(interp) == TCL_ERROR) {
	w3_error("main", "tclX init error");
        return;
    }
    
#endif WIN32

/*
    if (Itcl_Init(interp) == TCL_ERROR) {
	w3_error("main", "itcl init error");
        return;
    }
*/
//Add binding command.  This should eventually be moved elsewhere

   char bindCmd[] = 
     "proc bindNObj {name binding} {\n"
     " upvar #0 IvNodeBindings nodebindings\n"
     " set nodebindings($name) $binding\n"
     "}";

   int code = Tcl_Eval(interp, bindCmd);
   if (code) {w3_error("main1", "Tcl result %i: %s\n", code, interp->result);}

//Add key-bindings
/*
   SoEventCallback *kbCB = new SoEventCallback;
   kbCB->addEventCallback(SoKeyboardEvent::getClassTypeId(),
     keyboardCB, NULL);
   root->addChild(kbCB);
*/
//Run program arguments
   
   char *progfile = argv[1];
   code = Tcl_EvalFile(interp, progfile);

   if (code) {w3_error("main3", "Tcl result %i: %s\n", code, interp->result);}

// Add scene viewer

   if (argc >= 3) { //3rd arg is viewer type

     if (strcmp(argv[2], "walk") == 0) {
       myViewer = new SoXtWalkViewer(myWindow);
     }

     if (strcmp(argv[2], "fly") == 0) {
       myViewer = new SoXtFlyViewer(myWindow);
     }
     
     if (strcmp(argv[2], "plane") == 0) {
       myViewer = new SoXtPlaneViewer(myWindow);
     }
   
     if (strcmp(argv[2], "examine") == 0) {
       myViewer = new SoXtExaminerViewer(myWindow);
     }
   } else {
     myViewer = new SoXtWalkViewer(myWindow);
   }

//Schedule idle sensor for Tk Mainloop
   idle = new SoIdleSensor(idleCallback, NULL);
   idle->schedule();
  
//Do the viewer inits

   myViewer->setSceneGraph(root);

//   myViewer->setAntialiasing(TRUE, 1);
//really hurts performance with the line-drawings!

   myViewer->setTitle("TclSpace");
//SORTED screws up the current antialiased text, but that's
// not prime priority at moment... BAU 5/16/96
   myViewer->setTransparencyType(SoGLRenderAction::SORTED_OBJECT_BLEND);
//   myViewer->setTransparencyType(SoGLRenderAction::BLEND);
   myViewer->show();

   SoXt::show(myWindow);
   SoXt::mainLoop();
}

void idleCallback(void *data, SoSensor *) 
{
  //printf("idle\n");
  while (Tk_DoOneEvent(TK_ALL_EVENTS|TK_DONT_WAIT)) {}; //non-blocking query
  // process all outstanding events, then nap.


printf("arg, need to nap (napms/sginap)!\n");
  //sginap(1);
  idle->schedule();
}

#ifndef WIN32

int XErrorProc(ClientData data, XErrorEvent *errEventPtr)
{
  Tk_Window w = (Tk_Window)data;
  w3_error("xerrorproc","x protocol error:\nerror=%d request=%d minor=%d",
    errEventPtr->error_code, errEventPtr->request_code,
    errEventPtr->minor_code);

  return 0;
}

#endif 

//END

