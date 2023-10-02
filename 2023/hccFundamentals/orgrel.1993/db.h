#include <stdio.h>
#include <fcntl.h>
#include <ndbm.h>

class VpDB //build from ndbm
{ public:
   VpDB();
   VpDB(char *name);
   ~VpDB();

   int open();
   int close();
   void setName(char *nname) {name=nname;}

   void* retrieve(void *data, int size);
   int   save(void *key, int ksize, void *data, int dsize);
   int getSize() {return record.dsize;}

  protected:
   char *name;
   DBM *DB;
   datum record, key;
};

