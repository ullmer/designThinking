#ifndef __VP_SOUND__
#define __VP_SOUND__

#include <stdio.h>
#include <stdlib.h>

class VpsBase 
  //Vps == Virtual Physics Sound
{ public:
    VpsBase();
    VpsBase(char *filename);

    inline void setFilename(char *filename);
    char* getFilename();
    virtual void play();

  protected:
    char *sfilename;
};

#endif
