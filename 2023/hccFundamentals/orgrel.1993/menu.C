#include "menu.h"

void VpuSSList::init(int x, int y)
{ const int listLength = 10;

  ///Create shell and listwidget itself

  shell = XtAppCreateShell("List Menu", NULL,
			   applicationShellWidgetClass,
			   SoXt::getDisplay(), NULL, 0);

  Arg Args[2];

  XtSetArg(Args[0], XmNvisibleItemCount, (XtArgVal) listLength);
  ListWidgetID = XmCreateScrolledList(shell, "ListWidget", Args, 1);

  ///Use Inventor resize mechanism (some size must be defined)

  SbVec2s menuSize(x,y);
  SoXt::setWidgetSize(shell, menuSize); //Can be done through X directly

  XtManageChild(ListWidgetID);
}

void VpuSSList::initStr(StringList *strLst)
{ 
  Arg Args[4];

  Widget w1, w2;

  ///Add scrollbars

  XtSetArg(Args[0], XmNhorizontalScrollBar, (XtArgVal) &w1);
  XtSetArg(Args[1], XmNverticalScrollBar, (XtArgVal) &w2);
  XtGetValues(ListWidgetID, Args, 2);

  XmAddTabGroup(ListWidgetID);
  XmAddTabGroup(w2);
  if (w1) XmAddTabGroup(w1);

  ///Add callbacks

  XtAddCallback(ListWidgetID, XmNbrowseSelectionCallback, 
		(XtCallbackProc) &VpuSSList::browseCallback, NULL);

  XtAddCallback(ListWidgetID, XmNdefaultActionCallback, 
		(XtCallbackProc) &VpuSSList::selectCallback, NULL);

  ///Add initial text, if present
  
  if (strLst != NULL)
    { XmString *Xstr = new XmString[strLst->length()];
      strLst->resetMarker();
      
      for(int i=0; i < strLst->length(); i++)
	Xstr[i] = (XmString) XmStringCreateLtoR( strLst->next(), 
					     XmSTRING_DEFAULT_CHARSET);

      XtSetArg(Args[0], XmNitems, (XtArgVal) Xstr);
      XtSetArg(Args[1], XmNitemCount, (XtArgVal) strLst->length());
      XtSetValues(ListWidgetID, Args, 2);
    }

  ///Realize

  XtRealizeWidget(shell);
}

void VpuSSList::addItem(char *item)
{ char *newstr = new char[strlen(item) + 1], *ptr;
  strcpy(newstr, item);

  while (ptr=strchr(newstr,'\n'))
    *ptr = ' '; //Remove CR's which may be present

  XmString Xstr = (XmString) XmStringCreateLtoR(newstr,
						XmSTRING_DEFAULT_CHARSET);

  XmListAddItem(ListWidgetID, Xstr, 0);
}

void VpuSSList::browseCallback(Widget, caddr_t, caddr_t call_data)
{ char *s;

  XmListCallbackStruct *cb = (XmListCallbackStruct *) call_data;
  XmStringGetLtoR(cb->item, XmSTRING_DEFAULT_CHARSET, &s);

  printf("Browser: \"%s\"\n", s);
}

void VpuSSList::selectCallback(Widget, caddr_t, caddr_t call_data)
{ char *s;

  XmListCallbackStruct *cb = (XmListCallbackStruct *) call_data;
  XmStringGetLtoR(cb->item, XmSTRING_DEFAULT_CHARSET, &s);

  printf("Selected: \"%s\"\n", s);
}

////// Packed scrollbars

