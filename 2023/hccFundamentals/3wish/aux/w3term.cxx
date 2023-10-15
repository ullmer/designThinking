// 3wish terminal window
// First-pass implementation begun 1/1/1996
// Brygg Ullmer, MIT Media Lab VLW  ullmer@media.mit.edu

#include "3wish.h"
#include "w3term.h"

#include <Inventor/nodes/SoRotationXYZ.h>
#include <Inventor/nodes/SoRotation.h>

extern SoSelection *root;
extern SoXtViewer *myViewer;
extern Tcl_Interp *interp;
extern win3term *console;

/////////////////////////// TclShowStaticTextWin ///////////////////////////

int TclShowStaticTextWin(ClientData , Tcl_Interp *interp,
  int argc, char *argv[])
{
   if (argc != 6) {
     interp->result = "bad # args; {x y z} text {rot} size transp";
     return TCL_ERROR;
   }

   char *Spoint = argv[1];
   char *text =   argv[2];
   char *Srot =   argv[3];
   char *Ssize =  argv[4];
   char *Stransp =argv[5];

   char **mlines;

//Create text lines array

  int count=0;
  char *ptr, *nptr;

  //Count num lines
   ptr=text;
   while (ptr != NULL) {
     count++;
     ptr=strchr(ptr, '\n');
     if (ptr != NULL) {ptr++;}
   }

  //Build array
   int i=0, len;
   mlines = new char*[count];
   ptr=text;
   while (ptr != NULL) {

     nptr=strchr(ptr, '\n');
     if (nptr == NULL) {len = strlen(ptr);}
     else {len = (int)(nptr-ptr);}

     mlines[i] = new char[len+1];
     strncpy(mlines[i], ptr, len);
     mlines[i][len]=0;

     ptr = nptr;
     if (ptr != NULL) {ptr++;}
     i++;
  }

//

  float size = atof(Ssize);
  float transp = atof(Stransp);

  SbVec3f *point = convTcl2Iv_vert(Spoint);
  SbVec3f *Vrot =  convTcl2Iv_vert(Srot);

  SoTranslation *trans = new SoTranslation;
  trans->translation.setValue(*point);

  SoRotation *rot = new SoRotation;
  rot->rotation.setValue(*(hprToRot((*Vrot)[0], (*Vrot)[1], (*Vrot)[2])));

  TextObj *textobj = new TextObj;
  textobj->setTextLines(count, mlines);
  textobj->setTrans(transp);
  textobj->setScale(size);

  SoSeparator *sep = new SoSeparator;
  sep->ref();

  sep->addChild(trans);
  sep->addChild(rot);
  sep->addChild(textobj);

  root->addChild(sep);

  return TCL_OK;
}

//////////////////////////////////////////////////////////////////////////
/////////////////////////////// tclDialogue //////////////////////////////
//////////////////////////////////////////////////////////////////////////

////////////////////////////// tclDialogue ////////////////////////////////

tclDialogue::tclDialogue(Tcl_Interp *zeinterp) {

  interp = zeinterp;

  nextCommand=NULL;
  lastCommand=NULL;

  command=NULL;
  result=NULL;
  errorcode=0;
  commandNum=1;
}

////////////////////////////// ~tclDialogue ////////////////////////////////

tclDialogue::~tclDialogue() {

 if (command != NULL) {delete command;}
 if (result != NULL)  {delete result;}
}

////////////////////////////// evalResult ////////////////////////////////

char* tclDialogue::evalResult() {

  if (command == NULL) {
    fprintf(stderr, "tclDialogue evalResult called with null command\n");
    return NULL;
  }

  if (interp == NULL) {
    fprintf(stderr, "tclDialogue evalResult called with null interp\n");
    return NULL;
  }

  if (result != NULL) {delete result;}
  errorcode = Tcl_Eval(interp, command);
  result = new char[strlen(interp->result)+1];
  strcpy(result, interp->result);

  return result;
}

////////////////////////////// setCommand ////////////////////////////////

char* tclDialogue::setCommand(char *newcommand) {

  if (result != NULL) {delete result; result=NULL;}
  if (command != NULL) {delete command;}

  command = new char[strlen(newcommand)+1];
  strcpy(command, newcommand);

  return command;
}

////////////////////////////// createNextCommand //////////////////////////////

tclDialogue* tclDialogue::createNextCommand() {
  nextCommand = new tclDialogue(interp); 
  nextCommand->setCommandNum(commandNum+1);
  nextCommand->setLastCommand(this);
  return nextCommand;
}

//////////////////////////////////////////////////////////////////////////
///////////////////////////// tclIvDialogue //////////////////////////////
//////////////////////////////////////////////////////////////////////////

