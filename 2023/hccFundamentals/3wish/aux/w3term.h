// 3wish terminal window
// First-pass implementation begun 1/1/96
// Brygg Ullmer, MIT Media Lab VLW  ullmer@media.mit.edu

#ifndef __W3_WINTERM__
#define __W3_WINTERM__

#include "3wish.h"

////////////////////////// tclDialogue //////////////////////////////

class tclDialogue {

  public:
    tclDialogue(Tcl_Interp *zeinterp=NULL);
    ~tclDialogue();

    void setInterp(Tcl_Interp *ninterp) {interp = ninterp;}
    char* setCommand(char *newcommand);
    
    char* evalResult();

    char* getCommand() {return command;}
    char* getResult()  {return result;}
    int   getErrorcode() {return errorcode;}

    void setLastCommand(tclDialogue *nlastCommand) 
      {lastCommand = nlastCommand;}
    void setNextCommand(tclDialogue *nnextCommand) 
      {nextCommand = nnextCommand;}

    tclDialogue* getNextCommand() {return nextCommand;}
    tclDialogue* getLastCommand() {return lastCommand;}

    void delLastCommand() {
      if (lastCommand != NULL) {delete lastCommand; lastCommand=NULL;}
    }

    void delNextCommand() {
      if (nextCommand != NULL) {delete nextCommand; nextCommand=NULL;}
    }

    virtual tclDialogue* createNextCommand();

    void setCommandNum(int num) {commandNum = num;}
    int  getCommandNum()        {return commandNum;}

  protected:

    tclDialogue *nextCommand, *lastCommand;
    char *command, *result;
    int errorcode;
    Tcl_Interp *interp;

    int commandNum;
};

////////////////////////// win3line //////////////////////////////

class win3line {
  public:
    win3line();

    int nextChar(char newchar); //returns overflow flag
    void setWidth(int width);
    
    char* getText() {return text;}
    char* setText(char *newtext);  //returns overflow 

    TextObj* getIv() {return textiv;}

    int getPtr() {return ptr;}

    void setPtr(int nptr) {
      if (nptr <= strlen(text)) {ptr = nptr;}
      else {ptr = strlen(text);}
    }

    void setNextLine(win3line *line) {nextline = line;}
    void setLastLine(win3line *line) {lastline = line;}

    typedef void simpleCB(void *nthisptr);

    void setEvalCB(simpleCB *newevalCB, void *nthisptr) {
      evalCB = newevalCB; thisptr = nthisptr;
    }

    win3line* getNextLine() {return lastline;}
    win3line* getLastLine() {return nextline;}

  protected:
    int width;
    int ptr;
    char *text;

    TextObj *textiv;

    simpleCB *evalCB;
    void *thisptr;

    win3line *lastline, *nextline;

};

////////////////////////// tclIvDialogue //////////////////////////////

class win3term;

class tclIvDialogue : public tclDialogue {

  public:

    tclIvDialogue(Tcl_Interp *zeinterp=NULL, win3term *nparent=NULL);

    virtual tclDialogue* createNextCommand();

    win3line *getCommandRep() {return commandRep;}
    win3line *getResultRep() {return resultRep;}

    void runCommand();
    static void SrunCommand(void *thisptr);
    char* genName();

  protected:
    win3line *commandRep, *resultRep;
    win3term *parent;

};

////////////////////////// win3term //////////////////////////////

class win3term {

  public:
    win3term(Tcl_Interp *interp=NULL, 
       char *tname="console",
       int xdim=60, int ydim=25);

    ~win3term();

    void setDim(int xdim=60, int ydim=25);

    int nextChar(char newchar);

    tclDialogue* getDialogue() {return dialogue;}

    void displayTerm();
    void commandExecuted();

    char* getName() {return name;}

  protected:
    SoSeparator *terminal;

    tclIvDialogue *dialogue;
    int winWidth, winHeight;

    char *name;

    int numQueries;

    Tcl_Interp *interp;
};

#endif

