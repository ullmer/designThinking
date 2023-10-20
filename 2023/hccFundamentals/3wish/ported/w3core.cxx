//// Wish3 Tcl Code ////
//// Brygg Ullmer, MIT Media Lab VLW 
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Disaggregated from tcl_examp3 11/24/95

#include "w3core.h"

extern SoSelection *root;
extern SoXtViewer *myViewer;

//////////////////////////  Add Obj   //////////////////////////
/// Simply push passed text Iv Obj onto space

int TclAddObj(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
   if (argc != 2) {
     interp->result = "bad # args";
     return TCL_ERROR;
   }

   SoInput input;
   input.setBuffer(argv[1], strlen(argv[1]));

   SoSeparator *newNode = SoDB::readAll(&input);

   root->addChild(newNode);
   return TCL_OK;
}


///////////////////////// Get Named  Node /////////////////////////////
//

SoNode *getNamedNode(char *name)
{
   SoSearchAction search;
   search.setName(name);
   search.apply(root);
   SoPath *path = search.getPath();

   if (path == NULL) {return NULL;}
   return path->getTail();
}

///////////////////////// Get Named Node Path /////////////////////////
//

SoPath *getNamedNodePath (char *name)
{
   SoSearchAction search;
   search.setName(name);
   search.apply(root);
   SoPath *path = search.getPath();

   if (path == NULL) {return NULL;}
   return path;
}

///////////////////////// Get Parent Node /////////////////////////////
// Used by addNFrame and addNObj to get parent node

SoSeparator *getParentFrame(char *name) 
{  
   char *ptr=strrchr(name, HIERSEP_CHAR);
   if (ptr == NULL) { // we have a root frame

     return root;
   }

   //Find node handle to parent node  

   char *parentname;
   int  parentlen = (int)(ptr-name);
   parentname = new char[parentlen+1];
   strncpy(parentname, name, parentlen);
   parentname[parentlen] = NULL;

   SoNode *node = getNamedNode(parentname);

   // Deal with node that was returned

   if (node == NULL) {
     w3_error("getParentFrame", "getParentFrame error: can't find \"%s\"!", name);
     return NULL;
   }

   //Problems with SoArray.  Tweaking following line to..
   //if (!(node->isOfType(SoSeparator::getClassTypeId()))) { 

   if (!(node->isOfType(SoGroup::getClassTypeId()))) { 
      //"parent" is not a Separator

     w3_error("getParentFrame","addNFrame error: parent frame \"%s\" is not a Separator!\n", 
       parentname);
     return NULL;
   }

   return (SoSeparator *)node;
}

//////////////////////////  Add Named Inline Obj   //////////////////////////
/// Push single text Iv Obj inline into parent (instead of inside own sep)
// addNInlineObj name iv

int TclAddNInlineObj(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
   if (argc < 3) {
     interp->result = "bad # args";
     return TCL_ERROR;
   }

   int pre=0; //append, don't prepend

   if (argc > 3 && (strcmp(argv[3], "pre")==0)) {pre=1;} //prepend

   char *name = argv[1];
   SoSeparator *parent = getParentFrame(name);

   if (parent==NULL) {
     sprintf(interp->result, 
       "addNFrame error: \"%s\" does not have a valid parent frame!", name);
     return TCL_ERROR;
   }

   SoInput input;
   input.setBuffer(argv[2], strlen(argv[2]));

   SoSeparator *sepNode = SoDB::readAll(&input);
   SoNode *newNode = sepNode->getChild(0); //get first child

   newNode->setName(name);

   if (!pre) {
     parent->addChild(newNode);
   } else {
     parent->insertChild(newNode, 0);
   }

   return TCL_OK;
}

//////////////////////////  Add Named Obj   //////////////////////////
/// Push passed text Iv Obj onto space as a named object
// addNObj name iv

int TclAddNObj(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
   if (argc < 3) {
     interp->result = "bad # args";
     return TCL_ERROR;
   }

   int pre=0; //append, don't prepend

   if (argc > 3 && strcmp(argv[3], "pre")) {pre=1;} //prepend

   char *name = argv[1];
   SoSeparator *parent = getParentFrame(name);

   if (parent==NULL) {
     sprintf(interp->result, 
       "addNFrame error: \"%s\" does not have a valid parent frame!", name);
     return TCL_ERROR;
   }

   SoInput input;
   input.setBuffer(argv[2], strlen(argv[2]));

   SoSeparator *newNode = SoDB::readAll(&input);
   newNode->setName(name);

   if (!pre) {
     parent->addChild(newNode);
   } else {
     parent->insertChild(newNode, 0);
   }

   return TCL_OK;
}

//////////////////////////  Add Named Frame //////////////////////////
/// Adds a named separator.  Introduces support for hierarchy
// addNFrame name 


int TclAddNFrame(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
   if (argc != 2) {
     interp->result = "bad # args";
     return TCL_ERROR;
   }

   char *name = argv[1], *ptr;
   SoSeparator *parent = getParentFrame(name);

   if (parent==NULL) {
     sprintf(interp->result, 
       "addNFrame error: \"%s\" does not have a valid parent frame!", name);
     return TCL_ERROR;
   }

   SoSeparator *sep = new SoSeparator; sep->ref();
   sep->setName(name);
   parent->addChild(sep);
   sep->unref();

   return TCL_OK;
}

//////////////////////////  Delete Named Obj   //////////////////////////
/// Simply push passed text Iv Obj onto space

int TclDelNObj(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
   if (argc != 2) {
     interp->result = "bad # args";
     return TCL_ERROR;
   }

   char *name = argv[1];

   SoSearchAction search;
   search.setName(name);
   search.apply(root);
   SoPath *path = search.getPath();

   if (path == NULL) {
     sprintf(interp->result, "delNObj error: can't find \"%s\"!", name);
     return TCL_ERROR;
   }
 
   SoNode *parent = path->getNodeFromTail(1);
   if (parent != NULL &&
      parent->isOfType(SoSeparator::getClassTypeId())) {

    //OK, we've got a valid parent
    ((SoSeparator *)parent)->removeChild(path->getTail());
   }
   
   return TCL_OK;
}

//////////////////////////  Tweak Named Obj   //////////////////////////
/// Get Inventor scene graph contents associated with a name

int TclTweakNObj(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
   if (argc != 3) {
     interp->result = "bad # args; tweakNObj name params";
     return TCL_ERROR;
   }

   char *name   = argv[1];
   char *params = argv[2];

   SoNode *node = getNamedNode(name);

   if (node == NULL) {
     sprintf(interp->result, "tweakNObj error: can't find \"%s\"!", name);
     return TCL_ERROR;
   }

   node->set(params);

   return TCL_OK;
}

//////////////////////////  Get Named Obj   //////////////////////////
/// Get Inventor scene graph contents associated with a name

int TclGetNObj(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
   if (argc != 2) {
     interp->result = "bad # args";
     return TCL_ERROR;
   }

   char *name = argv[1];

   SoNode *node = getNamedNode(name);

   if (node == NULL) {
     sprintf(interp->result, "getNObj error: can't find \"%s\"!", name);
     return TCL_ERROR;
   }

   int buffsize = 5000;
   char *buffer = (char *)malloc(buffsize);

   if (node != NULL) {
     SoOutput output;
     output.setBuffer(buffer, buffsize, realloc);

     SoWriteAction wa(&output);
     wa.apply(node);
   }

   char *result = new char[strlen(buffer)+1];
   strcpy(result, buffer);
   free(buffer);

   interp->result = result;

   return TCL_OK;
}

/////// END ////////

