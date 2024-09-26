from kafka import KafkaProducer
# Configura el productor Kafka
producer = KafkaProducer (bootstrap_servers='localhost:29092')
# Envía un mensaje al tópico 'test-topic'
producer.send('test-topic', key=b'key', value=b'value')
# Asegúrate de que todos los mensajes sean enviados 
producer.flush()
# Cierra el productor
producer.close()