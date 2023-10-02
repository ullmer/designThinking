% Family example
% By Brygg Ullmer, Clemson University
% Begun 2022-01-01

% borrows from https://raw.githubusercontent.com/Anniepoo/prolog-examples/master/familytree.pl

%:- module(family, []).

fullLast(Fullname,  Lastname)  :- 
  person(lf, Fullname, L), nth0(0, L, Lastname).

fullFirst(Fullname, Firstname) :- 
  person(lf, Fullname, L), nth0(1, L, Firstname).

fullNickL(Fullname,  Nicknames) :- 
  person(lfn, Fullname, L), nth0(2, L, Nicknames).

fullNick(Fullname,  Nickname) :- fullNickL(Fullname, L), member(Nickname, L).

resident(State, City, Resident)   :- residents(State, City, R), member(Resident, R).
resident(X, R) :- state(X), resident(X, _, R).
resident(X, R) :- city(X),  resident(_, X, R).

state(S) :- residents(S, _, _).
city(C)  :- residents(_, C, _).

male(P)    :- parents(_, P, _).
male(P)    :- boys(B), member(P, B).

female(P)  :- parents(P, _, _).
female(P)  :- girls(G), member(P, G).

friend(P1, P2) :- (friends(P1, F), member(P2, F));
                  (friends(P2, G), member(P1, G)).

%male(X)    :- males(Y),   member(X, Y).
%female(X)  :- females(Y), member(X, Y).

father(F, C)   :- parents(_, F, L), member(C, L).
mother(M, C)   :- parents(M, _, L), member(C, L).
parent(P, C)   :- mother(P,C); father(P,C).

partners(X, Y) :- married(X, Y); parents(X, Y, _).
wife(X, Y)     :- married(X, Y), female(X).
husband(X, Y)  :- married(X, Y), husband(X).

relationFF(X, F1, F2) :-                  %F1 and F2 are firstnames
  fullFirst(FL1, F1), fullFirst(FL2, F2), %FL1 and FL2 are fullnames
  relation(X, FL1, FL2).

relation(father, X, Y)   :- father(X, Y).
relation(mother, X, Y)   :- mother(X, Y).
relation(sister, X, Y)   :- sister(X, Y).
relation(brother, X, Y)  :- brother(X, Y).
relation(daughter, X, Y) :- daughter(X, Y).
relation(siblings, X, Y) :- siblings(X, Y).
relation(cousin, X, Y)   :- cousin(X, Y).
relation(son, X, Y)      :- son(X, Y).
relation(aunt, X, Y)     :- aunt(X, Y).
relation(uncle, X, Y)    :- uncle(X, Y).
relation(niece, X, Y)    :- niece(X, Y).
relation(nephew, X, Y)   :- nephew(X, Y).
relation(nephew, X, Y)   :- nephew(X, Y).
relation(married, X, Y)  :- married(X, Y); married(Y, X).
relation(partners, X, Y) :- partners(X, Y).
relation(parents, X, Y)  :- parents(X, Y, _); parents(Y, X, _). %X and Y are the parents
relation(parent, P, C)   :- parent(P, C).                       %P is the parent of child C
relation(child, C, P)    :- parent(P, C).                       %P is the parent of child C
relation(grandfather, X, Y)  :- grandfather(X, Y).
relation(grandmother, X, Y)  :- grandmother(X, Y).

relation(X,Y) :- ancestor(A,X), ancestor(A,Y).
nickname(P, N) :- nicknames(P, Nnames), member(N, Nnames).

son(Child,Parent)      :- male(Child),   parent(Parent,Child).
daughter(Child,Parent) :- female(Child), parent(Parent,Child).

grandfather(GF,GC) :- male(GF),   parent(GF,Somebody),parent(Somebody,GC).
grandmother(GM,GC) :- female(GM), parent(GM,Somebody),parent(Somebody,GC).

uncle(X,Y)    :- brother(Par, X), parent(Par,Y).
aunt(X,Y)     :- sister(Par, X),  parent(Par,Y).

nephew(X,Y)   :- male(Y),   (aunt(Y, X); uncle(Y, X)).
niece(X,Y)    :- female(Y), (aunt(Y, X); uncle(Y, X)).

%sister(X,Y)   :- female(X), parent(Par,X), parent(Par,Y), X \= Y.
%brother(X,Y)      :- male(X),   parent(Par,X), parent(Par,Y), X \= Y.

brother(B, P) :- male(B),   B \= P, siblings(Sib, P), member(B, Sib).
brother(B, P1) :- married(P1, P2), brother(B, P2).

sister(S, P)  :- female(S), S \= P, siblings(Sib, P), member(S, Sib).
sister(S, P1)  :- married(P1, P2), sister(S, P2).

siblings(Siblings, Person) :- parents(_, _, Siblings), member(Person, Siblings).
%brother(X,Y)  :- male(X), parents(_, _, Children), 
%                 member(X, Children), member(Y, Children), X \= Y.

cousin(X,Y)   :- uncle(Unc, X), father(Unc,Y).
cousin(X,Y)   :- aunt(Unc, X),  mother(Unc,Y).
ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Somebody),ancestor(Somebody,Y).

enby(X)        :- enbies(Y),    member(X, Y).

%%% end %%%
