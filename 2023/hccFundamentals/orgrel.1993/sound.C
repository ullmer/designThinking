#include "sound.h"

//// VpsBase ////

VpsBase::VpsBase()
{ sfilename = NULL; }

VpsBase::VpsBase(char *filename)
{ setFilename(filename); }

char* VpsBase::getFilename()
{ return sfilename; }

void VpsBase::setFilename(char *nfile)
{ sfilename = nfile; }

void VpsBase::play()
{ char str[100];

  if (sfilename != NULL)
    { sprintf(str,"playaifc %s &", sfilename);
      printf("<%s>\n", str);
      system(str);
    }
}
