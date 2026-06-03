# Data Dictionary

## fund_master

| Column        | Type    | Description             |
| ------------- | ------- | ----------------------- |
| amfi_code     | Integer | Unique AMFI scheme code |
| fund_house    | Text    | Mutual fund company     |
| scheme_name   | Text    | Name of scheme          |
| category      | Text    | Fund category           |
| sub_category  | Text    | Detailed category       |
| risk_category | Text    | Risk classification     |

## nav_history

| Column    | Type    | Description     |
| --------- | ------- | --------------- |
| amfi_code | Integer | Scheme code     |
| date      | Date    | NAV date        |
| nav       | Float   | Net Asset Value |

## investor_transactions

| Column           | Type  | Description            |
| ---------------- | ----- | ---------------------- |
| investor_id      | Text  | Unique investor        |
| transaction_date | Date  | Transaction date       |
| transaction_type | Text  | SIP/Lumpsum/Redemption |
| amount_inr       | Float | Transaction amount     |

## scheme_performance

| Column            | Type  | Description   |
| ----------------- | ----- | ------------- |
| return_1yr_pct    | Float | 1-year return |
| return_3yr_pct    | Float | 3-year return |
| return_5yr_pct    | Float | 5-year return |
| expense_ratio_pct | Float | Expense ratio |
