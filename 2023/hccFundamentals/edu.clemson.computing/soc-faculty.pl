% Prolog representation of Clemson University School of Computing faculty
% Brygg Ullmer, Clemson University
% Begun 2021-01-05

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

  FOI: [Svetlana Drachova, Yvon Feaster, Alexander Herzog, 
        Catherine Kittelstad, Christopher Plaue, Carrie Russell, Mitch Shue, 
        Yu-Shan Sun, Connie Taylor, Roger Van Scoy, Nicolas Widman]


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

domCat(inst, dncpsci, [Domain, State, City, Country, People]) :-
  institution(Domain, State, City, Country, People).

institutions(X) :- findall(Y, institution(Y, _, _, _, _), X).

institution(  brown.edu, ri, pvd, usa, [jt]).
institution(clemson.edu, sc, ceu, usa, [aa, ep, sd, yf, ck, cr]).
institution(  mines.edu, co, den, usa, [kl]). 
institution(   udel.edu, de, ilg, usa, [nl]).
institution(    gmu.edu, va, dca, usa, [ms]).
institution( gatech.edu, ga, atl, usa, [kc, ek, vz, cp]). 
institution(indiana.edu, in, bmg, usa, [gf]).
institution(    jhu.edu, md, bwi, usa, [ct]).
institution(    mit.edu, ma, bos, usa, [bcd, wg, bu]).
institution(   ncsu.edu, nc, rdu, usa, [jm]).
institution(    osu.edu, oh, osu, usa, [ms]).
institution(    psu.edu, pa, unv, usa, [nm]).
institution(   scad.edu, ga, sav, usa, [ik]).
institution(     tum.de,  _, muc, deu, [nh]).
institution(   tamu.edu, tx, cll, usa, [ad]).
institution(   unibe.ch,  _, brn, che, [dsd]).
institution(    uci.edu, ca, sna, usa, [bk]).
institution(   ucla.edu, ca, lax, usa, [nw]).
institution(    ucf.edu, fl, mco, usa, [jw]).
institution( 
  tcd.ie:         {ftd: [Joerg],                           cab: DUB, ia3: IRL}
institution( 
  ufl.edu:        {ftd: [Brinkley, Robb],         sab: FL, cab: GNV, ia3: USA}
institution( 
  unige.it:       {ftd: [Iuricich],                        cab: GOA, ia3: ITA}
institution( 
  umaine.edu:     {ftd: [Razi],                   sab: ME, cab: BDL, ia3: USA}
institution( 
  umass.edu:      {ftd: [Sorber],                 sab: MA, cab: BGR, ia3: USA}
institution( 
  unc.edu:        {ftd: [Smotherman],             sab: NC, cab: RDU, ia3: USA}
institution( 
  charlotte.edu:  {ftd: [Babu],                   sab: NC, cab: CLT, ia3: USA}
institution( 
  pitt.edu:       {ftd: [Van Scoy],               sab: PA, cab: PIT, ia3: USA}
institution( 
  utdallas.edu:   {ftd: [Luo],                    sab: TX, cab: DFW, ia3: USA}
institution( 
  virginia.edu:   {ftd: [Hedetniemi],             sab: VA, cab: CHO, ia3: USA}
institution( 
  uu.nl:          {ftd: [Karamouzas],                      cab: UTC, ia3: NLD}
institution( 
  vanderbilt.edu: {ftd: [Apon],                   sab: TN, cab: BNA, ia3: USA}
institution( 
  vatech.edu:     {ftd: [Cheng, Ge],              sab: VA, cab: ROA, ia3: USA}
institution( 
  washington.edu: {ftd: [Jin],                    sab: WA, cab: SEA, ia3: USA}

category(acadRank, Rank, P) :- acadRank(P, Rank).

acadRank(P, Rank) :- person(P, flr,  L),  nth0(L, 2, Rank).
acadRank(P, Rank) :- person(P, fmlr, L),  nth0(L, 3, Rank).
acadRank(P, Rank) :- person(P, fmlrr, L), nth0(L, 3, Rank).

division(P, Division) :- person(P, flr,  L),  nth0(L, 2, Rank).
acadRank(P, Rank) :- person(P, fmlr, L),  nth0(L, 3, Rank).
acadRank(P, Rank) :- person(P, fmlrr, L), nth0(L, 3, Rank).

### end ###
