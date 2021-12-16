module(soc01a, []).

:- use_module(library(yaml)).
:- use_module(library(dicts)).

%%%%%%%%%%%%% string processing and auto-abbreviation helpers %%%%%%%%%%%%%%%

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

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%% auto-assertions passage %%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%% assert divisions %%%%%%%%%%%%%%%%%%%

assertDivisions(YAML) :- dict_keys(YAML.'divisions', Divisions),
 foreach(member(Division, Divisions), assertDivision(YAML, Division)).

assertDivision(YAML, Division) :-
 forall(member(Faculty, YAML.'divisions'.Division), 
   addFaculty(Division, Faculty)).

%%%%%%%%%%%%%%%%% add faculty %%%%%%%%%%%%%%%%%%%

addFaculty(Division, Faculty) :-
  assertz(faculty(Faculty)), assertz(divisionMember(Faculty, Division)).

assertMajorResearchAreas(YAMLwhole) :- 
 YAML = YAMLwhole.'researchAreas', dict_keys(YAML, MajorAreas),
 forall(member(MajorArea, MajorAreas), 
        assertSpecificAreas(YAML, MajorArea)).

%%%%%%%%%%%%%%%%% assert manual research abbreviations %%%%%%%%%%%%%%%%%%%

assertManualResearchAbbrevs(YAMLwhole) :-
 YAMLmeta = YAMLwhole.'meta',               %writeln(YAMLmeta), 
 YAML = YAMLmeta.'manualAliases',           %writeln(YAML),
 dict_keys(YAML, ManualAliases),            %writeln(ManualAliases),
 forall(member(ManualAlias, ManualAliases), %writeln(ManualAlias)).
        assertManualResearchAbbrev(YAML, ManualAlias)).

assertManualResearchAbbrev(YAML, ManualAlias) :- %writeln(ManualAlias), 
  SpecificAlias = YAML.ManualAlias,     %format('~w ~w\n', [SpecificAlias, ManualAlias]),
  assertManualResearchAbbrv(ManualAlias, SpecificAlias).

assertManualResearchAbbrv(ManualAlias, SpecificAlias) :- 
  %writeln(['amra1', SpecificAlias]),
  string(SpecificAlias), 
  assertz(manualResearchAbbrev(ManualAlias, SpecificAlias)).

assertManualResearchAbbrv(ManualAlias, SpecificAliases) :- 
  %debug(['amra2', SpecificAliases]),
  is_list(SpecificAliases),
  forall(member(SpecificAlias, SpecificAliases),
    assertManualResearchAbbrv(ManualAlias, SpecificAlias)).

%%%%%%%%%%%%%%%%% assert specific research areas %%%%%%%%%%%%%%%%%%%

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
