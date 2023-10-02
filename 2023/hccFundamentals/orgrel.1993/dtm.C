//DTM code for Vp works

#define __DTMCPP__

#include "dtm.h"


dtmBaseReader::dtmBaseReader(int port, char *host)
{ setPort(port); setHost(host); 
  init();
}

void dtmBaseReader::init()
{ portStr = new char[(host==NULL?0:strlen(host)) + 10];

  sprintf(portStr, "%s:%i", (host==NULL?"":host), port);

  printf("DTM: \"%s\"\n", portStr);

  DTM_port = DTMmakeInPort(portStr, DTM_DEFAULT);

  if (DTM_port == DTMERROR)
    { fprintf(stderr, "Error creating DTM port\n");
      exit(-1);
    }
}

void dtmBaseReader::setPort(int nport)
{ port = nport; }

void dtmBaseReader::setHost(char *nhost)
{ host = nhost; }

int dtmBaseReader::dataAvailable()
{ return DTMavailRead(DTM_port); }


VpDtmSimpleObjReader::VpDtmSimpleObjReader(int port, char *host) : 
  dtmBaseReader(port, host)
{}

VpSimpleObjStruct* VpDtmSimpleObjReader::readRecord()
{ //VpSimpleObjStruct *objStruct = new VpSimpleObjStruct;

  char *string = new char[50];

  DTMreadMsg(DTM_port, string, 50, NULL, 0, DTM_CHAR);

  return (VpSimpleObjStruct *)string;
}

