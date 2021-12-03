:- use_module(library(yaml/parser)).
:- use_module(library(yaml/util)).
:- use_module(library(yaml/serializer)).


module(ex, []).

:- use_module(library(yaml/parser)).
:- use_module(library(yaml/util)).
:- use_module(library(yaml/serializer)).

ex1 :-
    read_yaml('ex1.yaml', YAML),
    parse(YAML, PL),
    print_term(PL, []),
    serialize(PL, YAML1),
    write(YAML1),
    write_yaml('ex1_gen.yaml', YAML1).

