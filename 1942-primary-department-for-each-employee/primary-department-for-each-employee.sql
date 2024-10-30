# Write your MySQL query statement below
with cte as 
(
select employee_id, department_id, primary_flag 
from Employee
group by 1
having count(*) = 1
),

cte2 as
(
select employee_id, department_id, primary_flag
from Employee
where primary_flag = 'Y' 
)

select employee_id, department_id from cte 
union 
select employee_id, department_id from cte2