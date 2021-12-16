module(soc01a, []).

:- use_module(library(yaml)).
:- use_module(library(dicts)).

%%%%%%%%%%%%% string processing and auto-abbreviation helpers %%%%%%%%%%%%%%%

strToWords(Str, Words)    :- split_string(Str, " -", " ", Words).
strFirstChar("and", "&").
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
 assertz(division(Division)),
 forall(member(Faculty, YAML.'divisions'.Division), 
   addFaculty(Division, Faculty)).

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
  assertz(areaAbbrev(ManualAlias, SpecificAlias)).

assertManualResearchAbbrv(ManualAlias, SpecificAliases) :- 
  %debug(['amra2', SpecificAliases]),
  is_list(SpecificAliases),
  forall(member(SpecificAlias, SpecificAliases),
    assertManualResearchAbbrv(ManualAlias, SpecificAlias)).

%%%%%%%%%%%%%%%%% add faculty %%%%%%%%%%%%%%%%%%%

addFaculty(Division, Faculty) :-
  assertz(faculty(Faculty)), assertz(divisionMember(Faculty, Division)).

assertResearchAreas(YAMLwhole) :- 
 YAML = YAMLwhole.'researchAreas', dict_keys(YAML, MajorAreas),
 writeln(MajorAreas),
 forall(member(MajorArea, MajorAreas), 
        assertSpecificAreas(YAML, MajorArea)).

%%%%%%%%%%%%%%%%% assert specific research areas %%%%%%%%%%%%%%%%%%%

assertSpecificAreas(YAML, MajorArea) :- 
 Area = YAML.MajorArea, dict_keys(Area, SpecificAreas),
 assertz(researchArea(MajorArea)),
 forall(member(SpecificArea, SpecificAreas), 
   assertSpecificArea(MajorArea, SpecificArea, Area.SpecificArea)).
   
assertSpecificArea(MajorArea, SpecificArea, PersonList) :-
  assertz(researchArea(MajorArea, SpecificArea)),
  forall(member(Person, PersonList), 
    assertz(researchFocus(Person, MajorArea, SpecificArea))).

:- dynamic(areaAbbrev/2). % most instantiations to be expressed via assertz; 
                          % but one must exist for findall
areaAbbrev([], []).

researchFocusByPersonAbbrev(PersonAbbrev, MajorArea, SpecificArea) :-
  personAbbrev(Person, PersonAbbrev),
  researchFocus(Person, MajorArea, SpecificArea).

researchFocusByMajorAbbrev(Person, MajorAreaAbbrev, SpecificArea) :-
  areaAbbrev(MajorArea, MajorAreaAbbrev),
  researchFocus(Person, MajorArea, SpecificArea).

assertAreaAbbreviation(Area) :- areaAbbrev(Area, _).

assertAreaAbbreviation(Area) :- %writeln(Area),
  strToAbbrev(Area, Abbrev),
  assertz(areaAbbrev(Area, Abbrev)).

areaAbbrevRE(Area, AbbrevRE) :-
  areaAbbrev(Area, Abbrev), wildcard_match(AbbrevRE, Abbrev).

areaAbbrevRE(Area, Abbrev, AbbrevRE) :-
  areaAbbrev(Area, Abbrev), wildcard_match(AbbrevRE, Abbrev).

areaAbbrevRE(Area, Abbrev, AbbrevRE) :- 
  areaAbbrev(Area, Abbrev), wildcard_match(AbbrevRE, Abbrev).

areaAbbrevsRE(AbbrevRE, L2) :- 
  findall([Abbrev, Area], areaAbbrevRE(Area, Abbrev, AbbrevRE), L1),
  sort(L1, L2).

majorAreaAbbrev(Area, Abbrev) :- researchArea(Area), areaAbbrev(Area, Abbrev).

listMajorAreas(L2) :- 
  findall([Abbrev, Area], majorAreaAbbrev(Area, Abbrev), L1), sort(L1, L2).



listDivisions(L2) :- 
  findall([Abbrev, Area], majorAreaAbbrev(Area, Abbrev), L1), sort(L1, L2).

print(divions)               :- listDivisions(L),  printTable(L).
print(majorArea)             :- listMajorAreas(L), printTable(L).
printAreaRE(all, AbbrevRE)   :- areaAbbrevsRE(AbbrevRE, L), printTable(L).
printAreaRE(AbbrevRE)          :- printAreaRE('all', AbbrevRE). % default

assertAreaAbbreviations([]).
assertAreaAbbreviations([H|T]) :- assertAreaAbbreviation(H), assertAreaAbbreviations(T).

assertAreaAbbreviations() :-
  findall(MinorArea, researchArea(_, MinorArea), L1),
  assertAreaAbbreviations(L1),

  findall(MajorArea, researchArea(MajorArea, _), L2),
  assertAreaAbbreviations(L2).

  %findall(SpecificArea, researchArea(MajorArea, SpecificArea), L),
  %assertAreaAbbreviations(L).

%abbreviatedArea(WholeName, Abbrev) :- researchArea(

%%%%%%%%%%%%%%%%% person abbreviations%%%%%%%%%%%%%%%%%%%

:- dynamic(personAbbrev/2).
personAbbrev([], []).

personAbbrevRE(FullName, AbbrevRE) :- 
  personAbbrev(FullName, Abbrev), wildcard_match(AbbrevRE, Abbrev).

personAbbrevsRE(FullName, AbbrevRE, L2) :- 
  findall(FullName, personAbbrevRE(FullName, AbbrevRE), L1),
  sort(L1, L2).

personAbbrevsRE(FullName, Abbrev, AbbrevRE, L2) :- 
  findall([Abbrev, FullName], personAbbrevRE(FullName, Abbrev, AbbrevRE), L1),
  sort(L1, L2).

personAbbrevsRE(AbbrevRE, L2) :- 
  findall([Abbrev, FullName], personAbbrevRE(FullName, Abbrev, AbbrevRE), L1),
  sort(L1, L2).

printPeopleRE(AbbrevRE) :- personAbbrevsRE(AbbrevRE, L), printTable(L).

personAbbrevRE(FullName, Abbrev, AbbrevRE) :- 
  personAbbrev(FullName, Abbrev), wildcard_match(AbbrevRE, Abbrev).

assertPersonAbbreviation(Person) :- personAbbrev(Person, _).
assertPersonAbbreviation(Person) :-
  strToAbbrev(Person, Abbrev),
  assertz(personAbbrev(Person, Abbrev)).

assertPersonAbbreviations() :-
  findall(Person, faculty(Person), People),
  forall(member(P, People), assertPersonAbbreviation(P)).

%%%%%%%%%%%%%%%%% print table %%%%%%%%%%%%%%%%%%%

printTable([]).
printTable([H|T]) :-
  format('~w\t~w\n', H), printTable(T).

%%%%%%%%%%%%%%%%% process YAML passage %%%%%%%%%%%%%%%%%%%

procYamlFaculty :-
  yaml_read('soc-faculty.yaml', YAML), 
  assertDivisions(YAML).

procYamlResearch :-
  yaml_read('soc-research1b.yaml', YAML), 
   assertResearchAreas(YAML),
   assertManualResearchAbbrevs(YAML).

procYaml :- procYamlFaculty, procYamlResearch, 
  assertAreaAbbreviations,
  assertPersonAbbreviations.

%%%% end %%%%
