--1
SELECT * FROM player p inner join hall_of_fame f  on p.player_id=f.player_id where inducted='Y' ;
SELECT  count(*) FROM player p inner join hall_of_fame f  on p.player_id=f.player_id where inducted='Y' ;

--2
SELECT c.* FROM player p 
	inner join hall_of_fame f  on p.player_id=f.player_id 
	inner join player_college c  on p.player_id=c.player_id 
	where inducted='Y' ;

	
--3

select subquery1.college_id,count(*) from (
	SELECT DISTINCT c.college_id, p.player_id FROM player p 
		inner join hall_of_fame f  on p.player_id=f.player_id 
		inner join player_college c  on p.player_id=c.player_id 
		where inducted='Y' order by  c.college_id
) subquery1 group by subquery1.college_id order by count(*) desc;


