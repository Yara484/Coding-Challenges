# Write your MySQL query statement below
with cte as
(
 select managerId, count(id) as num
from Employee 
group by 1
having count(id) >= 5   
)

select e.name
from Employee e join cte c on e.id = c.managerId
