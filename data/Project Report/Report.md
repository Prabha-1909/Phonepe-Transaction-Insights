PhonePe Data Analysis

1. Introduction

This project analyzes PhonePe transaction and user data to identify trends across states, districts, device brands, and time periods. The goal is to uncover business insights that can support strategic decision-making and market expansion.

2. Data Sources

The data was structured into aggregated, map-level, and top-ranking tables to support state, district, and pin code level analysis.

The following tables were used:

-aggregated_transaction
-aggregated_user
-aggregated_insurance
-map_transaction
-map_user
-map_insurance
-top_transaction
-top_user
-top_insurance

3. Business Cases Solved

3.1. Decoding Transaction Dynamics on PhonePe
Queries used:

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

CONCLUSION:
-Analyzed transaction growth across states and quarters.
-Identified high-performing and low-performing regions.
-Compared transaction count vs transaction amount.

Key Insight:
Certain states consistently contribute higher transaction values, indicating strong digital payment adoption.

3.2. Device Dominance and User Engagement Analysis Scenario
Queries used:

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

CONCLUSION:

-Analyzed registered users by device brand.
-Compared app opens vs registrations.

Key Insight:
Some device brands have high registrations but low app engagement, indicating potential performance or usability gaps.

3.3. Transaction Analysis for Market Expansion
Queries used:

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

CONCLUSION:
-Identified top and bottom performing states.
-Analyzed year-wise transaction trends.

Key Insight:
High-performing states represent mature markets, while lower-performing regions offer expansion opportunities.

3.4. Transaction Analysis Across States and Districts
Queries used:

- Top 10 States by Transaction Amount
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

CONCLUSION:
-Ranked regions based on transaction volume and value.
-Identified concentrated activity clusters.

Key Insight:
A small number of districts contribute significantly to total transaction value.

3.5. User Registration Analysis
Queries used:

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

CONCLUSION:
-Analyzed top registration regions for specific year & quarter.
-Identified high-growth districts.

Key Insight:
User registrations are concentrated in urban clusters.

4. Visualizations Used

- KPI summary metrics (Total Transactions, Users, Insurance)
- Bar charts for state-wise performance
- Line charts for year-wise transaction trends
- Pie and Donut charts for distribution analysis
- Choropleth maps for state-wise geographical analysis
- Treemap charts for hierarchical ranking
- Top 10 ranking charts for states, districts, and pin codes

5. Business Recommendations

-Expand aggressively in high-growth districts.
-Improve engagement for underutilized device brands.
-Target low-performing states with awareness campaigns.
-Strengthen merchant partnerships in top-performing regions.

6. Conclusion

This analysis provides actionable insights into transaction behavior, user engagement, and regional performance, enabling strategic decision-making for future growth.







