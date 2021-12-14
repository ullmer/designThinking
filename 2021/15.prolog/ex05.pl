module(ex05, []).

:- use_module(library(yaml/parser)).
:- use_module(library(yaml/util)).
:- use_module(library(dicts)).

assertDivisions(PL) :- dict_keys(PL.'divisions', Divisions),
 foreach(member(Division, Divisions), assertDivision(PL, Division)).

assertDivision(PL, Division) :- printBarred(Division),
 forall(member(Faculty, PL.'divisions'.Division), 
   addFaculty(Division, Faculty)).

addFaculty(Division, Faculty) :-
  format('~w ~w\n', [Division, Faculty]), assertz(faculty(Faculty)).   

procYaml :-
  read_yaml(file('soc-faculty.yaml'), YAML), parse(YAML, PL),
  assertDivisions(PL).

%%%% end %%%%
