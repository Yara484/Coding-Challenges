WITH cte1 AS (
    SELECT query_name, COUNT(*) AS alls
    FROM Queries
    GROUP BY query_name
),

cte2 AS (
    SELECT query_name, COUNT(query_name) AS part
    FROM Queries
    WHERE rating < 3
    GROUP BY query_name
),

cte3 AS (
    SELECT t1.query_name, ROUND((part / alls) * 100, 2) AS poor_query_percentage
    FROM cte1 t1 
    left JOIN cte2 t2 ON t1.query_name = t2.query_name
),

cte4 AS (
    SELECT query_name, ROUND(AVG(rating / position), 2) AS quality
    FROM Queries
    GROUP BY query_name
)

SELECT cte4.query_name, quality, COALESCE(poor_query_percentage,0) AS poor_query_percentage 
FROM cte4 
left JOIN cte3 ON cte3.query_name = cte4.query_name
WHERE cte4.query_name IS NOT NULL
