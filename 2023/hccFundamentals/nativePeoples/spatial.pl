% Initial spatial relations.  Consultation needed on terminology
% Brygg Ullmer, Clemson University
% Begun 2023-11-22

:- use_module(library(lists)).

tribeIntersectsState(State, Name) :- 
        tribe(_, _, States, Name), 
            member(State, States).

tribeIntersectsState(State, Bia, Epa, States, Name) :- 
                      tribe(Bia, Epa, States, Name), 
                        member(State, States).

tribeIntersectsRegion(Region, Name, State) :-
         tribe(_, _, States1, Name),
         beaRegion(Region, States2),
             member(State, States2),
             member(State, States1).

tribesIntersectRegion(Region, Names) :-
  findall(Name, tribeIntersectsRegion(Region, Name, _), Names).

%tribeIntersectsRegion(Region, Name, CommonStates) :-
%         tribe(_, _, States1, Name),
%         beaRegion(Region, States2),
%     intersection(States1, States2, CommonStates).

%%% end %%%
