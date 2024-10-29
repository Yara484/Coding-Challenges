# Write your MySQL query statement below
with cte as 
(
select distinct reports_to as ids, count(reports_to) as reports_count, round(avg(age)) as average_age 
from Employees
where reports_to is not null
group by 1
)


select employee_id, name, reports_count, average_age
from Employees e join cte c on c.ids = e.employee_id
order by 1
