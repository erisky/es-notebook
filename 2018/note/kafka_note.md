## Kafka Note

Steps memo and notes for trying kafa.

## Reference projects

* [The Kafka quick start](https://kafka.apache.org/quickstart)
* [Kafka C library](https://kafka.apache.org/quickstart)
* Kafka python - tbd

> Local repo:  ~/git/kafka/kafka_2.11-1.1.0

## Quick Start 

**Install and Run**
```
tar -xzf kafka_2.11-1.1.0.tgz
cd kafka_2.11-1.1.0
bin/zookeeper-server-start.sh config/zookeeper.properties
```
In another terminal
```
bin/kafka-server-start.sh config/server.properties
```
follow the quickstart if necessary

## Concept of Kafka
* A streaming platform 
    * Publish and Subscribe 
    * Store streams of records in a fault-tolerant durable way. *fault-tolerance*
    * Process streams of records as they occur - *realtime*
* Run as a cluster
* Topic based 
* record ==> (key,value,timestamp)

* 4 APIS:
    * Producer API
    * Consumer API
    * Streames API (forwarding concept: in and out)
    * Connector API (connects Kafka topic to existe applications)



## Start with lib
> local: ~/git/kafka
```
git clone https://github.com/edenhill/librdkafka.git
```
