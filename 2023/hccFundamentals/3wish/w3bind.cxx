//// Wish3 Tcl Code ////
//// Brygg Ullmer, MIT Media Lab VLW 
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Begun 11/24/95

#include "w3bind.h"

//#include "w3term.h"

extern SoSelection *root;
extern SoXtViewer *myViewer;
extern Tcl_Interp *interp;
extern win3term *console;

//////////////////////////  Selection Callback //////////////////////////
// Look for named nodes.  If node is named, see if Tcl has 
// a binding in IvNodeBindings containing executable code.

void selectionCB(void *userData, SoPath *path)
{
  char tclCall[200];
  int numNodes = path->getLength();

  //printf("Selection callback\n");

  //Iterate through children looking for lowest-level binding
  for(int i=numNodes-1; i>=0; i--) {

    SoNode *node = path->getNode(i);
    const char *name = node->getName().getString();
    if (name==NULL) {continue;}

    //Name must be non-null.  Check to see if Tcl has a binding

    sprintf(tclCall, "upvar #0 IvNodeBindings nodebindings; "
      "return [info exists nodebindings(%s)]", name);

//    printf("Debug: <%s>", tclCall);

    int code = Tcl_Eval(interp, tclCall);
    if (code) {printf("Tcl result %i: %s\n", code, interp->result);}

    //execute binding if present
    if (strcmp(interp->result, "1") == 0) { // we have a match!

      sprintf(tclCall, "upvar #0 IvNodeBindings nodebindings; "
	"set nodebindings(%s)", name);

      code = Tcl_Eval(interp, tclCall);
      if (code) {w3_error("selectionCB", "Tcl result %i: %s\n", code, interp->result);}
      else { //run code which was returned
	char *newcode = new char[strlen(interp->result)+1];
	strcpy(newcode, interp->result);
	code = Tcl_Eval(interp, newcode);

	root->deselectAll(); // so we can click on same obj twice
	if (code) {
	  w3_error("selectionCB", "Tcl result %i on bound code: %s\n", code, interp->result);
	}

	delete newcode;
      }

      return;
    }
  }

  //printf("No Tcl bindings found for Iv selection\n");
}

//////////////////////////  Keyboard Callback //////////////////////////

void keyboardCB(void *userData, SoEventCallback *eventCB)
{ 
  const SoEvent *event = eventCB->getEvent();
  SoKeyboardEvent *kbevent = (SoKeyboardEvent *)event;

  char tclCommand[200];
  char callbackChar = kbevent->getPrintableCharacter();

//use SoRayPickAction to figure out if placed over a shell window


  if (SO_KEY_PRESS_EVENT(event, ANY)) {

    //Special-case keys
    if (SO_KEY_PRESS_EVENT(event, BACKSPACE)) {
       callbackChar = 8;
    }
    if (SO_KEY_PRESS_EVENT(event, ENTER)) {
       callbackChar = 10;
    }

    //printf("[%i]", callbackChar); fflush(stdout);

    if (console != NULL) {console->nextChar(callbackChar);}

    eventCB->setHandled(); //uncomment when "B" taken care of
  }

/* //this needs to be handled differently in presence of console
  if (SO_KEY_PRESS_EVENT(event, B)) {
    
    //printf("Evaluating \"b\" command!\n");
    sprintf(tclCommand, 
      "run_b_command");

    int code = Tcl_Eval(interp, tclCommand);
    if (code) {w3_error("keyboardCB", "Tcl result %i: %s\n", code, interp->result);}
    eventCB->setHandled();
  }
*/
}
    
