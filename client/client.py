# File: client/client.py  
import grpc  
from kafka import KafkaProducer  
import json  
import time  
import conveyor_pb2  
import conveyor_pb2_grpc  
from conveyor import ConveyorBelt  

# Kafka setup  
producer = KafkaProducer(  
    bootstrap_servers='kafka:9092',  
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  
)  

def send_to_kafka(data):  
    producer.send('sensor_topic', data)  

def run():  
    conveyor = ConveyorBelt()  
    channel = grpc.insecure_channel('server-service:50051')  
    stub = conveyor_pb2_grpc.ConveyorServiceStub(channel)  

    while True:  
        sensor_data = conveyor.generate_data()  
        sensor_data['lamport_time'] = time.time_ns()  # For Component 4  
        send_to_kafka(sensor_data)  

        # Existing gRPC logic  
        request = conveyor_pb2.SensorData(**sensor_data)  
        response = stub.GetOptimizedSettings(request)  
        print(f"Optimized: {response}")  
        time.sleep(1)  

if __name__ == '__main__':  
    run()  