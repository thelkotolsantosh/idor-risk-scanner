import pandas as pd

df = pd.read_csv("data/api_access_logs.csv")

df["idor_risk"] = (
    (df["user_id"] != df["accessed_by"]).astype(int) +
    (df["status"] == 200).astype(int)
)

high_risk = df[df["idor_risk"] >= 2]
print("High-risk IDOR access patterns:")
print(high_risk.head())
