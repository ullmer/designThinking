#include "objects.h"


//// VpoPlanar ////

VpoPlanar::VpoPlanar(VpVec loc, VpVec normal)
{ ApplyLoc(loc); setDir(normal); }
 
/*
VpVec VpoPlanarDirectional::direction(VpVec P)
{ if (Above(P)) return VpgPlane::direction(P);
  VpVec Zero; return Zero;
}
*/

VpoLine::VpoLine(VpVec loc, VpVec orientation)
{ ApplyLoc(loc); setDir(orientation); }

//// VpoText ////

VpoText::VpoText(char *string)
{ SetText(string); }

VpoText::VpoText(VpVec &loc, VpVec &vel, char *string)
{ SetText(string); ApplyLoc(loc); ApplyVel(vel); }

void VpoText::SetText(char *str)
{string = str;}

char* VpoText::GetText()
{ return string; }

// WrapText:: Wraps internal char *string to length (really length+1)
// characters, looking out for already-present linefeeds in the process

char* VpoText::WrapText(int length)
{ char *optr = string,
       *ptr = string + length,
       *tmp;
  
  char *n = string;
  while (n = strchr(n, '\n')) {*(n++)=' ';}

  do { //if ((tmp=strchr(optr, '\n')) && tmp <= ptr) //Let's remove \n's for now
       // {optr = ++tmp; ptr = optr + length; }
    //else
    { while (*ptr != ' ' && ptr > optr) ptr--;
      if (ptr == optr)
	{ ptr = optr + length;
	  while (*ptr != ' ' && *ptr != NULL) ptr++; 
	  if (*ptr == NULL) return string;
	  *ptr = '\n';
	  optr = ++ptr;
	  ptr = optr + length;
	}
      else { *ptr = '\n';
	     optr = ++ptr;
	     ptr = optr + length;
	   }
    }
  } while (string + strlen(string) > ptr);
  
  return string;
}


