//Documents, including text files, PostScript, etc.

#ifndef __VPDOC__
#define __VPDOC__

#include <stdio.h>
#include <strings.h>
#include "list.h"

MakeList(char, FileList);

void ReadList(char *filename, FileList *list);

class VpdBase
{ public:
    VpdBase();
    VpdBase(char *filename);

    inline void setFilename(char *filename);
    char* getFilename();
    virtual void show() {}
    
  protected:
    char *filename;
};

class VpdText : public VpdBase
{ public:
    VpdText() : VpdBase() {}
    VpdText(char *filename) : VpdBase(filename) {}

    virtual void show();

  protected:
};

#endif 
