# Write your MySQL query statement below
with cte1 as 
(
    select distinct product_id from Products
),

cte2 as 
(
select distinct product_id, 
FIRST_VALUE(new_price) OVER (PARTITION BY product_id ORDER BY change_date DESC) AS price
from Products 
where change_date <= '2019-08-16'
)

select c1.product_id, 
case when price is null then 10 else c2.price end as price
from cte1 c1 left join cte2 c2 on c1.product_id = c2.product_id
