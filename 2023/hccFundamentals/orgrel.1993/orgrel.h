//Organizational relations
//Brygg Ullmer, Interval Research Corporation
//Coding begun 06/25/1993
//Theoretical foundation documented in AI notes ~03/1993

//Quick test for stabilization
//Domain - basic info from Interval mailing lists

#include "db.h"
#include "doc.h" //For ReadList function
#include "list.h"
#include <strings.h>

const int PeopleRepulseK = 50,
	  GroupRepulseK = 100;

class PersonObjects;
class GroupObjects;
class GroupObject;

class PersonObject //: public VpObject 
  //remove VpObject dependency so class is useful to Goffman group
{ public:
    PersonObject(char *name);

    void addGroup(GroupObject *group);
    void setName(char *nname) {name = nname;}
    char* getName() {return name;}
    GroupObjects* getGroups() {return membership;}

  protected:
    char *name;
    GroupObjects *membership;
};

MakeList(PersonObject, PersonObjects);

class GroupObject //: public VpObject
{ public:
    GroupObject(char *name);

    void addPerson(PersonObject *person);
    void setName(char *nname) {name=nname;}
    char* getName() {return name;}
    PersonObjects *getPeople() {return members;}

  protected:
    char *name;
    PersonObjects *members;
};

MakeList(GroupObject, GroupObjects);

class PeopleDB : public VpDB
{ public:
    PeopleDB();
    ~PeopleDB();

    virtual PersonObject* getPerson(char *name);

};

class ListHandler : public PeopleDB
{ public:
    ListHandler();

    void readData(char *name); //use name as filename and groupname
    virtual PersonObject* getPerson(char *name);

    PersonObjects* getPeople() {return people;}
    GroupObjects* getGroups() {return groups;}

  protected:
    PersonObjects *people;
    GroupObjects  *groups;
};


