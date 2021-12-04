module(ex01, []).

:- use_module(library(yaml/parser)).
:- use_module(library(yaml/util)).
:- use_module(library(yaml/serializer)).
:- use_module(library(dicts)).

procDivisions(PL) :- dict_keys(PL.'divisions', Divisions),
    foreach(member(Division, Divisions), procDivision(PL, Division)).

procDivision(PL, Division) :- 
   Bar='===========', writeln(format('%s%s%s', [Bar, Division, Bar])),
   forall(member(Faculty, PL.'divisions'.Division), writeln(Faculty)).

procYaml :-
    read_yaml(file('soc-faculty.yaml'), YAML), parse(YAML, PL),
    procDivisions(PL).


