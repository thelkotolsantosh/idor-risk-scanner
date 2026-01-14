import pandas as pd

df = pd.read_csv("data/api_access_logs.csv")

# Sequential access detection
df = df.sort_values(["accessed_by", "object_id"])
df["delta"] = df.groupby("accessed_by")["object_id"].diff()

suspicious = df[df["delta"] == 1]
print("Potential ID enumeration detected:")
print(suspicious.head())
