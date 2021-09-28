insert into facultyDivisions(name) 
  values ('CS'),('HCC'),('VC'),('FOI');

insert into facultyRanks(order, abbrev, name) values
  (1, 'asst',  'Asst. Prof.'),
  (2, 'assoc', 'Assoc. Prof.'),
  (3, 'full',  'Professor'),
  (4, 'lecturer', 'Lecturer'),

create table facultyRanks(
  id   integer primary key,
  abbrev text,
  name   text,
  order  int
);


