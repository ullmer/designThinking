#include "doc.h"

//// VpdBase ////

VpdBase::VpdBase()
{ filename = NULL; }

VpdBase::VpdBase(char *filename)
{ setFilename(filename); }

void VpdBase::setFilename(char *nfilename)
{ filename = nfilename; }

char* VpdBase::getFilename()
{ return filename; }

//// VpdText ////

void VpdText::show()
{ char *command;

  command = new char[100];
  sprintf(command, "cat %s", filename); //Should be more, but that requires
   //separate window
  system(command);
}

//// ReadList ////

void ReadList(char *filename, FileList *list)
{ FILE *in = fopen(filename, "rt");

  if (in == NULL) 
    { fprintf(stderr, "Bad filename \"%s\" passed to ReadList\n", filename);
      exit(-1);
    }

  while (!feof(in))
    { char *newLine = new char[80];
      fgets(newLine, 80, in);
      newLine[strlen(newLine)-1] = 0;
      if (!feof(in)) list->append(newLine);
    }
}
