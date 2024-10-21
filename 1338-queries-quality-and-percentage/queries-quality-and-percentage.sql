select query_name, round(avg(cast(rating as decimal)/position), 2) as quality,
ROUND(SUM(CASE WHEN rating < 3 then 1 else 0 end) * 100 / COUNT(*) ,2) as poor_query_percentage
from Queries
group by query_name
having query_name is not null