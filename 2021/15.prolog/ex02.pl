module(ex01, []).

:- use_module(library(yaml/parser)).
:- use_module(library(yaml/util)).
:- use_module(library(yaml/serializer)).

procYaml :-
    read_yaml(file('soc-faculty.yaml'), YAML),
    parse(YAML, PL),
    write(PL.'divisions'.'HCC').
