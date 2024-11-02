# Write your MySQL query statement below
with order_turn as
(
select person_id, person_name, weight,
sum(weight) over (order by turn) as total,
 turn 
from Queue 
order by turn asc
),

filtered as 
(
select * from order_turn
where total <= 1000 
order by turn desc
)

select person_name from filtered limit 1



