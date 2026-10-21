


-- select gender, sum(purchase_amount ) as revenue
-- from shopping_behavior
-- group by gender;


-- SELECT customer_id, purchase_amount
-- FROM shopping_behavior
-- WHERE discount_applied = 'Yes'
-- and purchase_amount > (SELECT AVG(purchase_amount) from shopping_behavior);

-- SELECT item_purchased, ROUND(AVG(review_rating), 2) as average_rating
-- FROM shopping_behavior

-- GROUP BY item_purchased
-- ORDER BY average_rating DESC
-- LIMIT 5;

WITH customer_type AS
(SELECT customer_id, previous_purchases,
CASE WHEN previous_purchases = 1 THEN 'NEW'
     WHEN previous_purchases BETWEEN 1 AND 5 THEN 'returning'
     WHEN previous_purchases > 5 THEN 'Loyal Customer'
     ELSE 'New Customer' END AS customer_category
FROM shopping_behavior
)

SELECT customer_category, COUNT(*) AS customer_count
FROM customer_type
GROUP BY customer_category
ORDER BY customer_count DESC;   