////////////////////////////// tclIvDialogue //////////////////////////////

tclIvDialogue::tclIvDialogue(Tcl_Interp *zeinterp, win3term *nparent) : 
  tclDialogue(zeinterp)
{

  commandRep = new win3line;
  resultRep  = new win3line;
  parent = nparent;

  commandRep->setEvalCB(SrunCommand, this);
}

////////////////////////////// SrunCommand //////////////////////////////

void tclIvDialogue::SrunCommand(void *thisptr) {

  tclIvDialogue *t = (tclIvDialogue *)thisptr;
  t->runCommand();
}

////////////////////////////// runCommand //////////////////////////////

void tclIvDialogue::runCommand() 
{
  setCommand(commandRep->getText());

  char *ptr = evalResult();
  w3_error("tclIvDialogue::runCommand", "eval result: %s\n", ptr);

  resultRep->setText(ptr);

  if (parent != NULL) {
    parent->commandExecuted();
  }
}

////////////////////////////// genName //////////////////////////////

char* tclIvDialogue::genName() {

  char *pname;
  char *basename = "command";

  if (parent != NULL) { pname = parent->getName();}
  else {pname = new char[0]; pname[0]=NULL;}

  char *result = new char[strlen(pname) + strlen(basename) + 5];
   //give some breathing room for up to 10k commands... hardwired, yeah.

  sprintf(result, "%s:%s%i", pname, basename, commandNum);

  if (parent == NULL) {delete pname;} //clean up...

  return result;
}

////////////////////////////// createNextCommand //////////////////////////////

tclDialogue* tclIvDialogue::createNextCommand() {
  nextCommand = new tclIvDialogue(interp, parent); 
  nextCommand->setCommandNum(commandNum+1);
  nextCommand->setLastCommand(this);
  return nextCommand;
}

//////////////////////////////////////////////////////////////////////////
/////////////////////////////// win3term /////////////////////////////////
//////////////////////////////////////////////////////////////////////////

/////////////////////////// win3term ///////////////////////////

win3term::win3term(Tcl_Interp *ninterp, char *tname, int xdim, int ydim)
{
  numQueries = 10;
  interp = ninterp;

  name = new char[strlen(tname)+1];
  strcpy(name, tname);

  terminal = new SoSeparator; terminal->ref();
  dialogue = new tclIvDialogue(interp, this);
  setDim(xdim, ydim);

  SoSeparator *command = new SoSeparator; command->ref();
  command->setName(dialogue->genName());
  //printf("running command %s\n", dialogue->genName());

  command->addChild(dialogue->getCommandRep()->getIv());

  SoTranslation *trans = new SoTranslation;
  trans->translation.setValue(0, -1, 0);
  command->addChild(trans);

  command->addChild(dialogue->getResultRep()->getIv());
  terminal->addChild(command);
  command->unref();
}

//////////////////////// commandExecuted ////////////////////////

void win3term::commandExecuted() {

  tclIvDialogue *ptr = dialogue;

  while (ptr != NULL) {
    
    //shift old command
    char tclcommand[200];
    sprintf(tclcommand, 
      "shiftNObj %s:trans {0 0 %f} {0 0 %f} .5 5; getNObj root",
      ptr->genName(), 
      (ptr->getCommandNum() - 1) * 3., ptr->getCommandNum() * 3.);

    int code = Tcl_Eval(interp, tclcommand);
    if (code) {w3_error("win3term", "Tcl result %i: %s\n", code, interp->result);}

    ptr = (tclIvDialogue *) ptr->getLastCommand();
  }

  //Create new command
  dialogue = (tclIvDialogue *)(dialogue->createNextCommand());

  //...and assert into environment
  SoSeparator *command = new SoSeparator; command->ref();
  command->setName(dialogue->genName());
  //printf("running command %s\n", dialogue->genName());

  command->addChild(dialogue->getCommandRep()->getIv());

  SoTranslation *trans = new SoTranslation;
  trans->translation.setValue(0, -1, 0);
  command->addChild(trans);

  command->addChild(dialogue->getResultRep()->getIv());
  terminal->addChild(command);
}

/////////////////////////// nextChar ///////////////////////////

int win3term::nextChar(char newchar) {

  return dialogue->getCommandRep()->nextChar(newchar);
}

/////////////////////////// nextChar ///////////////////////////

