#include "orgrel.h"
#include "doc.h"

//Test of organizational relations
//Brygg Ullmer, Interval Research Corporation
//Coding begun 06/25/1993

ListHandler zeList;

main(int argc, char **argv)
{ 
  //Read in the data files

  for(int i=1; i<argc; i++)
    zeList.readData(argv[i]);

  //Spit them back out

  PersonObject *pO;
  PersonObjects *people = zeList.getPeople();

  GroupObject *gO;
  GroupObjects *groups;

  people->resetMarker(); pO = people->first();

  while (pO != NULL)
    { groups = pO->getGroups();
      gO = groups->first();
      groups->resetMarker();

      printf("Person: %s\n", pO->getName());

      while (gO != NULL)
	{ printf("   Group: %s\n", gO->getName()); 
	  gO = groups->next(); 
	}

      printf("\n");
      pO = people->next();
    }

}
