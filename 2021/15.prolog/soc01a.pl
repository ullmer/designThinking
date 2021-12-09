module(soc01a, []).

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

%%%%%%%%%%%%%%%%% auto-assertions passage %%%%%%%%%%%%%%%%%%%

assertDivisions(YAML) :- dict_keys(YAML.'divisions', Divisions),
 foreach(member(Division, Divisions), assertDivision(YAML, Division)).

assertDivision(YAML, Division) :-
 forall(member(Faculty, YAML.'divisions'.Division), 
   addFaculty(Division, Faculty)).

addFaculty(Division, Faculty) :-
  assertz(faculty(Faculty)), assertz(divisionMember(Faculty, Division)).

assertMajorResearchAreas(YAMLwhole) :- 
 YAML = YAMLwhole.'researchAreas', dict_keys(YAML, MajorAreas),
 forall(member(MajorArea, MajorAreas), 
        assertSpecificAreas(YAML, MajorArea)).

assertManualResearchAbbrevs(YAMLwhole) :-
 YAML = YAMLwhole.'meta'.'manualAliases', 
 dict_keys(YAML, ManualAliases),
 forall(member(ManualAlias, ManualAliases),
        assertManualResearchAbbrev(YAML, ManualAlias)).

assertManualResearchAbbrev(YAML, ManualAlias) :-
  dict_keys(YAML.ManualAlias, SpecificAlias),
  format('~w ~w\n', 
    [SpecificAlias, YAML.ManualAlias.SpecificAlias]).

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

:- dynamic(areaAbbrev/2). % most instantiations may be expressed via assertz; 
                          % but one must exist for findall
areaAbbrev([], []).

assertAreaAbbreviation(Area) :-
  \+ areaAbbrev(Area, _), %no need to reassert if already present
  strToAbbrev(Area, Abbrev),
  assertz(areaAbbrev(Area, Abbrev)).

assertAreaAbbreviations([]).
assertAreaAbbreviations([H|T]) :- assertAreaAbbreviation(H), assertAreaAbbreviations(T).

assertAreaAbbreviations() :-
  %findall(MajorArea, researchArea(MajorArea, _), L),
  findall(MinorArea, researchArea(_, MinorArea), L),
  assertAreaAbbreviations(L). 

  %findall(SpecificArea, researchArea(MajorArea, SpecificArea), L),
  %assertAreaAbbreviations(L).

%abbreviatedArea(WholeName, Abbrev) :- researchArea(

%%%%%%%%%%%%%%%%% process YAML passage %%%%%%%%%%%%%%%%%%%

procYaml1 :-
  yaml_read('soc-faculty.yaml', YAML), 
  assertDivisions(YAML).

procYaml2 :-
  yaml_read('soc-research1b.yaml', YAML), 
   assertMajorResearchAreas(YAML),
   assertManualResearchAbbrevs(YAML).

procYaml :- procYaml1, procYaml2.

%%%% end %%%%
