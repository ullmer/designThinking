# 3Wish Python port
# By Brygg Ullmer (orig version @MIT Media Lab, port @Clemson University)
# Originally disaggregated from tcl_examp3 1995-11-24
# Python port begun 2023-10-20

import pivy.coin as coin
import traceback

################ Add Obj ################ 
# Initially, push passed text Iv Obj onto space

def addObj(parent, ivObj):
   try:
     iolen = len(ivObj)
     input = coin.SoInput()
     sdb   = coin.SoDb()

     input.setBuffer(ivObj, iolen)   #https://www.coin3d.org/Coin/html/classSoInput.html
     newNode = sdb.readAll(input)    #https://www.coin3d.org/Coin/html/classSoDB.html
     parent.addChild(newNode)
   except:
     print("addObj exception:"); traceback.print_exc()
     return False

   return True

################ Get Named  Node ################ 

def getNamedNode(parent, name):

   search = coin.SoSearchAction()
   search.setName(name)
   search.apply(parent)
   path = search.getPath()
  
   if path is None: return None

   return path.getTail()

################ Get Named Node Path ################ 

def getNamedNodePath (parent, name):

   search = coin.SoSearchAction()
   search.setName(name)
   search.apply(parent)
   path = search.getPath()

   if path is None: return None
   return path

################ Get Parent Node ################ 
# Used by addNFrame and addNObj to get parent node

def getObjSeparator(parent, name): 
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
     w3_error("getObjSeparator", "getObjSeparator error: can't find \"%s\"!", name);
     return NULL;
   }

   //Problems with SoArray.  Tweaking following line to..
   //if (!(node->isOfType(SoSeparator::getClassTypeId()))) { 

   if (!(node->isOfType(SoGroup::getClassTypeId()))) { 
      //"parent" is not a Separator

     w3_error("getObjSeparator","addNFrame error: parent frame \"%s\" is not a Separator!\n", 
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
   SoSeparator *parent = getObjSeparator(name);

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

################ Add Named Obj ################ 
# Push passed text Iv Obj onto space as a named object
# addNObj name iv

def addNObj(parent, obj, name, prepend=False): #default is to append
  parent = getObjSeparator(parent, name);

  if parent is None:
    print("addNFrame error: %s does not have a valid parent frame!" % name)
    return False

  if prepend: parent.insertChild(newNode, 0)
  else:       parent.addChild(newNode)

  return True

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
   SoSeparator *parent = getObjSeparator(name);

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

################ Deleted Named Obj ################ 

def delNObj(root, name):
   try:
     search = coin.SoSearchAction()
     search.setName(name)
     search.apply(root)
     path = search.getPath();

     if path is None:
       print("delNObj error: can't find \"%s\"!" % name);
       return False
 
     parent = path.getNodeFromTail(1);
     if parent is None:
       print("delNObj error: issue extracting \"%s\"!" % name);
       return False

     if parent.isOfType(coin.SoSeparator.getClassTypeId)):
        #we've got a valid parent
        parent.removeChild(path.getTail())
        return True
     else: 
        print("delNObj: problem with removing child %s!" % name);
        return False

   except:
     print("addObj exception:"); traceback.print_exc()
     return False

################ Tweak Named Obj ################ 
### Get Inventor scene graph contents associated with a name

def tweakNObj(root, name, params):

   node = getNamedNode(root, name)

   if node is None:
     print("tweakNObj error: can't find \"%s\"!" % name)
     return False
   
   result = setParams(node, params)
   return result

################ Get Named Obj ################ 
# Get Inventor scene graph contents associated with a name

def getNObj(root, name):
  node = getNamedNode(root, name)
  return node

### end ###

