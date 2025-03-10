import time
import json
import random
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")

if producer.bootstrap_connected() == True:
    print("Yhdistetty Kafkaan onnistuneesti")


def generoi_data():
    return {
        "potilas_1": {
            "potilas_id": 1,
            "laite_id": 1,
            "syke": random.randint(50, 100),
            "kehon_lampotila": round(random.uniform(36.0, 37.5), 2),
            "happisaturaatio": round(random.uniform(90.0, 100.0), 2),
            "aikaleima": time.time(),
        },
        "potilas_2": {
            "potilas_id": 2,
            "laite_id": 2,
            "syke": random.randint(65, 120),
            "kehon_lampotila": round(random.uniform(37.2, 38.5), 2),
            "happisaturaatio": round(random.uniform(75.0, 89), 2),
            "aikaleima": time.time(),
        },
    }


try:
    while True:
        data = generoi_data()
        for potilas, info in data.items():
            producer.send(
                topic="potilastiedot-events",
                value=json.dumps(info).encode("utf-8"),
            )
            print(f"Lähetetään {potilas}: {info}")
        time.sleep(5)

except KeyboardInterrupt:
    print("Keskeytetty käyttäjän toimesta")

finally:
    producer.flush()
    producer.close()
    print("Kafka-tuottaja suljettu")
