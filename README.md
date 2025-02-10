# **Conveyor System Simulation with Distributed ICS**

This project simulates an **Industrial Control System (ICS)** for a **conveyor system**, integrating multiple distributed components such as **Raft Consensus**, **Kafka Message Broker**, **LLM Agents (Future Integration)**, and a **Resource Manager** using Kubernetes.

## **Project Overview**

The system consists of the following components:

- **Client**: Simulates the conveyor belt and sends sensor data to the **ICS Simulator**.
- **Server**: The ICS Simulator processes the sensor data and interacts with other components.
- **Kafka Message Broker**: Handles communication between system components.
- **Raft Consensus Service**: Implements leader election and distributed consensus.
- **Resource Manager (K8s Scheduler)**: Manages resource allocation for workloads.
- **XR Client** (Optional): Connects external systems such as AR/VR clients.
- **LLM Agents (Future Work)**: Will provide optimization based on AI-driven decision-making.

## **Architecture Diagram**

```mermaid
graph TD
  A["LLM Agents (Future Integration)"] -->|gRPC/Protobuf| B["ICS Simulator (gRPC Server)"]
  B -->|gRPC/Protobuf| C["Message Broker (Kafka)"]
  C -->|gRPC| D["Consensus Service (Raft + Clocks)"]
  B -->|gRPC/Protobuf| E["XR Client"]
  C -->|gRPC| F["Resource Manager (K8s Scheduler)"]

  classDef service fill:#ADD8E6,stroke:#005A9C,stroke-width:2px,color:#000,font-weight:bold;
  classDef broker fill:#FFD700,stroke:#DAA520,stroke-width:2px,color:#000,font-weight:bold;
  classDef consensus fill:#98FB98,stroke:#228B22,stroke-width:2px,color:#000,font-weight:bold;
  classDef client fill:#FFB6C1,stroke:#FF69B4,stroke-width:2px,color:#000,font-weight:bold;
  
  class A,B,F service;
  class C broker;
  class D consensus;
  class E client;



# 1. Configure Docker to use Minikube’s environment
minikube docker-env | Invoke-Expression

# 2. Build the server Docker image
docker build -t server:latest -f server/Dockerfile server

# 3. Build the client Docker image
docker build -t client:latest -f client/Dockerfile client

# 4. Delete existing Kubernetes resources (if applicable)
kubectl delete -f kubernetes/

# 5. Apply Kubernetes configurations
kubectl apply -f kubernetes/

# 6. Verify running pods
kubectl get pods

# 7. Check logs of a specific pod (replace <pod-name>)
kubectl logs <pod-name>

# 8. Get Kubernetes service details
kubectl get svc

# 9. Delete all running pods (useful for debugging)
kubectl delete pods --all

# 10. Get details of a specific pod (replace <pod-name>)
kubectl describe pod <pod-name>



