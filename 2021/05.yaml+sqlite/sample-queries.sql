-- Sample queries for representing and research areas ###
-- Brygg Ullmer, Clemson University
-- Begun 2021-09-20

-- find all full professors
select name from faculty where rank='full';   

-- find all asst professors in CS
select name from faculty where rank='asst' and division='CS';

-- find all major research categories

select ra.name from researchArea as ra, researchAreaRelation as rar
  where rar.parentID = 0 and ra.id = rar.childID;

-- find all faculty investigating AI-related research fields

select f.name, f.division, f.rank 
   from faculty as f, researchArea as ra, personResearchRelation as prr
   where ra.name = 'Artificial Intelligence' and prr.id = ra.id and prr.id = f.id
   group by f.name order by f.rank, f.division;

-- find all faculty investigating HCC-related research fields

select f.name, f.division, f.rank 
   from faculty as f, researchArea as ra, personResearchRelation as prr
   where ra.name = 'Human-Centered Computing' and prr.id = ra.id and prr.fid = f.fid
   group by f.name order by f.division, f.lastName;

--- end ---
