//// Wish3 Tcl Code ////
//// Brygg Ullmer, MIT Media Lab VLW 
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Disaggregated from tcl_examp3 11/24/95

#include "3wish.h"

#include <Inventor/nodes/SoRotationXYZ.h>
#include <Inventor/nodes/SoRotation.h>

extern SoSelection *root;
extern SoXtViewer *myViewer;
extern Tcl_Interp *interp;

//////////////////////////  Place Text //////////////////////////

int TclPlaceText(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{ 
   if (argc < 3) {
     interp->result = "bad # args; name text [{x y z} {rot} size transp"
        " {r g b} font]";
     return TCL_ERROR;
   }

   char *name =   argv[1];
   char *text =   argv[2];

   char *Spoint;
   if (argc > 3)
     Spoint  = argv[3];
   else 
     Spoint  = "0 0 0";

   char *Srot;
   if (argc > 4)
     Srot    = argv[4];
   else 
     Srot    = "0 0 0";

   char *Ssize; 
   if (argc > 5)
     Ssize  = argv[5];
   else 
     Ssize  = "3";
   
   char *Stransp; 
   if (argc > 6)
     Stransp =argv[6];
   else 
     Stransp ="0";

   char *Scolor;
   if (argc > 7)
     Scolor = argv[7]; 
   else
     Scolor = ".9 .9 .9";

   char *font;
   if (argc > 8)
     font =  argv[8];
   else
     font =  "Swiss_bold.48";

   float size = atof(Ssize);
   float transp = atof(Stransp);

  SbVec3f *point = convTcl2Iv_vert(Spoint);
  SbVec3f *Vrot =  convTcl2Iv_vert(Srot);
  SbVec3f *Vcolor = convTcl2Iv_vert(Scolor);

  SoMFColor *rgb= new SoMFColor;
  rgb->setValue((*Vcolor)[0], (*Vcolor)[1], (*Vcolor)[2]);

  SoTranslation *trans = new SoTranslation;
  trans->translation.setValue(*point);

  SoRotation *rot = new SoRotation;
  rot->rotation.setValue(*(hprToRot((*Vrot)[0], (*Vrot)[1], (*Vrot)[2])));

  TextObj *textobj = new TextObj;
  textobj->setTextName(text);
  textobj->setTrans(transp);
  textobj->setScale(size);
  textobj->setColor(rgb);
  textobj->setTextFont(font);

  SoSeparator *sep = new SoSeparator;
  sep->ref();

  sep->addChild(trans);
  sep->addChild(rot);
  sep->addChild(textobj);

  sep->setName(name);
  SoSeparator *parent = getParentFrame(name);

  parent->addChild(sep);

  return TCL_OK;
}


//////////////////////////  Place Parallel Text //////////////////////////

int TclPlaceParText(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{ 
   if (argc != 4) {
     interp->result = "bad # args; PlaceParText text 4verts zoffset";
     return TCL_ERROR;
   }

   char *text  = argv[1];
   char *verts = argv[2];
   float zoffset = atof(argv[3]);

   //Convert Tcl vertices to Inventor vertex array

   int numverts;
   SbVec3f *vecarray = convTcl2Iv_vertlist(interp, verts, &numverts);

   if (numverts != 4) {

     w3_error("TclPlaceParText","TclPlaceParText expects four vertices; %i given!\nAborting...\n",
       numverts);
     exit(-1);
   }

   SbVec3f center = (vecarray[0] + vecarray[1] + vecarray[2] + vecarray[3])/4;
   SbVec3f a      = (vecarray[0] + vecarray[1])/2,
	   b      = (vecarray[1] + vecarray[2])/2,
	   c      = a - center,
	   d      = b - center;

   SbVec3f up = center + c.cross(d); 

   SoTransform *transf = new SoTransform;
//   transf->pointAt(center, up);
   transf->pointAt(center, b);

   SoTranslation *trans = new SoTranslation;
   trans->translation.setValue(0, zoffset, 0);

   TextObj *textobj = new TextObj;

   textobj->setScale(2.0);
   SoMFColor *red = new SoMFColor;
   red->setValue(1,0,0);
   textobj->setColor(red);
   textobj->setTrans(0.5);
   textobj->setTextName(text);
   textobj->setRotationX(-1*M_PI_2);
   textobj->setJustification(SoText3::CENTER);

   SoSeparator *sep = new SoSeparator;
   sep->ref();

 //Extra test routine
/*
   for(int i=0; i<4; i++) { //add four points
     SoSeparator *sep2 = new SoSeparator;
     sep2->ref();

     SoTranslation *trans2 = new SoTranslation;
     trans2->translation = vecarray[i];

     sep2->addChild(trans2);

     SoMaterial *material = new SoMaterial;
     material->diffuseColor.setValue(1,0,0);
     sep2->addChild(material);

     SoCube *cube = new SoCube;
     cube->width.setValue(0.3);
     cube->height.setValue(0.3);
     cube->depth.setValue(0.3);
     sep2->addChild(cube);

     root->addChild(sep2);
   }
*/

   sep->addChild(transf);
   sep->addChild(trans);
   sep->addChild(textobj);

   root->addChild(sep);

   return TCL_OK;
}

      
//////////////////////////  Place Parallel Image //////////////////////////

int TclPlaceParImage(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{ 
   float ratio = 200./256.,
     height=2.5, width=height/ratio;

   if (argc != 6) {
     interp->result = "bad # args; text pointlist";
     return TCL_ERROR;
   }

   char *imagefile = argv[1];
   char *verts = argv[2];
   float xoffset = atof(argv[3]);
   float yoffset = atof(argv[4]);
   float zoffset = atof(argv[5]);

   //Convert Tcl vertices to Inventor vertex array

   int numverts;
   SbVec3f *vecarray = convTcl2Iv_vertlist(interp, verts, &numverts);

   if (numverts != 4) {

     w3_error("TclPlaceParImage","TclPlaceParImage expects four vertices; %i given!\nAborting...\n",
       numverts);
     exit(-1);
   }

//Transform
   SbVec3f center = (vecarray[0] + vecarray[1] + vecarray[2] + vecarray[3])/4;
   SbVec3f up      = (vecarray[1] + vecarray[2])/2;

   SoTransform *transf = new SoTransform;
   transf->pointAt(center, up);

//Translate
   SoTranslation *trans = new SoTranslation;
   trans->translation.setValue(xoffset, zoffset, yoffset);

//Surface
   SoCoordinate3 * coords = new SoCoordinate3;

   coords->point.set1Value(0, 0, -height/2, -width/2);
   coords->point.set1Value(1, 0, -height/2, +width/2);
   coords->point.set1Value(2, 0, +height/2, +width/2);
   coords->point.set1Value(3, 0, +height/2, -width/2);

   SoFaceSet *faceset = new SoFaceSet;
   faceset->numVertices.set1Value(0,4);

   SoTexture2 *texture = new SoTexture2;
   texture->filename.setValue(imagefile);

//Aggregate
   SoSeparator *sep = new SoSeparator;
   sep->ref();

   sep->addChild(transf);
   sep->addChild(trans);
   sep->addChild(coords);
   sep->addChild(texture);
   sep->addChild(faceset);

   //printf("Parallel image addition complete\n");

   root->addChild(sep);

   return TCL_OK;
}

//////////////////////////  Place Parallel Iv //////////////////////////

int TclPlaceParIv(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{ 
   if (argc < 6) {
     interp->result = "bad # args; PlaceParIv Iv Surf x y z [name]";
     return TCL_ERROR;
   }

   char *ivSpec= argv[1];
   char *verts = argv[2];
   float xoffset = atof(argv[3]);
   float yoffset = atof(argv[4]);
   float zoffset = atof(argv[5]);


   SoInput input;
   input.setBuffer(argv[1], strlen(ivSpec));

   SoSeparator *newNode = SoDB::readAll(&input);

   //Convert Tcl vertices to Inventor vertex array

   int numverts;
   SbVec3f *vecarray = convTcl2Iv_vertlist(interp, verts, &numverts);

   if (numverts != 4) {

     w3_error("TclPlaceParIv","TclPlaceParIv expects four vertices; %i given!\nAborting...\n",
       numverts);
     exit(-1);
   }

//Transform
   SbVec3f center = (vecarray[0] + vecarray[1] + vecarray[2] + vecarray[3])/4;
   SbVec3f up      = (vecarray[1] + vecarray[2])/2;

   SoTransform *transf = new SoTransform;
   transf->pointAt(center, up);

//Translate
   SoTranslation *trans = new SoTranslation;
   trans->translation.setValue(xoffset, zoffset, yoffset);

//Aggregate
   SoSeparator *sep = new SoSeparator;
   sep->ref();

//rotation
   SoRotationXYZ *rot = new SoRotationXYZ;
   rot->axis.setValue(SoRotationXYZ::Y);
   rot->angle.setValue(-M_PI_2);


   sep->addChild(transf);
   sep->addChild(trans);
   sep->addChild(rot);
   sep->addChild(newNode);

    
   if (argc > 6) {
     sep->setName(argv[6]);  //create a named node
//     printf("Binding name <%s>\n", argv[6]);
   }

   //printf("Parallel Iv addition complete\n");

   root->addChild(sep);

   return TCL_OK;
}

