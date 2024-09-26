from kafka.admin import KafkaAdminClient, NewTopic
# Cliente administrador
admin_client = KafkaAdminClient (bootstrap_servers="localhost:29092", client_id='test_client')
# Crear un nuevo tema
topic = NewTopic (name="new-topic", num_partitions=1, replication_factor=1)
admin_client.create_topics([topic])
print("Tema creado con éxito")