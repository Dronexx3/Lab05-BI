from kafka import KafkaConsumer
# Configura el consumidor Kafka
consumer = KafkaConsumer (
'test-topic',
bootstrap_servers='localhost:29092',
group_id='my-group',
auto_offset_reset='earliest'
)
# Imprime los mensajes del tópico
for message in consumer:
    print(f"Key: {message.key}, Value: {message.value}")
# Cierra el consumidor
consumer.close()