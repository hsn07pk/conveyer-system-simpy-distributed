import grpc
from concurrent import futures
import time
import conveyor_pb2
import conveyor_pb2_grpc
from conveyor import ConveyorBelt

class ConveyorService(conveyor_pb2_grpc.ConveyorServiceServicer):
    def __init__(self):
        self.conveyor = ConveyorBelt()

    def GetOptimizedSettings(self, request, context):
        """Handle incoming sensor data and return optimized settings."""
        print(f"Received sensor data: {request}")

        # Apply optimization logic to the received data (simulate here)
        optimized_settings = self.optimize_system(request)

        # Apply optimized settings to the conveyor system
        self.conveyor.speed = optimized_settings['new_speed']
        self.conveyor.voltage = optimized_settings['new_voltage']
        print(f"Optimized settings applied: {optimized_settings}")

        # Return the optimized settings to the client
        return conveyor_pb2.OptimizedSettings(
            new_speed=optimized_settings['new_speed'],
            new_voltage=optimized_settings['new_voltage'],
            new_pid_kp=optimized_settings['new_pid_kp'],
            new_pid_ki=optimized_settings['new_pid_ki'],
            new_pid_kd=optimized_settings['new_pid_kd']
        )

    def optimize_system(self, sensor_data):
        """Simulate optimization logic and return new settings."""
        # Example optimization strategy
        new_speed = sensor_data.speed * 1.05  # Increase speed by 5%
        new_voltage = sensor_data.voltage * 0.95  # Decrease voltage by 5%
        new_pid_kp = 1.2  # Optimized Kp
        new_pid_ki = 0.6  # Optimized Ki
        new_pid_kd = 0.15  # Optimized Kd

        return {
            "new_speed": new_speed,
            "new_voltage": new_voltage,
            "new_pid_kp": new_pid_kp,
            "new_pid_ki": new_pid_ki,
            "new_pid_kd": new_pid_kd
        }

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    conveyor_pb2_grpc.add_ConveyorServiceServicer_to_server(ConveyorService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
