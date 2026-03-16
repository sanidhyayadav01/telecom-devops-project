terraform {
  required_providers {
    kubernetes = {
      source = "hashicorp/kubernetes"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_deployment_v1" "telecom" {
  metadata {
    name = "telecom-deployment"
    labels = {
      app = "telecom"
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "telecom"
      }
    }

    template {
      metadata {
        labels = {
          app = "telecom"
        }
      }

      spec {
        container {
          name  = "telecom-container"
          image = "telecom-service"
          
          port {
            container_port = 5000
          }
        }
      }
    }
  }
}

resource "kubernetes_service_v1" "telecom_service" {
  metadata {
    name = "telecom-service"
  }

  spec {
    selector = {
      app = "telecom"
    }

    port {
      port        = 80
      target_port = 5000
      node_port   = 30007
    }

    type = "NodePort"
  }
}