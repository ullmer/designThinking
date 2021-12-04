module(ex06, []).

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

assertMajorAreas(PL) :- dict_keys(PL.'majorAreas', MajorAreas),
 writeln(MajorAreas),
 forall(member(MajorArea, MajorAreas), writeln(MajorArea)).

procYaml1 :-
  read_yaml(file('soc-faculty.yaml'), YAML), 
   parse(YAML, PL), assertDivisions(PL).

procYaml2 :-
  read_yaml(file('soc-research-categories.yaml'), YAML), 
   parse(YAML, PL), writeln('foo'), assertMajorAreas(PL).

%%%% end %%%%
