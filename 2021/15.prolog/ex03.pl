module(ex01, []).

:- use_module(library(yaml/parser)).
:- use_module(library(yaml/util)).
:- use_module(library(yaml/serializer)).

assertFaculty(X) :- assertz(faculty(X)).

procYaml :-
    read_yaml(file('soc-faculty.yaml'), YAML),
    parse(YAML, PL),
    assertFaculty(PL.'divisions'.'HCC'.X)).
