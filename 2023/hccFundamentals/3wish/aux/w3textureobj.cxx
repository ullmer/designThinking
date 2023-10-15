//// 3wish Tcl Code ////
//// Brygg Ullmer, MIT Media Lab VLW 
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Texture obj -- 12/7/95

#include "3wish.h"

#include <Inventor/nodes/SoRotationXYZ.h>
#include <Inventor/nodes/SoTexture2Transform.h>

extern SoSelection *root;
extern SoXtViewer *myViewer;
extern Tcl_Interp *interp;

//////////////////////////  Place Text //////////////////////////

int TclPlaceTextureObj(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{ 
   if (argc != 12) {
     interp->result = 
       "bad # args; ivTextFrame name texture text offset size transp rgb";
     return TCL_ERROR;
   }
   //printf("textureobj called");

//Argv

   char *name =    argv[1];
   char *Btexture = argv[2];
   char *text =    argv[3];
   char *Boffset = argv[4];
   char *Bsize   = argv[5];
   char *Btransp = argv[6];
   char *Brgb    = argv[7];
   char *Bdisp   = argv[8];
   char *Bx = argv[9];
   char *By = argv[10];
   char *Btexturerot = argv[11];

// Conversions

   float size =   atof(Bsize);
   float transp = atof(Btransp);

   float width = atof(Bx);
   float height= atof(By);
   float texturerot = atof(Btexturerot);

   SbVec3f *offset = convTcl2Iv_vert(Boffset);
   SbVec3f *disp   = convTcl2Iv_vert(Bdisp);
   SbVec3f *B2rgb  = convTcl2Iv_vert(Brgb);

   SoMFColor *rgb= new SoMFColor;
   rgb->setValue((*B2rgb)[0], (*B2rgb)[1], (*B2rgb)[2]);

   SoTranslation *trans = new SoTranslation;
   trans->translation.setValue(*offset);

   SoTranslation *displace = new SoTranslation;
   displace->translation.setValue(*disp);

   SoTexture2Transform *texturetransf = new SoTexture2Transform;
   texturetransf->rotation.setValue(texturerot);

//TextObj

   TextObj *textobj = new TextObj;

   //printf("text %s\n", text);

   textobj->setTextName(text);
// textobj->setRotationZ(-1*M_PI_2);
   textobj->setColor(rgb);
   textobj->setScale(size);
   textobj->setJustification(SoText3::CENTER);
   textobj->setTrans(transp);

//Surface
   SoCoordinate3 *coords = new SoCoordinate3;

   coords->point.set1Value(0, +width/2, -height/2, 0);
   coords->point.set1Value(1, +width/2, +height/2, 0);
   coords->point.set1Value(2, -width/2, +height/2, 0);
   coords->point.set1Value(3, -width/2, -height/2, 0);

   SoFaceSet *faceset = new SoFaceSet;
   faceset->numVertices.set1Value(0,4);

   SoTexture2 *texture = new SoTexture2;
   texture->filename.setValue(Btexture);

//Aggregate

   SoSeparator *sep = new SoSeparator;
   sep->ref();
   sep->setName(name);

   SoSeparator *subsep = new SoSeparator; subsep->ref();
   subsep->addChild(texturetransf);
   subsep->addChild(texture);
   subsep->addChild(coords);
   subsep->addChild(faceset);

   sep->addChild(displace);
   sep->addChild(subsep);

   sep->addChild(trans);
   sep->addChild(textobj);

   //printf("Adding textureobj to root");

   root->addChild(sep);

   return TCL_OK;
}


