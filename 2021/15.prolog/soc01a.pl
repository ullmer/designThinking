module(cu-soc01a, []).

:- use_module(library(yaml)).
:- use_module(library(dicts)).

strToWords(Str, Words)    :- split_string(Str, " -", " ", Words).
strFirstChar("and", '&').
strFirstChar(Str, Letter) :- sub_atom(Str, 0, 1, _, Letter).

%abbrevSeq: recursively transform list of words (produced by strToWords)
% to list of letters (extracted by strFirstChar).  

abbrevSeq([],[]). 
abbrevSeq([H|T], Abbrev) :- 
  strFirstChar(H, HfirstChar), abbrevSeq(T, TailAbbrev), 
  append([HfirstChar], TailAbbrev, Abbrev).

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

assertMajorResearchAreas(YAMLwhole) :- YAML = YAMLwhole.'researchAreas', 
 dict_keys(YAML, MajorAreas),
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

%abbreviatedArea(WholeName, Abbrev) :- researchArea(
%strToAbbrev(Str, Abbrev)  :- 

procYaml :- procYaml1, procYaml2.

procYaml1 :-
  yaml_read('soc-faculty.yaml', YAML), 
  assertDivisions(YAML).

procYaml2 :-
  yaml_read('soc-research1b.yaml', YAML), 
   assertMajorResearchAreas(YAML).

%%%% end %%%%
