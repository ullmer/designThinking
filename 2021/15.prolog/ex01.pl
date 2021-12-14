module(ex01, []).

:- use_module(library(yaml/parser)).
:- use_module(library(yaml/util)).
:- use_module(library(yaml/serializer)).

procYaml :-
    write('hello yaml'),
    read_yaml(file('soc-faculty.yaml'), YAML),
    parse(YAML, PL),
    print_term(PL, []),
    serialize(PL, YAML1),
    write(YAML1),
    write_yaml('soc-faculty-v2.yaml', YAML1).

