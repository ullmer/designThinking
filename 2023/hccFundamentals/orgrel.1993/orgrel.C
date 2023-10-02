#include "orgrel.h"

//Implementations

//// ListHandler ////

ListHandler::ListHandler()
{ people = new PersonObjects;
  groups = new GroupObjects;
}

void ListHandler::readData(char *name)
{ GroupObject *newGroup = new GroupObject(name);

  FILE *in = fopen(name, "rt");

  while (!feof(in))
    { char *line = new char[50];
      fscanf(in, "%s", line);

      if (*line == NULL) continue;

      PersonObject *person = getPerson(line);
      newGroup->addPerson(person);
      person->addGroup(newGroup);
    } 

  fclose(in);
  groups->append(newGroup);
}

PersonObject* ListHandler::getPerson(char *name)
{ PersonObject *person;

  void *data = retrieve(name,strlen(name));
  if (data != NULL) person = *((PersonObject **) person);
  else
    { person = new PersonObject(name);
      save(name, strlen(name), (void *)(&person), sizeof(PersonObject *));
      people->append(person);
      printf("New person\n");
    }

  printf("PTR %p, size %i\n", person, getSize());
  return person;
}

//// PeopleDB ////

PeopleDB::PeopleDB()
{ setName("people");
  system("rm people.[pd]??"); //Something of a hack, but not too bad for 
     // the present

  if (open() < 0) 
    {fprintf(stderr, "Unable to open database\n"); exit(-1);}
}

PeopleDB::~PeopleDB()
{ system("rm people.[pd]??"); //Same as before
}

PersonObject* PeopleDB::getPerson(char *name)
{ 
  PersonObject *data = (PersonObject *) retrieve(name,strlen(name));

  if (data == NULL)
    { data = new PersonObject(name);
      save(name, strlen(name), data, sizeof(PersonObject *));
    }

  return data;
}

//// PersonObject ////

PersonObject::PersonObject(char *name)
{ setName(name); 
  membership = new GroupObjects;
}

void PersonObject::addGroup(GroupObject *group)
{ membership->append(group); }

//// GroupObject ////

GroupObject::GroupObject(char *name)
{ setName(name);
  members = new PersonObjects;
}

void GroupObject::addPerson(PersonObject *person)
{ members->append(person); }
