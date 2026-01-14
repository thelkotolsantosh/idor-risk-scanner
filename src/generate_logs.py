import pandas as pd
import random
from faker import Faker

fake = Faker()
rows = []

for _ in range(1500):
    user_id = random.randint(1, 50)
    object_id = random.randint(1, 200)

    rows.append({
        "user_id": user_id,
        "endpoint": "/api/v1/orders/" + str(object_id),
        "object_id": object_id,
        "accessed_by": user_id if random.random() > 0.1 else random.randint(1, 50),
        "status": random.choice([200, 200, 200, 403]),
    })

pd.DataFrame(rows).to_csv("data/api_access_logs.csv", index=False)
