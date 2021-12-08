module(ex08, []).

:- use_module(library(yaml)).
:- use_module(library(dicts)).

strToWords(Str, Words)    :- split_string(Str, " ", " ", Words).
strFirstChar(Str, Letter) :- sub_atom(Str, 0, 1, _, Letter).
strToAbbrev(Str, Abbrev)  :- strToWords(Str, Words), 
                             atomics_to_string( 
                                foreach(member(Word, Words), 
                                        strFirstChar(Word)), Abbrev).
%maplist to be used in above? https://www.swi-prolog.org/pldoc/man?predicate=maplist/2

% https://stackoverflow.com/questions/47744096/prolog-concatenate-all-elements-inside-a-list-to-make-a-string

assertDivisions(YAML) :- dict_keys(YAML.'divisions', Divisions),
 foreach(member(Division, Divisions), assertDivision(YAML, Division)).

assertDivision(YAML, Division) :-
 forall(member(Faculty, YAML.'divisions'.Division), 
   addFaculty(Division, Faculty)).

addFaculty(Division, Faculty) :-
  assertz(faculty(Faculty)), assertz(divisionMember(Faculty, Division)).

assertMajorAreas(YAML) :- dict_keys(YAML, MajorAreas),
 forall(member(MajorArea, MajorAreas), assertSpecificAreas(YAML, MajorArea)).

assertSpecificAreas(YAML, MajorArea) :- 
 dict_keys(YAML.MajorArea, SpecificAreas),
 assertz(researchArea(MajorArea)),
 forall(member(SpecificArea, SpecificAreas), 
   assertSpecificArea(MajorArea, SpecificArea, 
     YAML.MajorArea.SpecificArea)).
   
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
