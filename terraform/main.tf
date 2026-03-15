terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
    }
  }
}

provider "docker" {}

resource "docker_image" "telecom" {
  name = "telecom-service:latest"
  build {
    path = ".."
  }
}

resource "docker_container" "telecom_container" {
  name  = "telecom-container"
  image = docker_image.telecom.latest
  ports {
    internal = 5000
    external = 5001
  }
}