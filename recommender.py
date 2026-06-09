import pandas as pd # type: ignore

funds = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

mapping = {
    "Low":"Low",
    "Moderate":"Moderate",
    "High":"High"
}

result = (
    funds[
        funds["risk_grade"] ==
        mapping[risk]
    ]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print(
    result[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)