void win3term::setDim(int xdim, int ydim)
{

  winWidth = xdim; winHeight=ydim;

  dialogue->getCommandRep()->setWidth(winWidth);
  dialogue->getResultRep()->setWidth(winWidth);

  tclIvDialogue *ptr = dialogue;
  while ((ptr = (tclIvDialogue *)dialogue->getNextCommand()) != NULL) {
    ptr->getCommandRep()->setWidth(winWidth);
    ptr->getResultRep()->setWidth(winWidth);
  }

  ptr = dialogue;
  while ((ptr = (tclIvDialogue *)dialogue->getLastCommand()) != NULL) {
    ptr->getCommandRep()->setWidth(winWidth);
    ptr->getResultRep()->setWidth(winWidth);
  }

}

/////////////////////////////// displayTerm //////////////////////////////

void win3term::displayTerm()
{ terminal->setName(name);

  root->addChild(terminal);
}

//////////////////////////////////////////////////////////////////////////
/////////////////////////////// win3line //////////////////////////////
//////////////////////////////////////////////////////////////////////////

/////////////////////////////// win3line //////////////////////////////

win3line::win3line() {

  width = 80; //default
  ptr = 0;

  text=new char[width+1];
  textiv = new TextObj;

  evalCB = NULL;

  lastline = NULL;
  nextline = NULL;
}

/////////////////////////////// setWidth //////////////////////////////

void win3line::setWidth(int newwidth) {

  char *newbuffer = new char[newwidth+1];
  if (newwidth > width) {
    strcpy(newbuffer, text);
  } else {
    strncpy(newbuffer, text, newwidth);
    newbuffer[newwidth] = NULL;

    if (strlen(newbuffer) > 0) {setText(newbuffer);} 
  }

  delete text;
  text = newbuffer;
}

/////////////////////////////// setText //////////////////////////////

char* win3line::setText(char *newtext) {

 int textlen = strlen(newtext);
 char *result = NULL;

 char *buffer = new char[textlen + 1];
 strcpy(buffer, newtext);


 if (textlen > width) { //wrap to width, returning excess

   buffer[width] = NULL;
   char *ptr = strrchr(buffer, ' ');

   if (ptr == NULL) {

     //wrap hard to width
     strcpy(text, buffer);
     result = new char[textlen - width + 1];
     strcpy(result, &newtext[width]);
   } else {

     int newlen = (int)(ptr - buffer);
     strncpy(text, newtext, newlen);
     text[newlen]=NULL;

     result = new char[textlen - newlen + 1];
     strcpy(result, &newtext[newlen + 1]);
   }

   delete buffer;
 } else { //no need to wrap

   strcpy(text, newtext);
 }

   char **mlines;

//Create text lines array

  int count=0;
  char *cptr, *nptr;

  //Count num lines
   cptr=text;
   while (cptr != NULL) {
     count++;
     cptr=strchr(cptr, '\n');
     if (cptr != NULL) {cptr++;}
   }

  //Build array
   int i=0, len;
   mlines = new char*[count];
   cptr=text;
   while (cptr != NULL) {

     nptr=strchr(cptr, '\n');
     if (nptr == NULL) {len = strlen(cptr);}
     else {len = (int)(nptr-cptr);}

     mlines[i] = new char[len+1];
     strncpy(mlines[i], cptr, len);
     mlines[i][len]=0;

     cptr = nptr;
     if (cptr != NULL) {cptr++;}
     i++;
  }

//
 textiv->setTextLines(count, mlines);
 ptr = strlen(text);

 return result;
}

/////////////////////////////// nextChar //////////////////////////////

int win3line::nextChar(char newchar) {

  if (ptr >= width) {return 0;} //overflow, unsuccessful

  if (newchar == 8) { //backspace

    //printf("<bs>"); fflush(stdout);
    if (ptr == 0) {return 1;} //"successfull"

    //remove char, backup ptr.
    text[--ptr] = NULL; 

    textiv->setTextName(text);
    return 1;
  }

  if (newchar == 10) { //enter:  eval callback
    //printf("<cr>"); fflush(stdout);
    if (evalCB != NULL) {(*evalCB)(thisptr);}
  }

  //printf("w3line:[%i/%c]", newchar, newchar); fflush(stdout);

  if (newchar < 30 || newchar > 128) { //control char, ignore
    return 1;
  }

  //add char to buffer
  text[ptr] = newchar;
  text[++ptr] = NULL;

  textiv->setTextName(text);
  return 1;
}

/////////////////////////// TclCreateConsole ///////////////////////////

//createConsole consoleName

int TclCreateConsole(ClientData , Tcl_Interp *interp,
  int argc, char *argv[])
{
   if (argc != 2) {
     interp->result = "bad # args; createConsole consoleName";
     return TCL_ERROR;
   }

  char *console_name = argv[1];

  win3term *globconsole = console;
  win3term *console;

  console = new win3term(interp, console_name); //create console
  console->displayTerm(); //adds node to root

  globconsole = console; //define last console as root until focus in place
 
  return TCL_OK;
}

//END//

