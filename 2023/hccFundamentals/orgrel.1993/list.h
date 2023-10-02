
// list.h -- definition of generic list, stack, and queue classes
  
#ifndef _list_h
#define _list_h
  
/*
 *
 * This file provides a set of generic list and list-like classes (queues and
 * stacks).  The basic class is List, and this is used to define Queue and
 * Stack (using a list is a very flexible way to implement queues and stacks).
 * Besides operations to add and remove elements, you can find the length of
 * the underlying list and/or whether or not it is empty.  To access each item
 * in the list (or stack or queue), call the function resetMarker().  This sets
 * an internal marker to the start of the underlying list.  Then you can call
 * next() (until it returns NULL) to access each item in turn.  next()
 * automatically advances the internal marker after returning what it points
 * to.
 *
 * The real power in this file is that it defines macros which create new
 * classes holding pointers to a given class type.  The only restriction is
 * that the class support the print() method.  The print() method must take
 * one parameter: an ostream&.  It can return whatever type you want (including
 * void).  An easy way to fulfill this requirement is to derive your class 
 * from Object which provides a default print() method (printing out the
 * address of the Object instance).
 *
 * The << operator for ostreams has been defined so that you can print out
 * a pointer to a List by the code `cout << l' where l is a List* variable.
 * This prints out the items in the list between [ and ] with semicolons
 * between each.  To work well, you should define the print() method for
 * each object to print out descriptive info.  Note that List itself is
 * derived from Object, so you can easily create lists of lists.
 *
 * Here are the macros you should use:
 *
 * MakeList(elt-type, class-name);
 * 	This declares a new class (called by the given name) with the methods
 *	   empty()
 * 	   length()
 *	   void prepend(elt-type *p)
 *	   void append(elt-type *p)
 *	   elt-type* first()
 *   	   elt-type* get()
 *	   void del(elt-type *p)
 *	   void resetMarker()
 *   	   elt-type* next()
 *	The data stored in the list are pointers to the given element type.
 *
 * Note that there should be a semicolon after the MakeList command.  MakeList
 * expands to a regular class declaration, and this declaration needs a ;
 * after the closing } (as usual).
 *
 * MakeQueue(elt-type, class-name);
 * 	This declares a new class (called by the given name) with the methods
 *	   empty()
 * 	   length()
 *	   void put(elt-type *p)
 *   	   elt-type* get()
 *	   elt-type* front()
 *	   void resetMarker()
 *   	   elt-type* next()
 *	The data stored in the queue are pointers to the given element type.
 *
 * MakeStack(elt-type, class name);
 *	Similar to MakeQueue with the methods
 *	   empty()
 * 	   length()
 *	   void push(elt-type *p)
 *   	   elt-type* pop()
 *	   elt-type* top()
 *	   void resetMarker()
 *	   elt-type* next()
 *
 * As an example of the above, suppose we wish to have a queue of Lists.
 * Then we would would need to put the following in a header file:
 *	#include "list.h"
 *	MakeQueue(List, LQ);
 *			   ^
 *			   note the semicolon!
 *
 */

#include <stream.h>
#include <libc.h>
#include <generic.h>
//#include "obj.h"

struct listCell {
    void     *data;
    listCell *next;
    listCell(void *in_data, listCell *in_next) {
	data = in_data; next = in_next;
    }
};

class List  {
friend class Stack;
friend class Queue;
    listCell *head, *tail, *mark;
    int      len;
public:
    List() {head = tail = NULL; len = 0;}
  virtual ~List();
    int   empty() {return head == NULL;} // is list empty?
    int   length() { return len; }
    void  resetMarker() { mark = head; }
    void  prepend(void *in_data);	 // add to front of list
    void  append(void *in_data);	 // add to end
    void* first();			 // observe front of list
    void* get();			 // remove first element
    void* next();			 // get next entry and increment
    void  del(void *data);		 // remove specified entry
//    virtual ostream& print(ostream& o);
//    virtual ostream& printElement(ostream &out, void *data);
};

class Queue  {
    List  queue;
public:
    int   empty()	{ return queue.empty(); }
    int   length()	{ return queue.length();}
    void  resetMarker() { queue.resetMarker(); 	}
    void* next()	{ return queue.next();	}
    void  put(void *p)	{ queue.append(p); 	}
    void* get()		{ return queue.get();	}
    void* front()	{ return queue.first();	}
//    virtual ostream& print(ostream& o);
//    virtual ostream& printElement(ostream &out, void *data);
};

class Stack  {
    List  stack;
public:
    int   empty()	{ return stack.empty(); }
    int   length()	{ return stack.length();}
    void  resetMarker() { stack.resetMarker(); 	}
    void* next()	{ return stack.next();	}
    void  push(void *p) { stack.prepend(p);	}
    void* pop()		{ return stack.get();	}
    void* top()		{ return stack.first();	}
//    virtual ostream& print(ostream& o);
//    virtual ostream& printElement(ostream &out, void *data);
};

/* 
#define MakeList(elt_type, name)				\
    class name : public List {					\
    public:							\
	elt_type* first() { return (elt_type*)List::first(); }	\
	elt_type* get()   { return (elt_type*)List::get();   }	\
	elt_type* next()  { return (elt_type*)List::next();  }	\
//	virtual ostream& printElement(ostream &out, void *data){\
//	    ((elt_type*)data)->print(out);			\
//	    return out;						\
//	}							\
    }
*/

#define MakeList(elt_type, name)				\
    class name : public List {					\
    public:							\
	elt_type* first() { return (elt_type*)List::first(); }	\
	elt_type* get()   { return (elt_type*)List::get();   }	\
	elt_type* next()  { return (elt_type*)List::next();  }	\
    }


/*
#define MakeQueue(elt_type, name)				\
    class name : public Queue {					\
    public:							\
	elt_type* next()  { return (elt_type*)Queue::next();  }	\
	elt_type* get()   { return (elt_type*)Queue::get();   }	\
	elt_type* front() { return (elt_type*)Queue::front(); }	\
//	virtual ostream& printElement(ostream &out, void *data){\
//	    ((elt_type*)data)->print(out);			\
//	    return out;						\
//	}							\
    }
*/

#define MakeQueue(elt_type, name)				\
    class name : public Queue {					\
    public:							\
	elt_type* next()  { return (elt_type*)Queue::next();  }	\
	elt_type* get()   { return (elt_type*)Queue::get();   }	\
	elt_type* front() { return (elt_type*)Queue::front(); }	\
    }

/*
#define MakeStack(elt_type, name)				\
    class name : public Stack {					\
    public:							\
	elt_type* next() { return (elt_type*)Stack::next(); }	\
	elt_type* pop()  { return (elt_type*)Stack::pop();  }	\
	elt_type* top()  { return (elt_type*)Stack::top();  }	\
//	virtual ostream& printElement(ostream &out, void *data){\
//	    ((elt_type*)data)->print(out);			\
//	    return out;						\
//	}							\
    }
*/

#define MakeStack(elt_type, name)				\
    class name : public Stack {					\
    public:							\
	elt_type* next() { return (elt_type*)Stack::next(); }	\
	elt_type* pop()  { return (elt_type*)Stack::pop();  }	\
	elt_type* top()  { return (elt_type*)Stack::top();  }	\
}

#endif
