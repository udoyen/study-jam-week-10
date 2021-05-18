## Final Solution to Creating a GKE Cluster and Deploying Workload to GKE and Exposing it Using an Ingress Object

Steps:

1. Create gke cluster

   gcloud deployment-manager deployment create <name_of_deployment> --config cluster.yaml

2. Deploy workload and expose it:


   gcloud deployment-manager deployment create deployment --config deployment.yaml