module(ex06, []).

:- use_module(library(yaml)).
:- use_module(library(dicts)).

assertDivisions(YAML) :- dict_keys(YAML.'divisions', Divisions),
 foreach(member(Division, Divisions), assertDivision(YAML, Division)).

assertDivision(YAML, Division) :-
 forall(member(Faculty, YAML.'divisions'.Division), 
   addFaculty(Division, Faculty)).

addFaculty(Division, Faculty) :-
  assertz(faculty(Faculty)), assertz(divisionMember(Faculty, Division)).

assertMajorAreas(YAML) :- dict_keys(YAML.'researchAreas', MajorAreas),
 forall(member(MajorArea, MajorAreas), assertSpecificAreas(YAML, MajorArea)).

assertSpecificAreas(YAML, MajorArea) :- 
 dict_keys(YAML.'researchAreas'.MajorArea, SpecificAreas),
 assertz(researchArea(MajorArea)),
 forall(member(SpecificArea, SpecificAreas), 
   assertSpecificArea(MajorArea, SpecificArea, 
     YAML.'researchAreas'.MajorArea.SpecificArea]))).
   
assertSpecificArea(MajorArea, SpecificArea, PersonList) :-
  assertz(researchArea(MajorArea, SpecificArea)),
  forall(member(Person, PersonList), 
    assertz(researchFocus(Person, MajorArea, SpecificArea))).

procYaml1 :-
  yaml_read('soc-faculty.yaml', YAML), 
  assertDivisions(YAML).

procYaml2 :-
  yaml_read('soc-research-categories.yaml', YAML), 
   assertMajorAreas(YAML).


%%%% end %%%%
