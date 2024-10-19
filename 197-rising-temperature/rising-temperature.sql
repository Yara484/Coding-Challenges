# Write your MySQL query statement below
# Inner join
select a.id as Id
from Weather a join Weather b on datediff(a.recordDate,b.recordDate) = 1
where a.temperature > b.temperature   