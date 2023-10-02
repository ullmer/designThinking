
// list.c -- implementation of generic list class

#include "list.h"

List::~List() {
    while ( head ) {
	listCell *next = head->next;
	delete head;
	head = next;
    }
    tail = NULL;
}

void List::prepend(void *in_data) {
    len++;
    head = new listCell(in_data, head);
    if ( !tail ) tail = head;
}

void List::append(void *in_data) {
    if ( tail ) {
	tail->next = new listCell(in_data, NULL);
	tail = tail->next;
	len++;
    } else prepend(in_data);
}

void* List::first() {
    if ( !head ) {
	cout.flush();
	cerr << "ERROR: Empty list.\n";
	abort();
    }
    return head->data;
}

void* List::get() {
    void     *out_data = first();
    listCell *next = head->next;
    delete head;
    head = next;
    len--;
    if ( !head ) tail = NULL;
    return out_data;
}

void* List::next() {
    void *data = mark ? mark->data : NULL;
    if ( mark ) mark = mark->next;
    return data;
}

void List::del(void *key) {
    listCell *l = head;
    listCell *trail = NULL;
    while ( l && l->data != key ) { trail = l; l = l->next; }
    if ( !l ) {
	cout.flush();
	cerr << "ERROR: key not in list.\n";
	abort();
    }
    if ( l == head )
	get();
    else {
	if ( l == tail ) tail = trail;
	trail->next = l->next;
	len--;
	delete l;
    }
}

//ostream& List::printElement(ostream& out, void *data) {
//    return out << "LE" << hex(long(data));
//}

//ostream& Stack::printElement(ostream& out, void *data) {
//    return out << "SE" << hex(long(data));
//}

//ostream& Queue::printElement(ostream& out, void *data) {
//    return out << "QE" << hex(long(data));
//}

/*
ostream& List::print(ostream& out) {
    listCell *l = head;
    out << "[";
    if ( l ) {
	printElement(out, l->data);
	while ( l = l->next ) {
	    out << ", ";
	    printElement(out, l->data);
	}
    }
    return out << "]";
}

ostream& Queue::print(ostream& out) {
    listCell *l = queue.head;
    out << "[";
    if ( l ) {
	printElement(out, l->data);
	while ( l = l->next ) {
	    out << ", ";
	    printElement(out, l->data);
	}
    }
    return out << "]";
}

ostream& Stack::print(ostream& out) {
    listCell *l = stack.head;
    out << "[";
    if ( l ) {
	printElement(out, l->data);
	while ( l = l->next ) {
	    out << ", ";
	    printElement(out, l->data);
	}
    }
    return out << "]";
}

*/
