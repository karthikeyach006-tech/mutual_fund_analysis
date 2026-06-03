-- 1
SELECT * FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2
SELECT strftime('%Y-%m', date),
AVG(nav)
FROM fact_nav
GROUP BY 1;

-- 3
SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 4
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5
SELECT category,
COUNT(*)
FROM dim_fund
GROUP BY category;

-- 6
SELECT risk_category,
COUNT(*)
FROM dim_fund
GROUP BY risk_category;

-- 7
SELECT fund_house,
COUNT(*)
FROM dim_fund
GROUP BY fund_house;

-- 8
SELECT transaction_type,
SUM(amount_inr)
FROM fact_transactions
GROUP BY transaction_type;

-- 9
SELECT AVG(return_3yr_pct)
FROM fact_performance;

-- 10
SELECT AVG(expense_ratio_pct)
FROM fact_performance;