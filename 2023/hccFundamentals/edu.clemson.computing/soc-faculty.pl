% Prolog representation of Clemson University School of Computing faculty
% Brygg Ullmer, Clemson University
% Begun    2021-01-05
% Extended 2023-11-20

%%%%%%%%%%%%%% CS %%%%%%%%%%%%%%

category(division, cs,  hncp, [soc, 'Computer Science',
  [apon, dean, hubig, liu, luo, wang, yang, goddard, 
   smotherman, sorber, westall, donar, rodeghero, ge, 
   cheng, razi, zhang, li]]).

person(apon,       flr,  [aa,  'Amy',         'Apon',       full])
person(cheng,      flr,  [lc,  'Long',        'Cheng',      asst]).
person(dean,       fmlrr,[bcd, 'Brian', 'C.', 'Dean',       full, director]).
person(hubig,      flr,  [nh,  'Nina',        'Hubig',      asst]).
person(li,         flr,  [nl,  'Nianyi',      'Li',         asst]).
person(liu,        flr,  [kl,  'Kai',         'Liu',        asst]).
person(luo,        flr,  [fl,  'Feng',        'Luo',        full]).
person(ge,         flr,  [rg,  'Rong',        'Ge',         assoc]).
person(goddard,    flr,  [wg,  'Wayne',       'Goddard',    full]).
person(rodeghero,  flr,  [pr,  'Paige,        'Rodeghero',  asst]).
person(smotherman, flr,  [ms,  'Mark',        'Smotherman', assoc]).
person(sorber,     flrr, [js,  'Jacob',       'Sorber',     full, chair]).
person(razi,       flr,  [ar,  'Abolfazi',    'Razi',       assoc]).
person(wang,       flr,  [jw,  'James',       'Wang',       full]).
person(zhang,      flr,  [zz,  'Zhenkai',     'Zhang',      asst]).
person(westall,    flr,  [mw,  'Mike',        'Westall',    resprof]).
person(donar,      flr,  [dd,  'David',       'Donar',      adjassoc]).

%%%%%%%%%%%%%% HCC %%%%%%%%%%%%%%

category(division, hcc,  hncp, [soc, 'Human-Centered Computing',
  [babu, brinkley, caine, dixon, freeman, knijnenburg, kraemer, 
   mcneese, robb, ullmer]]).

person(babu,        flr,  [sb, 'Sabarish', 'Babu',        assoc]).
person(brinkley,    flr,  [jb, 'Julian',   'Brinkley',    asst ]).
person(caine,       flr,  [kc, 'Kelly',    'Caine',       full ]).
person(dixon,       flr,  [ed, 'Emma',     'Dixon',       asst ]).
person(freeman,     flr,  [gf, 'Guo',      'Freeman',     assoc]).
person(hernandez,   flr,  [ch, 'Carlos',   'Hernandez',   asst ]).
person(knijnenburg, flr,  [bk, 'Bart',     'Knijnenburg', assoc]).
person(kraemer,     flr,  [ek, 'Eileen',   'Kraemer',     full ]).
person(mcneese,     flr,  [nm, 'Nathan',   'McNeese',     assoc]).
person(robb,        flr,  [ar, 'Andrew',   'Robb',        assoc]).
person(ullmer,      flr,  [bu, 'Brygg',    'Ullmer',      full ]).

%%%%%%%%%%%%%% VC %%%%%%%%%%%%%%

category(division, vc,  hncp, [soc, 'Visual Computing',
  [jin, karamouzas, patterson, iuricich, tessendorf, zordan, 
   singhdhillon, duchowski]]).

person(jin,          flr,  [sj,  'Shuangshuang', 'Jin',       assoc]).
person(patterson,    flr,  [ep,  'Eric',     'Patterson',     assoc]).
person(iuricich,     flr,  [fi,  'Federico', 'Iuricich',      asst ]).
person(tessendorf,   flr,  [jt,  'Jerry',    'Tessendorf',    full ]).
person(zordan,       flr,  [vz,  'Victor,    'Zordan',        full ]).
person(singhdhillon, flr,  [dsd, 'Daljit',   'Singh Dhillon', asst ]).
person(duchowski,    flr,  [ad,  'Andrew',   'Duchowski',     full ]).

%%%%%%%%%%%%%% FOI %%%%%%%%%%%%%%

category(division, fcoi,  hncp, [soc, 'Faculty of Instruction',
  [drachova, feaster, kittelstad, plaue, russell, shue, sun, taylor, vanscoy, widman]).

person(jin,          flr,  [sj,  'Shuangshuang', 'Jin',       assoc]).
  FOI: [Svetlana Drachova, Yvon Feaster, Alexander Herzog, 
        Catherine Kittelstad, Christopher Plaue, Carrie Russell, Mitch Shue, 
        Yu-Shan Sun, Connie Taylor, Roger Van Scoy, Nicolas Widman]


rank(X, asst)      :- person(X, flr, [_, _, _,  asst]).
rank(X, assoc)     :- person(X, flr, [_, _, _, assoc]).
rank(X, full)      :- person(X, flr, [_, _, _,  full]).
rank(X, lecturer)  :- person(X, flr, [_, _, _,  lecturer]).
rank(X, slecturer) :- person(X, flr, [_, _, _,  slecturer]).
rank(X, pop)       :- person(X, flr, [_, _, _,  pop]).
%chair(X)       :- person(X, 

rank:
  asst:      [Brinkley, Cheng, Singh Dhillon, Freeman, Hubig, Iuricich,
              Karamouzas, Li, Liu, McNeese, Robb, Rodeghero, Zhang]
  assoc:     [Babu, Caine, Donar, Ge, Jin, Joerg, Knijnenburg, Patterson,
              Razi, Smotherman, Sorber, Yang]
  full:      [Apon, Dean, Duchowski, Goddard, Hedetniemi, Kraemer, Luo, Martin,
              Sitaraman, Srimani, Tessendorf, Ullmer, Wang, Zordan]
  lecturer:  [Drachova, Sun, Widman]
  slecturer: [Feaster, Kittelstad, Plaue]
  pop:       [Kwon, Russell, Shue, Taylor, Van Scoy]

%           Domain, State, City, Country, PhD,  Mx, Bx 
institution(     brown.edu, ri, pvd, usa, [jt],                     [], [], []).
institution(   clemson.edu, sc, ceu, usa, [aa, ep, sd, yf, ck, cr], [], [], []).
institution(     mines.edu, co, den, usa, [kl],                     [], [], []). 
institution(      udel.edu, de, ilg, usa, [nl],                     [], [], []).
institution(       gmu.edu, va, dca, usa, [ms],                     [], [], []).
institution(    gatech.edu, ga, atl, usa, [kc, ek, vz, cp],         [], [], []). 
institution(  illinois.edu, il, cmi, usa, [],                       [], [bu], []).
institution(   indiana.edu, in, bmg, usa, [gf],                     [], [], []).
institution(       jhu.edu, md, bwi, usa, [ct],                     [], [], []).
institution(       mit.edu, ma, bos, usa, [bcd, wg, bu],            [bu], [bcd], []).
institution(      ncsu.edu, nc, rdu, usa, [jm],                     [], [], []).
institution(       osu.edu, oh, osu, usa, [ms],                     [], [], []).
institution(       psu.edu, pa, unv, usa, [nm],                     [], [], []).
institution(      scad.edu, ga, sav, usa, [ik],                     [], [], []).
institution(       tum.de,   _, muc, deu, [nh],                     [], [], []).
institution(      tamu.edu, tx, cll, usa, [ad],                     [], [], []).
institution(     unibe.ch,   _, brn, che, [dsd],                    [], [], []).
institution(       uci.edu, ca, sna, usa, [bk],                     [], [], []).
institution(      ucla.edu, ca, lax, usa, [nw],                     [], [], []).
institution(       ucf.edu, fl, mco, usa, [jw],                     [], [], []).
institution(       ufl.edu, fl, gnv, usa, [jb],                     [], [], []).
institution(      unige.it,  _, goa, ita, [fi],                     [], [], []).
institution(    umaine.edu, me, bdl, usa, [ar],                     [], [], []).
institution(     umass.edu, ma, bgr, usa, [js],                     [], [], []).
institution(       unc.edu, nc, rdu, usa, [ms],                     [], [], []).
institution( charlotte.edu, nc, clt, usa, [sb],                     [], [], []).
institution(      pitt.edu, pa, pit, usa, [rvs],                    [], [], []).
institution(  poly.edu.hk,   _, hkg, hkg, [],                       [], [], [bu]).
institution(  utdallas.edu, tx, dfw, usa, [fl],                     [], [], []).
institution(vanderbilt.edu, tn, bna, usa, [aa],                     [], [], []).
institution(    vatech.edu, va, roa, usa, [lc, rg],                 [], [], []).
institution(washington.edu, wa, sea, usa, [sj],                     [], [], []).
institution(       zib.de,   _, ber, deu, [],                       [], [], [bu]).

%%%%%%%%%%%%%% Generalizations %%%%%%%%%%%%%%

institutions(X) :- findall(Y, institution(Y, _, _, _, _), X).

domCat(inst, dncpsci, [Domain, State, City, Country, People]) :-
  institution(Domain, State, City, Country, People).

category(acadRank, Rank, P) :- acadRank(P, Rank).

acadRank(P, Rank) :- person(P, flr,   L), nth0(L, 2, Rank).
acadRank(P, Rank) :- person(P, fmlr,  L), nth0(L, 3, Rank).
acadRank(P, Rank) :- person(P, fmlrr, L), nth0(L, 3, Rank).

division(P, Division) :- person(P, flr,  L),  nth0(L, 2, Rank).
acadRank(P, Rank)     :- person(P, fmlr, L),  nth0(L, 3, Rank).
acadRank(P, Rank)     :- person(P, fmlrr, L), nth0(L, 3, Rank).

%%% end %%%
