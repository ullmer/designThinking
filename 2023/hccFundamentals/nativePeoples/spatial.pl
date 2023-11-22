% Initial spatial relations.  Consultation needed on terminology
% Brygg Ullmer, Clemson University
% Begun 2023-11-22

tribeIntersectsState(State, Name) :- 
        tribe(_, _, States, Name), 
            member(State, States).

tribeIntersectsState(State, Bia, Epa, States, Name) :- 
                      tribe(Bia, Epa, States, Name), 
                        member(State, States).

tribeIntersectsRegion(Region, Name) :-
           tribe(_, _, States1, Name),
           beaRegion(Region, States2),
          intersect(States1, States2).

%%% end %%%
