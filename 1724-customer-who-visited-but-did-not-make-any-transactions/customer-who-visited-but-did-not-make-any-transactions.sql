# Write your MySQL query statement below
select customer_id, count(*) as count_no_trans 
from Visits v left join Transactions t on v.visit_id = t.visit_id
where transaction_id is null
group by customer_id


/*
1,yara
2,rana
3,yara

123,1,50
*/