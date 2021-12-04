module(ex05, []).

:- use_module(library(yaml/parser)).
:- use_module(library(yaml/util)).
:- use_module(library(dicts)).

assertDivisions(PL) :- dict_keys(PL.'divisions', Divisions),
 foreach(member(Division, Divisions), assertDivision(PL, Division)).

assertDivision(PL, Division) :-
 forall(member(Faculty, PL.'divisions'.Division), 
   addFaculty(Division, Faculty)).

addFaculty(Division, Faculty) :-
  assertz(faculty(Faculty)), assertz(divisionMember(Faculty, Division)).

procYaml :-
  read_yaml(file('soc-faculty.yaml'), YAML1), 
   parse(YAML1, PL1), assertDivisions(PL1),
  read_yaml(file('soc-research-categories.yaml'), YAML2), 
   parse(YAML2, PL2), assertMajorAreas(PL2).

%%%% end %%%%
