//// 3wish utility Code ////
//// Brygg Ullmer, MIT Media Lab TMG
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Disaggregated from tcl_examp3 11/24/95
//// Disaggregated from w3core     11/04/96

#include "w3util.h"

extern SoSelection *root;
extern SoXtViewer *myViewer;
extern Tcl_Interp *interp;

//////////////////////////  Tcl Get Cam Position//////////////////////////

int TclGetCamPos(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
   SbVec3f loc = myViewer->getCamera()->position.getValue();

   sprintf(interp->result, "%f %f %f",
     loc[0], loc[1], loc[2]);

   return TCL_OK;
}

////////////////////////// TclW3Die //////////////////////////

//Die call -- so we can call a graceful quit from 3wish on SGI (hopefully!)

#ifndef WIN32

int TclW3Die(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
  myViewer->hide();
  char quit[] = "exit";
  Tcl_Eval(interp, quit);
  exit(0);
  return TCL_OK;
}

#endif WIN32

////////////////////////// TclTweakDrawstyle //////////////////////////

int TclTweakDrawstyle(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{
   if (argc != 2) {
     interp->result = "bad # args; need drawstyle";
     return TCL_ERROR;
   }

   char *drawstyle = argv[1];

//extern SoXtViewer *myViewer;

   if (strcasecmp(drawstyle, "no_texture")==0) {
     myViewer->setDrawStyle(SoXtViewer::INTERACTIVE, 
       SoXtViewer::VIEW_NO_TEXTURE);
     myViewer->setDrawStyle(SoXtViewer::STILL, SoXtViewer::VIEW_NO_TEXTURE);
   } 

   if (strcasecmp(drawstyle, "as_is")==0) {
     myViewer->setDrawStyle(SoXtViewer::INTERACTIVE, 
       SoXtViewer::VIEW_AS_IS);
     myViewer->setDrawStyle(SoXtViewer::STILL, SoXtViewer::VIEW_AS_IS);
   }

  return TCL_OK;
}

////////////////////////// convTcl2Iv_vert /////////////////////////
// Converts list of 3 floats to an SbVec3f

SbVec3f *convTcl2Iv_vert(char *list)
{ 
  float coords[3];

  sscanf(list, "%f %f %f", &coords[0], &coords[1], &coords[2]);

  SbVec3f *newVec = new SbVec3f(coords[0], coords[1], coords[2]);

  return newVec;
}

////////////////////////// convTcl2Iv_vertlist /////////////////////////

SbVec3f *convTcl2Iv_vertlist(Tcl_Interp *interp, char *list, int *numverts=NULL)
{
   // Calculate number of vertices
   char *len_command = new char[strlen(list) + 10];
   sprintf(len_command, "llength {%s}", list);
   int code = Tcl_Eval(interp, len_command);
   int length = atoi(interp->result);

   // Allocate array

   SbVec3f *verts = new SbVec3f[length];

   // Convert each vertex
   char *command = new char[strlen(list) + 15];
   SbVec3f *tmpvert;

   for(int i=0; i<length; i++) 
     { //Extract array element
       sprintf(command, "lindex {%s} %i", list, i);
       code = Tcl_Eval(interp, command);

       //Convert Tcl result
       tmpvert = convTcl2Iv_vert(interp->result);
       verts[i] = *tmpvert;

       //Clean up
       delete tmpvert;
     }

    delete command; delete len_command;

    if (numverts != NULL) {*numverts = length;}
    return verts;
}

///////////////////// TclInvRotz ///////////////////////////
// rot's Tcl vertices about Z axis by r radians

int TclInvRotz(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{ 
   if (argc != 3) {
     interp->result = "bad # args; angle pointlist";
     return TCL_ERROR;
   }

   char *tangle= argv[1];
   char *verts = argv[2];

   //Convert Tcl vertices to Inventor vertex array

   float angle = atof(tangle);

   int numverts;
   SbVec3f *vecarray = convTcl2Iv_vertlist(interp, verts, &numverts);
   SbVec3f *resarray = new SbVec3f[numverts];

   for(int i=0; i<numverts; i++) {

      float x=vecarray[i][0], y=vecarray[i][2], z=vecarray[i][1];

      float dist=sqrt(x*x + y*y);
      float theta2;
     
      theta2 = atan2(x,y) - angle + M_PI_2;

      resarray[i][0] = dist*cos(theta2);
      resarray[i][2] = dist*sin(theta2);
      resarray[i][1] = z;
   }

   char *presult = new char[50];
   char *result = new char[numverts*50];
   *result = 0; //clear result array

   for(i=0; i<numverts; i++) {

     sprintf(presult, "{%3.4f %3.4f %3.4f} ", 
       resarray[i][0], resarray[i][1], resarray[i][2]);
     strcat(result, presult);
   }

   //Tcl_SetResult(interp, result, TCL_VOLATILE); //for some reason, this
     // dumps core!

   Tcl_SetResult(interp, result, TCL_STATIC);
   //delete result; delete presult; //can't delete, because Volatile
   //doesn't work

   return TCL_OK;
}

///////////////////// Tcl SaveImage///////////////////////////
// saveImage imagename xres yres

int TclSaveImage(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{ 
   if (argc != 4) {
     interp->result = "bad # args; saveImage imagename xres yres";
     return TCL_ERROR;
   }

   char *imagename = argv[1];
   char *Sxres = argv[2];
   char *Syres = argv[3];

   short xres = atoi(Sxres);
   short yres = atoi(Syres);

   SbViewportRegion myViewport(xres, yres);

   SoOffscreenRenderer *myRenderer =
     new SoOffscreenRenderer(myViewport);

   SoGLRenderAction *glre = new SoGLRenderAction(myViewport); 
   glre->setTransparencyType(SoGLRenderAction::BLEND);
   glre->setNumPasses(3);
//   myRenderer->setGLRenderAction(myViewer->getGLRenderAction());
   myRenderer->setGLRenderAction(glre);
//   myRenderer->setViewportRegion(myViewport);

   SbVec2s res = myRenderer->getMaximumResolution();
   printf("Max res = %i %i\n", res[0], res[1]);

//   myRenderer->setBackgroundColor(SbColor(0,0,0));

   SoSeparator *sep = new SoSeparator; sep->ref();
   sep->addChild(myViewer->getCamera());
   sep->addChild(myViewer->getSceneGraph());

   if (!myRenderer->render(sep)) {
     delete myRenderer;
     sprintf(interp->result, "saveImage: Failure in render(root)");
     return TCL_ERROR;
   }

   FILE *f = fopen(imagename, "w");

   if (f == NULL) {
     sprintf(interp->result, "saveImage: failure in opening file");
     return TCL_ERROR;
   }

   myRenderer->writeToRGB(f);

   fclose(f);

   sep->unref();

   return TCL_OK;
}

///////////////////// Tcl getBBox ///////////////////////////
// getBBox name command
// commands supported = bounds, size, center, volume

int TclgetBBox(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{ 
   if (argc < 2) {
     interp->result = "bad # args; getBBox name [command == bounds]";
     return TCL_ERROR;
   }

   char *geomname = argv[1];
   char *command =  argv[2];

   if (myViewer == NULL) {
     interp->result = "Error: myViewer is null during call of getBBox";
     return TCL_ERROR;
   }

   SbViewportRegion viewport = myViewer->getViewportRegion();
   SoGetBoundingBoxAction bboxaction(viewport);

   SoNode *node = getNamedNode(geomname);
   if (node == NULL) {
     interp->result = "Error: bogus named node passed in call of getBBox";
     return TCL_ERROR;
   }

   bboxaction.apply(node);

   SbBox3f bbox;
   float a[3], b[3];

   // Process command

   //bounds command
   if (argc == 2 || strcmp(command, "bounds") == 0) {

     bbox = bboxaction.getBoundingBox();
     bbox.getBounds(a[0], a[1], a[2], b[0], b[1], b[2]);
     sprintf(interp->result, "{%f %f %f} {%f %f %f}", 
       a[0], a[1], a[2], b[0], b[1], b[2]);
     return TCL_OK;
   }

   //size command
   if (strcmp(command, "size") == 0) {

     bbox = bboxaction.getBoundingBox();
     bbox.getSize(a[0], a[1], a[2]);
     sprintf(interp->result, "%f %f %f", a[0], a[1], a[2]);
     return TCL_OK;
   }

   //magsize command
   if (strcmp(command, "magsize") == 0) {

     bbox = bboxaction.getBoundingBox();
     bbox.getSize(a[0], a[1], a[2]);

     float magsize = 
       sqrt (a[0]*a[0] + a[1]*a[1] + a[2]*a[2]);

     sprintf(interp->result, "%f", magsize);
     return TCL_OK;
   }

   //volume command
   if (strcmp(command, "volume") == 0) {

     bbox = bboxaction.getBoundingBox();
     a[0] = bbox.getVolume();
     sprintf(interp->result, "%f", a[0]);
     return TCL_OK;
   }
   
   //center command
   if (strcmp(command, "center") == 0) {

     SbVec3f center = bboxaction.getCenter();
     sprintf(interp->result, "%f %f %f", center[0], center[1], center[2]);
     return TCL_OK;
   }

   interp->result = "Error: bad command in call of getBBox";
   return TCL_ERROR;

}

///////////////////// Tcl getNObjTransf ///////////////////////////
// getNObjTransf name ; returns translation
// Could easily adjust like getBBox to return scale, rotation components

int TclgetNObjTransf(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{ 
   if (argc != 2) {
     interp->result = "bad # args; getNObjTransf name"; 
     return TCL_ERROR;
   }

   char *objname = argv[1];

   if (myViewer == NULL) {
     interp->result = "Error: myViewer is null during call of getBBox";
     return TCL_ERROR;
   }

   SbViewportRegion viewport = myViewer->getViewportRegion();
   SoGetMatrixAction matrixaction(viewport);

   SoPath *path = getNamedNodePath(objname);

   path->setName("debugpath");
   if (path == NULL) {
     interp->result = "Error: bogus named node passed in call of getBBox";
     return TCL_ERROR;
   }
   char debugcmd[] =
      "puts \"debug path\"; puts [getNObj debugpath]";

   Tcl_Eval(interp, debugcmd);

   matrixaction.apply(path);

   SbMatrix matrixres = matrixaction.getMatrix();

   SbVec3f trans, scale;
   SbRotation rotation, scaleorient;

   matrixres.getTransform(trans, rotation, scale, scaleorient);

   sprintf(interp->result, "%f %f %f", trans[0], trans[1], trans[2]);
   return TCL_OK;
}

//END//

