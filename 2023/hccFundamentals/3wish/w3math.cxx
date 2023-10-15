//// Wish3 Tcl Code ////
//// Brygg Ullmer, MIT Media Lab VLW 
//// ullmer@media.mit.edu / http://www.media.mit.edu/~ullmer
//// Disaggregated from tcl_examp3 11/24/95

#include "w3math.h"

extern SoSelection *root;
extern SoXtViewer *myViewer;
extern Tcl_Interp *interp;

//////////////////////////  Tcl Dist 3D //////////////////////////

int TclDist3D(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{  
   if (argc != 3) {
     w3_error("dist3D","Dist3D error: args should be point1 point2\n");
     interp->result = "Dist3D error: args should be point1 point2\n";
   }

   char *cpoint1 = argv[1],
	*cpoint2 = argv[2];

   SbVec3f *point1 = convTcl2Iv_vert(cpoint1);
   SbVec3f *point2 = convTcl2Iv_vert(cpoint2);

   SbVec3f diff = *point2 - *point1;

   sprintf(interp->result, "%f", diff.length());

   return TCL_OK;
}

//////////////////////////  Tcl Diff 3D //////////////////////////

int TclDiff3D(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{  
   if (argc != 3) {
     w3_error("diff3D","Diff3D error: args should be point1 point2\n");
     interp->result = "Dist3D error: args should be point1 point2\n";
   }

   char *cpoint1 = argv[1],
	*cpoint2 = argv[2];

   SbVec3f *point1 = convTcl2Iv_vert(cpoint1);
   SbVec3f *point2 = convTcl2Iv_vert(cpoint2);

   SbVec3f diff = *point2 - *point1;

   sprintf(interp->result, "%f %f %f",
     diff[0], diff[1], diff[2]);

   return TCL_OK;
}


//////////////////////////  Tcl Add 3D //////////////////////////

int TclAdd3D(ClientData , Tcl_Interp *interp,
  int argc, char *argv[]) 
{  
   if (argc != 3) {
     w3_error("add3D", "add3D error: args should be point1 point2\n");
     interp->result = "Dist3D error: args should be point1 point2\n";
   }

   char *cpoint1 = argv[1],
	*cpoint2 = argv[2];

   SbVec3f *point1 = convTcl2Iv_vert(cpoint1);
   SbVec3f *point2 = convTcl2Iv_vert(cpoint2);

   SbVec3f diff = *point2 + *point1;

   sprintf(interp->result, "%f %f %f",
     diff[0], diff[1], diff[2]);

   return TCL_OK;
}

