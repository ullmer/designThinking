module(ex08, []).

:- use_module(library(yaml)).
:- use_module(library(dicts)).

strToWords(Str, Words)    :- split_string(Str, " ", " ", Words).
strFirstChar(Str, Letter) :- sub_atom(Str, 0, 1, _, Letter).

%abbrevSeq: recursively transform list of words (produced by strToWords)
% to list of letters (extracted by strFirstChar).  

abbrevSeq([],[]). 
abbrevSeq([H|T], Abbrev) :- 
  strFirstChar(H, Hfc), abbrevSeq(T, Abbrev2), 
  append([Hfc], Abbrev2, Abbrev).

strToAbbrev(Str, Abbrev)  :- 
  strToWords(Str, Words), abbrevSeq(Words, Chars), 
  atomics_to_string(Chars, Abbrev).

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
