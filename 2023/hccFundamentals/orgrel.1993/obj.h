// obj.h

#ifndef _obj_h
#define _obj_h

#include <stream.h>

// Deriving from Object has the advantage that you can use the list macros
// more easily (the list macros require the print() method be defined, and 
// Object gives you a default implementation of print()).  But note that
// you do not have to derive from Object in order to store the thing in
// a list.

class Object {
public:
    Object() { }
//    virtual ostream& print(ostream& o);
};

// By overloading << to print Object*'s, we can automatically print out
// anything derived from Object!

//inline ostream& operator<< (ostream& out, Object *obj) {
//    return obj->print(out);
//}

#endif
