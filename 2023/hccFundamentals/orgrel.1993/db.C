#include "db.h"


//// VpDB ////

VpDB::VpDB()
{ name=NULL; DB=NULL; }

VpDB::VpDB(char *name)
{ DB = NULL; setName(name); open();
}

VpDB::~VpDB()
{ if (DB != NULL) 
    { close(); DB = NULL; }
}

int VpDB::open()
{ if (name == NULL) return -1;

  DB = dbm_open(name, O_RDWR|O_CREAT, 0644);

  printf("Database %s opened\n", name);

  return 1;
}  

int VpDB::close()
{ if (DB == NULL) return -1;

  dbm_close(DB);

  DB = NULL;
  return 1;
}

void* VpDB::retrieve(void *data, int size)
{ if (DB == NULL) return NULL;

  key.dptr = (char *)data; key.dsize = size;
  record = dbm_fetch(DB, key);

  printf("retreived: %s\n", (char *)data);
  
  printf("P: %p\n", record.dptr);
  return (void *)record.dptr;
}

int VpDB::save(void *nkey, int ksize, void *data, int dsize)
{ if (DB == NULL) return -1;

  key.dptr = (char *)nkey; key.dsize = ksize;
  record.dptr = (char *)data; record.dsize = dsize;

  dbm_store(DB, key, record, DBM_INSERT);

  return 1;
}

