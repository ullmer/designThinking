-- Basic tables for representing faculty and research areas ###
-- Brygg Ullmer, Clemson University
-- Begun 2021-09-19

create table faculty(
  id        integer primary key, 
  name      text,
  firstName text,
  lastName  text, 
  division  text,
  rank      text,
  extraRole text
);

create table researchArea(
  id   integer primary key,
  name text
);

create table facultyRanks(
  id   integer primary key,
  name text
);

create table facultyDivisions(
  id   integer primary key,
  name text
);

create table researchAreaRelation(
  id       integer primary key,
  parentId integer, -- parent/major research area
  childId  integer  -- child/research subarea
);

create table personResearchRelation(
  id   integer primary key,
  raid integer, -- research area ID
  fid  integer  -- faculty ID
);
  
--- end ---
