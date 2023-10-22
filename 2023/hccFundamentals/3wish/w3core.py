# 3Wish Python port
# By Brygg Ullmer (orig version @MIT Media Lab, port @Clemson University)
# Originally disaggregated from tcl_examp3 1995-11-24
# Python port begun 2023-10-20

import pivy.coin as coin
import traceback

global HIERSEP_CHAR 
HIERSEP_CHAR = ':'

################ Add Obj ################ 
# Initially, push passed text Iv Obj onto space

def addObj(parent, obj):
   try:
     parent.addChild(obj)
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

################ Add Named Inline Obj   ################ 
# Push single text Iv Obj inline into parent (instead of inside own sep)
# addNInlineObj name iv

def addNInlineObj(parent, name, obj, prepend=True):
  try:
    sep = getObjSeparator(parent, name)

    if sep is None:
      print("addNInlineObj error: \"%s\" does not have a valid parent frame!" % name)
      return False

    if prepend: sep.insertChild(obj, 0)
    else:       sep.addChild(obj)

    return True
  except:
    print("addNFrame exception:"); traceback.print_exc()
    return False

################ Add Named Obj ################ 
# Push passed text Iv Obj onto space as a named object
# addNObj name iv

def addNObj(root, name, obj, prepend=False): #default is to append
  obj.setName(name)
  parent = getParentFrame(root, name);

  if parent is None:
    print("addNFrame error: %s does not have a valid parent frame!" % name)
    return False

  if prepend: parent.insertChild(newNode, 0)
  else:       parent.addChild(obj)

  return True

################ Add Named Frame ################ 
# Adds a named separator.  Introduces support for hierarchy
# addNFrame name 

def addNFrame(parent, name):
  try:
    sep = coin.SoSeparator()
    sep.ref()
    sep.setName(name)
    parent.addChild(sep)
    sep.unref()

    return True
  except:
    print("addNFrame exception:"); traceback.print_exc()
    return False

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

     if parent.isOfType(coin.SoSeparator.getClassTypeId()):
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
   
   result = setParams(node, params) #needs iteration
   return result

################ Get Named Obj ################ 
# Get Inventor scene graph contents associated with a name

def getNObj(root, name):
  node = getNamedNode(root, name)
  return node

################# Get Parent Frame ################ 
## Used by addNFrame and addNObj to get parent node

def getParentFrame(root, name): 
  global HIERSEP_CHAR 

  try:
    idx=name.rfind(HIERSEP_CHAR)
    if idx == -1: # we have a root frame
      return root

    #Find node handle to parent node  
    parentname = name[:idx]
    parentNode = getNamedNode(root, parentname)

    if parentNode is None:
      print("getObjSeparator error: can't find \"%s\"!" % name)
      return None

    if not node.isOfType(coin.SoGroup.getClassTypeId()): #"parent" is not a Separator
      print("getParentFrame error: parent frame \"%s\" is not a Separator!" % parentname);
      return None

    return parentNode

  except:
    print("getObjSeparator exception:"); traceback.print_exc()
    return False

### end ###

