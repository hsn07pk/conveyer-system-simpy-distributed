```mermaid
graph TD;
    %% Main ICS Simulation Environment Components
    ICS_Simulator["ICS Simulator (gRPC Server)"] <--> Message_Broker["Message Broker (RabbitMQ)"]
    Message_Broker <--> LLM_Agents["LLM Agents (Future Integration)"]

    %% Additional Services and Their Connections
    ICS_Simulator <--> XR_Service["XR Service (WebSocket)"]
    Message_Broker <--> Consensus_Service["Consensus Service (Raft Algorithm)"]

    %% Resource and Cluster Management
    XR_Service <--> Resource_Manager["Resource Manager (Scheduler)"]
    Consensus_Service <--> Kubernetes_Cluster["Kubernetes Cluster (Auto-scaling)"]

    %% Grouping Components for Better Visualization
    subgraph ICS_Environment["ICS Simulation Environment"]
        ICS_Simulator
        Message_Broker
        LLM_Agents
        XR_Service
        Consensus_Service
        Resource_Manager
        Kubernetes_Cluster
    end
