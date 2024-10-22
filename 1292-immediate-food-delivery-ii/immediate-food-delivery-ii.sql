WITH cte1 AS (
    SELECT 
        delivery_id,
        customer_id,
        order_date,
        customer_pref_delivery_date,
        CASE 
            WHEN order_date = customer_pref_delivery_date THEN 'immediate' 
            ELSE 'scheduled' 
        END AS delivery,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date asc) as rn
    FROM Delivery
)
SELECT 
    ROUND((SUM(CASE WHEN delivery = 'immediate' AND rn = 1 THEN 1 ELSE 0 END) / 
           SUM(CASE WHEN rn = 1 THEN 1 ELSE 0 END)) * 100, 2) AS immediate_percentage
FROM cte1;
