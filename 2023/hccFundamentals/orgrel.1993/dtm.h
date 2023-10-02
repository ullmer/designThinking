#ifndef __VP_DTM__
#define __VP_DTM__

#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include "dtm/dtm.h"

typedef struct
  { int MagicNumber;
    char Name[50];
    char Description[500];
    float location[3];
    float velocity[3];
  } VpSimpleObjStruct;

#define VP_SIMPLE_OBJ_STRUCT

#ifdef __DTMCPP__

//INVENTOR:: quick metric for determination of C or C++ (online) environment
//replace with _CPLUSPLUS or whatever it is

//C++ headers for communciations code

class dtmBaseReader
{ public:
    dtmBaseReader(int port=7100, char *host=NULL);
    
    int dataAvailable();

    inline void setPort(int port);
    inline void setHost(char *host);

  protected:
    int port;
    char *host, *portStr;
    int DTM_port;

    void init();
};

class VpDtmSimpleObjReader : public dtmBaseReader
{ public:
    VpDtmSimpleObjReader(int port=7100, char *host=NULL);
    
    VpSimpleObjStruct* readRecord();
};

#else
/*Corresponding C headers */

#endif

#endif
