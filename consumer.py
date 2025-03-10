from kafka import KafkaConsumer
from influxdb_client_3 import InfluxDBClient3, Point
import json


def deserialize_message(message):
    return json.loads(message.decode("utf-8"))


token = "zxS8u7r59b5_Xt8hANEwtya0Q-Vv2QallPaHctXh-cH7Kb7V30SsVyX36xJut2iS-oMTcA_9m--91qCIOtJZQQ=="
org = "Opinnäytetyö"
host = "https://eu-central-1-1.aws.cloud2.influxdata.com"
client = InfluxDBClient3(host=host, token=token, org=org)
database = "kafka-potilastiedot"

consumer = KafkaConsumer(
    "potilastiedot-events",
    bootstrap_servers="localhost:9092",
    value_deserializer=deserialize_message,
)

print("Kuunnellaan Kafka-aiheitta...")

try:
    for message in consumer:
        data = message.value
        print("Vastaanotettu data:", data)

        point = (
            Point("potilastiedot")
            .tag("potilas_id", data["potilas_id"])
            .tag("laite_id", data["laite_id"])
            .field("syke", data["syke"])
            .field("kehon_lampotila", data["kehon_lampotila"])
            .field("happisaturaatio", data["happisaturaatio"])
            .field("aikaleima", data["aikaleima"])
        )
        client.write(database=database, record=point)
        print("Tiedot kirjoitettu InfluxDB tietokantaan.")

except KeyboardInterrupt:
    print("Kafka-lukija keskeytetty")

finally:
    consumer.close()
    print("Kafka-kuluttaja suljettu")
