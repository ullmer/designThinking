module(ex06, []).

:- use_module(library(yaml)).
:- use_module(library(dicts)).

assertDivisions(PL) :- dict_keys(PL.'divisions', Divisions),
 foreach(member(Division, Divisions), assertDivision(PL, Division)).

assertDivision(PL, Division) :-
 forall(member(Faculty, PL.'divisions'.Division), 
   addFaculty(Division, Faculty)).

addFaculty(Division, Faculty) :-
  assertz(faculty(Faculty)), assertz(divisionMember(Faculty, Division)).

assertMajorAreas(PL) :- dict_keys(PL.'researchAreas', MajorAreas),
 writeln(MajorAreas),
 forall(member(MajorArea, MajorAreas), writeln(MajorArea)).

procYaml1 :-
  read_yaml(file('soc-faculty.yaml'), YAML), 
   parse(YAML, PL), assertDivisions(PL).

procYaml2 :-
  yaml_read('soc-research-categories.yaml', YAML), 
   %writeln(YAML), 
   assertMajorAreas(YAML).

%  read_yaml(file('soc-research-categories.yaml'), YAML), 

%%%% end %%%%
