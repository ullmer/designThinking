module(ex04, []).

:- use_module(library(yaml/parser)).
:- use_module(library(yaml/util)).
:- use_module(library(yaml/serializer)).
:- use_module(library(dicts)).

printBarred(Str) :- 
  Bar='===========', format('\n~w ~w ~w\n', [Bar, Str, Bar]).

procDivisions(PL) :- dict_keys(PL.'divisions', Divisions),
    foreach(member(Division, Divisions), procDivision(PL, Division)).

procDivision(PL, Division) :- printBarred(Division),
   forall(member(Faculty, PL.'divisions'.Division), writeln(Faculty)).

procYaml :-
    read_yaml(file('soc-faculty.yaml'), YAML), parse(YAML, PL),
    procDivisions(PL).


