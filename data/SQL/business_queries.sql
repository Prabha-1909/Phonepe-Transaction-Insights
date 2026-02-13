---1. Decoding Transaction Dynamics on PhonePe Scenario
-- State-wise Total Transaction Amount
SELECT 
    state,
    SUM(transaction_amount) AS total_amount,
    SUM(transaction_count) AS total_transactions
FROM transaction_data
GROUP BY state
ORDER BY total_amount DESC;


-- Quarter-wise Transaction Trend
SELECT 
    year,
    quarter,
    SUM(transaction_amount) AS total_amount,
    SUM(transaction_count) AS total_transactions
FROM transaction_data
GROUP BY year, quarter
ORDER BY year, quarter;

--Payment Category Performance
SELECT 
    transaction_type,
    SUM(transaction_amount) AS total_amount,
    SUM(transaction_count) AS total_transactions
FROM transaction_data
GROUP BY transaction_type
ORDER BY total_amount DESC;

---2. Device Dominance and User Engagement Analysis
--Device Brand Popularity
SELECT 
    brand,
    SUM(registered_users) AS total_users,
    SUM(app_opens) AS total_app_opens
FROM map_user
GROUP BY brand
ORDER BY total_users DESC;

--Engagement Rate per Device
SELECT 
    brand,
    SUM(registered_users) AS total_users,
    SUM(app_opens) AS total_opens,
    ROUND(SUM(app_opens)::numeric / NULLIF(SUM(registered_users),0),2) AS engagement_rate
FROM map_user
GROUP BY brand
ORDER BY engagement_rate DESC;

--Underutilized Devices
SELECT 
    brand,
    SUM(registered_users) AS total_users,
    SUM(app_opens) AS total_opens,
    ROUND(SUM(app_opens)::numeric / NULLIF(SUM(registered_users),0),2) AS engagement_rate
FROM map_user
GROUP BY brand
HAVING SUM(registered_users) > 100000
ORDER BY engagement_rate ASC;

--Region-wise Device Preference
SELECT 
    state,
    brand,
    SUM(registered_users) AS total_users
FROM map_user
GROUP BY state, brand
ORDER BY state, total_users DESC;

---4. Transaction Analysis for Market Expansion
-- State-wise Total Transaction Value
SELECT 
    state,
    SUM(transaction_amount) AS total_amount,
    SUM(transaction_count) AS total_transactions
FROM transaction_data
GROUP BY state
ORDER BY total_amount DESC;

-- State-wise Yearly Transaction Growth
SELECT 
    state,
    year,
    SUM(transaction_amount) AS total_amount
FROM transaction_data
GROUP BY state, year
ORDER BY state, year;

---7. Transaction Analysis Across States and Districts Scenario
-- Top 10 States by Transaction Amount
SELECT 
    state,
    SUM(transaction_amount) AS total_amount,
    SUM(transaction_count) AS total_transactions
FROM transaction_data
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;

-- Top 10 Districts by Transaction Amount
SELECT 
    district,
    SUM(transaction_amount) AS total_amount,
    SUM(transaction_count) AS total_transactions
FROM top_transaction
GROUP BY district
ORDER BY total_amount DESC
LIMIT 10;

-- Top 10 Pin Codes by Transaction Amount
SELECT 
    pincode,
    SUM(transaction_amount) AS total_amount,
    SUM(transaction_count) AS total_transactions
FROM top_transaction
GROUP BY pincode
ORDER BY total_amount DESC
LIMIT 10;

---8. User Registration Analysis Scenario
-- Top States by User Registrations (Year & Quarter specific)

SELECT 
    state,
    SUM(registered_users) AS total_users
FROM aggregated_user
WHERE year = 2022 
  AND quarter = 3
GROUP BY state
ORDER BY total_users DESC
LIMIT 10;

-- Top Districts by User Registrations

SELECT 
    district,
    SUM(registered_users) AS total_users
FROM top_user
WHERE year = 2022 
  AND quarter = 3
GROUP BY district
ORDER BY total_users DESC
LIMIT 10;

-- Top Pin Codes by User Registrations

SELECT 
    pincode,
    SUM(registered_users) AS total_users
FROM top_user
WHERE year = 2022 
  AND quarter = 3
GROUP BY pincode
ORDER BY total_users DESC
LIMIT 10;

