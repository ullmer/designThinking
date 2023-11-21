% Prolog representation of Clemson University School of Computing faculty
% Brygg Ullmer, Clemson University
% Begun 2021-01-05

category(acadRank, Rank, P) :- acadRank(P, Rank).

acadRank(P, Rank) :- person(P, flr,  L),  nth0(L, 2, Rank).
acadRank(P, Rank) :- person(P, fmlr, L),  nth0(L, 3, Rank).
acadRank(P, Rank) :- person(P, fmlrr, L), nth0(L, 3, Rank).

division(P, Division) :- person(P, flr,  L),  nth0(L, 2, Rank).
acadRank(P, Rank) :- person(P, fmlr, L),  nth0(L, 3, Rank).
acadRank(P, Rank) :- person(P, fmlrr, L), nth0(L, 3, Rank).


%%%%%%%%%%%%%% CS %%%%%%%%%%%%%%

category(division, cs,  hncp, [soc, 'Computer Science',
  [apon, dean, hubig, liu, luo, wang, yang, goddard, hedetniemi, srimani, 
   smotherman, martin, sorber, westall, donar, rodeghero, sitaraman, ge, 
   cheng, razi, zhang, li]]).

person(apon,       flrr, ['Amy',    'Apon',       full, director]).
person(cheng,      flr,  ['Long',   'Cheng',      asst]).
person(dean,       fmlrr,['Brian',  'C.', 'Dean', full, chair]).
person(hubig,      flr,  ['Nina',   'Hubig',      asst]).
person(li,         flr,  ['Nianyi',   'Li',       asst]).
person(liu,        flr,  ['Kai',    'Liu',        asst]).
person(luo,        flr,  ['Feng',   'Luo',        full]).
person(ge,         flr,  ['Rong',   'Ge',         assoc]).
person(goddard,    flr,  ['Wayne',  'Goddard',    full]).
person(hedetniemi, flr,  ['Sandra', 'Hedetniemi', full]).
person(martin,     flr,  ['Jim',    'Martin',     full]).
person(rodeghero,  flr,  ['Paige,   'Rodeghero',  asst]).
person(sitaraman,  flr,  ['Murali', 'Sitaraman',  prof]).
person(smotherman, flr,  ['Mark',   'Smotherman', assoc]).
person(sorber,     flr,  ['Jacob',  'Sorber',     assoc]).
person(srimani,    flr,  ['Pradip', 'Srimani',    full]).
person(razi,       flr,  ['Abolfazi', 'Razi',     assoc]).
person(wang,       flr,  ['James',  'Wang',       full]).
person(yang,       flr,  ['Yin',    'Yang',       assoc]).
person(zhang,      flr,  ['Zhenkai',  'Zhang',    asst]).
person(westall,    flr,  ['Mike',   'Westall',    resprof]).
person(donar,      flr,  ['David',  'Donar',      adjassoc]).

%%%%%%%%%%%%%% HCC %%%%%%%%%%%%%%

category(division, hcc,  hncp, [soc, 'Human-Centered Computing',
  [babu, brinkley, caine, freeman, knijnenburg, kraemer, 
   mcneese, robb, ullmer]]).

person(babu,        flr,  ['Sabarish', 'Babu',        assoc]).
person(brinkley,    flr,  ['Julian',   'Brinkley',    asst]).
person(caine,       flr,  ['Kelly',    'Caine',       assoc]).
person(freeman,     flr,  ['Guo',      'Freeman',     asst]).
person(knijnenburg, flr,  ['Bart',     'Knijnenburg', assoc]).
person(kraemer,     flr,  ['Eileen',   'Kraemer',     full]).
person(mcneese,     flr,  ['Nathan',   'McNeese',     asst]).
person(robb,        flr,  ['Andrew',   'Robb',        asst]).
person(ullmer,      flr,  ['Brygg',    'Ullmer',      full]).

%%%%%%%%%%%%%% VC %%%%%%%%%%%%%%

category(division, vc,  hncp, [soc, 'Visual Computing',
  [jin, joerg, karamouzas, patterson, iuricich, tessendorf, zordan, 
   singhdhillon, duchowski, kwon]]).

person(jin,        flr,  ['Shuangshuang', 'Jin',    assoc]).
person(joerg,      flr,  ['Sophie',       'Joerg',  assoc]).
person(karamouzas, flr,  ['Ioannis',      'Karamouzas', asst]).
person(patterson,  flr,  ['Eric', 'Patterson', assoc]).
person(iuricich,   flr,  ['Federico', 'Iuricich', asst]).
person(tessendorf, flr,  ['Jerry', 'Tessendorf', full]).
person(zordan,     flr,  ['Victor, 'Zordan', full]).
person(,        flr,  ['
Daljit Singh Dhillon
person(,        flr,  ['
Andrew Duchowski
person(,        flr,  ['
Insun Kwon
person(,        flr,  ['



  FOI: [Svetlana Drachova, Yvon Feaster, Alexander Herzog, 
        Catherine Kittelstad, Christopher Plaue, Carrie Russell, Mitch Shue, 
        Yu-Shan Sun, Connie Taylor, Roger Van Scoy, Nicolas Widman]

doCat(inst, brown, dncpsci, ['brown.edu', 'Brown University', [tessendorf], ri, pvd, usa]).

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

institutions: #ftd: Faculty w/ Terminal Degrees; sab, cab: State, City Abbrv
  brown.edu:      {ftd: [Tessendorf],             sab: RI, cab: PVD, ia3: USA}
  clemson.edu:    {ftd: [Patterson, Drachova, Feaster, Kittelstad, Russell, Sun],
                                                  sab: SC, cab: CEU, ia3: USA}
  mines.edu:      {ftd: [Liu],                    sab: CO, cab: DEN, ia3: USA}   
  udel.edu:       {ftd: [Li],                     sab: DE, cab: ILG, ia3: USA}
  gmu.edu:        {ftd: [Shue],                   sab: VA, cab: DCA, ia3: USA}
  gatech.edu:     {ftd: [Caine, Kraemer, Zordan, Plaue], 
                                                  sab: GA, cab: ATL, ia3: USA}
  indiana.edu:    {ftd: [Freeman],                sab: IN, cab: BMG, ia3: USA}
  jhu.edu:        {ftd: [Taylor],                 sab: MD, cab: BWI, ia3: USA}
  mit.edu:        {ftd: [Dean, Goddard, Ullmer],  sab: MA, cab: BOS, ia3: USA}
  ncsu.edu:       {ftd: [Martin],                 sab: NC, cab: RDU, ia3: USA}
  osu.edu:        {ftd: [Sitaraman],              sab: OH, cab: OSU, ia3: USA}
  psu.edu:        {ftd: [McNeese],                sab: PA, cab: UNV, ia3: USA}
  scad.edu:       {ftd: [Kwon],                   sab: GA, cab: SAV, ia3: USA}
  tum.de:         {ftd: [Hubig],                           cab: MUC, ia3: DEU}
  tamu.edu:       {ftd: [Duchowski],              sab: TX, cab: CLL, ia3: USA}
  unibe.ch:       {ftd: [Dhillon Singh],                   cab: BRN, ia3: CHE}
  caluniv.ac.in:  {ftd: [Srimani],                         cab: CCU, ia3: IND}
  uci.edu:        {ftd: [Knijnenburg],            sab: CA, cab: SNA, ia3: USA}
  ucla.edu:       {ftd: [Widman],                 sab: CA, cab: LAX, ia3: USA}
  ucf.edu:        {ftd: [Wang],                   sab: FL, cab: MCO, ia3: USA}
  tcd.ie:         {ftd: [Joerg],                           cab: DUB, ia3: IRL}
  ufl.edu:        {ftd: [Brinkley, Robb],         sab: FL, cab: GNV, ia3: USA}
  unige.it:       {ftd: [Iuricich],                        cab: GOA, ia3: ITA}
  umaine.edu:     {ftd: [Razi],                   sab: ME, cab: BDL, ia3: USA}
  umass.edu:      {ftd: [Sorber],                 sab: MA, cab: BGR, ia3: USA}
  unc.edu:        {ftd: [Smotherman],             sab: NC, cab: RDU, ia3: USA}
  charlotte.edu:  {ftd: [Babu],                   sab: NC, cab: CLT, ia3: USA}
  pitt.edu:       {ftd: [Van Scoy],               sab: PA, cab: PIT, ia3: USA}
  utdallas.edu:   {ftd: [Luo],                    sab: TX, cab: DFW, ia3: USA}
  virginia.edu:   {ftd: [Hedetniemi],             sab: VA, cab: CHO, ia3: USA}
  uu.nl:          {ftd: [Karamouzas],                      cab: UTC, ia3: NLD}
  vanderbilt.edu: {ftd: [Apon],                   sab: TN, cab: BNA, ia3: USA}
  vatech.edu:     {ftd: [Cheng, Ge],              sab: VA, cab: ROA, ia3: USA}
  washington.edu: {ftd: [Jin],                    sab: WA, cab: SEA, ia3: USA}

### end ###
