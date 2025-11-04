# Bachelor's thesis
[Real-time patient data collection and analysis using the Apache Kafka platform](https://www.theseus.fi/handle/10024/881694)

## Built using
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![InfluxDB](https://img.shields.io/badge/InfluxDB-22ADF6?style=for-the-badge&logo=InfluxDB&logoColor=white)
![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)
  
## Abstract
Apache Kafka is a platform designed for processing large volumes of data and data streams. This thesis examined the architecture of Apache Kafka, the principles of event streaming platforms, and the benefits and challenges of realtime analytics in modern society. Additionally, the aim was to develop a prototype that enables real-time collection and analysis of patient data using the Apache Kafka platform. 

The prototype was implemented by simulating patient data with the Python programming language, sending the data to Apache Kafka, and storing it in an InfluxDB database. The visualization of patient data was carried out using the Grafana visualization tool, enabling real-time analysis. The system’s performance and scalability were evaluated by simulating patient data at different frequencies. 

The results demonstrated that Apache Kafka can efficiently process large amounts of data, and a similar system could be utilized in healthcare. Future development should consider, for example, GDPR-compliant security requirements to enable the adoption of the prototype in healthcare applications. 

## Prototype
In this thesis I developed a prototype using **Apache Kafka** for real-time patient data collection and analysis. The prototype operates as follows:
1. ``producer.py`` simulates patient data every 5 seconds and sends it to Apache Kafka.
2. Apache Kafka receives the data and stores it to ``potilastieto-events`` topic.
3. ``consumer.py`` reads the data from the topic and sends it to InfluxDB database as a Point-object.
4. InfluxDB is integrated with Grafana allowing the data to be seamlessly visualized on a real-time dashboard.
![prototype flowchart](https://github.com/user-attachments/assets/5b3d5efe-a8c0-425a-8de2-e603bf96d192)