void VpuScrollbarStack::init(int num)
{ sliders = new SoXtSlider*[num];

  ///Create shell

  shell = XtAppCreateShell("Slider array", NULL,
			   applicationShellWidgetClass,
			   SoXt::getDisplay(), NULL, 0);

  RCwidget = XmCreateRowColumn(shell, "RowColumnWidget", NULL, 0);

  SbVec2s widgetSize(200, 200);
  SoXt::setWidgetSize(shell, widgetSize);

  ///Add scrollbar

/*
  Arg Args[4];
  Widget scrollbar;

  XtSetArg(Args[0], XmNverticalScrollBar, (XtArgVal) &scrollbar);
  XtGetValues(RCwidget, Args, 1);

  XmAddTabGroup(RCwidget);
  XmAddTabGroup(scrollbar);
*/

  XtManageChild(RCwidget);

  ///Go with Slider creation

  for(int i=0; i<num; i++)
    { sliders[i] = new SoXtSlider;

      char *namestr = new char[30];
      sprintf(namestr, "Widget #%i", i+1);

      sliders[i]->setLabel(namestr);
      sliders[i]->build(RCwidget, namestr); sliders[i]->show();
    }

  XtRealizeWidget(shell);
}

////// Packed scrollbars, this time with binding to various variables

void VpuScrollbarList::init()
{ valArray = new VPUSBstruct[ScrollbarMaxNum];
  numSliders = 0;

  shell = XtAppCreateShell("Slider array", NULL,
			   applicationShellWidgetClass,
			   SoXt::getDisplay(), NULL, 0);

  RCwidget = XmCreateRowColumn(shell, "RowColumnWidget", NULL, 0);

  SbVec2s widgetSize(200, 200);
  SoXt::setWidgetSize(shell, widgetSize);

  XtManageChild(RCwidget);
}

void VpuScrollbarList::addEntry(char *name, float *valuator, float min, 
				float max, float initial, void (*func)())
{ if (numSliders >= ScrollbarMaxNum)
    { fprintf(stderr, "Scrollbars surpass (arbitrary) max; please increase"
	      "internal constant!\nAborting...\n");
      exit(-1);
    }

  valArray[numSliders].slider = new SoXtSlider;
  valArray[numSliders].name = name;
  valArray[numSliders].val = valuator;
  valArray[numSliders].min = min;
  valArray[numSliders].max = max;
  valArray[numSliders].func = func;

  valArray[numSliders].slider->setLabel(name);
  valArray[numSliders].slider->setValue((initial-min)/(max-min));
  valArray[numSliders].slider->build(RCwidget, name); 
  valArray[numSliders].slider->show();

  VPUSBpassStruct *data = new VPUSBpassStruct;
  data->dclass = this;
  data->val = numSliders;
  valArray[numSliders].slider->addFinishCallback(&VpuScrollbarList::callback,
						 data);

  valArray[numSliders].slider->addValueChangedCallback(
			&VpuScrollbarList::ccallback, data);

  numSliders++;
}

void VpuScrollbarList::callback(void *data, float val)
{ VPUSBpassStruct *ldata = (VPUSBpassStruct *)data;
  VpuScrollbarList *p = (VpuScrollbarList *)ldata->dclass;
  int num = ldata->val;

  printf("<%f returned; min %f, max %f, num %i; val %f>\n", val, 
	  p->valArray[num].min, p->valArray[num].max, num,
	 *(p->valArray[num].val));

  *(p->valArray[num].val) = (p->valArray[num].min +
			     (p->valArray[num].max - 
			      p->valArray[num].min) * val);

  if (p->valArray[num].func != NULL) (p->valArray[num].func)();

  printf("%s changed to %f\n", 
	 p->valArray[num].name, *(p->valArray[num].val));

}
  
void VpuScrollbarList::ccallback(void *data, float val)
{ VPUSBpassStruct *ldata = (VPUSBpassStruct *)data;
  VpuScrollbarList *p = (VpuScrollbarList *)ldata->dclass;
  int num = ldata->val;

  *(p->valArray[num].val) = (p->valArray[num].min +
			     (p->valArray[num].max - 
			      p->valArray[num].min) * val);

  if (p->valArray[num].func != NULL) (p->valArray[num].func)();

  printf("."); 
}



