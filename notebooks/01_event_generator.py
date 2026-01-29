import json, time, random
from datetime import datetime

while True:
    event = {
        "user_id": random.randint(1, 100),
        "event_type": random.choice(["click", "view", "purchase"]),
        "event_time": datetime.now().isoformat()
    }
    print(json.dumps(event))
    time.sleep(2)
