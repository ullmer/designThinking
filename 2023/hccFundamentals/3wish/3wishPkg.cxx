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

SoSelection *root;
SoXtViewer *myViewer;

void TkUpdate_idleCallback(void *data, SoSensor *);
SoIdleSensor *iv_idle;

// Main code

int Iv3wish_Init(Tcl_Interp *interp) {

  printf("Loading 3wish Inventor package\n");

   Widget myWindow = SoXt::init("3wish");    
   if(myWindow == NULL) exit(1);     

   printf("Succesfully invoked Widget myWindow\n");
   
   root = new SoSelection; root->ref();
   root->setName("root");
//  root->addSelectionCallback(selectionCB, NULL);
  

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
   
// Add scene viewer

   myViewer = new SoXtWalkViewer(myWindow);

/*
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
*/

//Schedule idle sensor for Tk Mainloop
   iv_idle = new SoIdleSensor(TkUpdate_idleCallback, NULL);
   iv_idle->schedule();
  
//Do the viewer inits

   myViewer->setSceneGraph(root);
   myViewer->setTitle("TclSpace");

//SORTED screws up the current antialiased text, but that's
// not prime priority at moment... BAU 5/16/96
//   myViewer->setTransparencyType(SoGLRenderAction::BLEND);

   myViewer->setTransparencyType(SoGLRenderAction::SORTED_OBJECT_BLEND);
   myViewer->show();

   SoXt::show(myWindow);
   //SoXt::mainLoop(); 
     //WILL NOT RETURN!!  Needs to continue handling Tcl updates on its own...

   return TCL_OK;
}


void TkUpdate_idleCallback(void *data, SoSensor *) 
{
  //printf("idle\n");

  while (Tk_DoOneEvent(TK_ALL_EVENTS|TK_DONT_WAIT)) {}; //non-blocking query

  // process all outstanding events, then nap.


#ifdef SGI
  sginap(1);
#else
  //printf("arg, need to nap (napms/sginap)!\n");
#endif
  

  iv_idle->schedule();
}

//END

