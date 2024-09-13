# Write your MySQL query statement below
SELECT customer_id, COUNT(*) as count_no_trans 
FROM Visits
LEFT JOIN Transactions
ON Visits.visit_id = Transactions.visit_id
WHERE transaction_id IS NULL
GROUP BY 1