#ifndef __VPMENU__
#define __VPMENU__

#include "vis.h"

#include <stdio.h>
#include <X11/Xlib.h>
#include <X11/X.h>
#include <X11/Intrinsic.h>
#include <X11/Core.h>
#include <X11/Shell.h>
#include <Xm/Xm.h>
#include <Xm/List.h>
#include <Xm/RowColumn.h>

#include <Inventor/SoXtSlider.h>

MakeList(char, StringList);

typedef struct
  { char *String;
    void *data;
  } strAssocStruct;

MakeList(strAssocStruct, strBindList);

class VpuSSList //Virtual physics utility Selectable Scrollable List
{ protected:
    StringList *stringList;
    void callback();
    void init(int x=200, int y=500);
    void initStr(StringList *strLst);

    Widget shell, ListWidgetID;

    static void browseCallback(Widget w, caddr_t closure, caddr_t call_data);
    static void selectCallback(Widget w, caddr_t closure, caddr_t call_data);

  public:
    VpuSSList(StringList *strLst=NULL) {init(); initStr(strLst);}

    void addItem(char *item);   
};

class VpuScrollbarStack
{ protected:
    SoXtSlider **sliders;
    int numSliders;
    Widget shell, RCwidget; //RC == Row/Column widget

    void init(int num);

  public:
    VpuScrollbarStack(int num=1) {init(num);}

};

const int ScrollbarMaxNum = 20;

typedef struct 
  { SoXtSlider *slider;
    char *name;
    float min, max, *val;
    void (*func)();
  } VPUSBstruct;

///The following could be done a bit more cleanly on a second pass

typedef struct 
  { void *dclass;
    int val;
  } VPUSBpassStruct;

class VpuScrollbarList
{ protected:
    VPUSBstruct *valArray;

    int numSliders;
    Widget shell, RCwidget;

    void init();
    static void callback(void *data, float val);
    static void ccallback(void *data, float val); //Change in progress

  public:
    VpuScrollbarList() {init();}
    void addEntry(char *name, float *valuator, float min, float max, 
		  float initial, void (*func)() = NULL);

    void go() {XtRealizeWidget(shell);}
};

#endif
