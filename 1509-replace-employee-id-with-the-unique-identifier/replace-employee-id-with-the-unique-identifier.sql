/* Write your T-SQL query statement below */
select b.unique_id, a.name from Employees a
left join EmployeeUNI b
on a.id = b.id     