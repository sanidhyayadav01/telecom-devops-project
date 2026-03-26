# 🚀 Telecom DevOps Project – CI/CD Pipeline with Docker, Kubernetes & Terraform

## 📌 Project Overview

This project demonstrates a **complete DevOps pipeline** for deploying a telecom messaging API using modern DevOps tools.

The application is containerized using Docker, deployed to Kubernetes, and automated through a Jenkins CI/CD pipeline. Infrastructure provisioning is handled using Terraform.

The goal of this project is to showcase how code moves from **development to production using automation, containerization, and Infrastructure as Code (IaC).**

---

# 🏗 Architecture

Developer → GitHub → Jenkins CI/CD Pipeline → Docker Build → Docker Hub → Terraform → Kubernetes Deployment

### 🛠 DevOps Tools Used

* GitHub – Source code management
* Jenkins – CI/CD pipeline automation
* Docker – Containerization
* Docker Hub – Container registry
* Kubernetes – Container orchestration
* Terraform – Infrastructure as Code

---

# 📂 Project Structure

```
telecom-devops-project
│
├── app/
│   ├── app.py
│   └── requirements.txt
│
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
│
├── terraform/
│   └── main.tf
│
├── Jenkinsfile
├── Dockerfile
```

---

# 📡 Application Description

The application is a simple **Flask-based Telecom Messaging API** that exposes a health-check endpoint.

Endpoint:

```
GET /status
```

Response:

```json
{
  "service": "Telecom Messaging API",
  "status": "running"
}
```

---

# ⚙ CI/CD Pipeline Flow

1️⃣ Developer pushes code to GitHub
2️⃣ Jenkins pipeline automatically triggers
3️⃣ Jenkins builds a Docker image
4️⃣ Docker image is pushed to Docker Hub
5️⃣ Terraform provisions Kubernetes infrastructure
6️⃣ Kubernetes deploys the containerized application

---

# 🖥 Running the Application Locally

### 1️⃣ Clone Repository

```
git clone https://github.com/<your-username>/telecom-devops-project.git
cd telecom-devops-project
```

---

### 2️⃣ Build Docker Image

```
docker build -t telecom-service .
```

---

### 3️⃣ Run Container

```
docker run -p 5000:5000 telecom-service
```

Access the API:

```
http://localhost:5000/status
```

---

# ☸ Kubernetes Deployment

Apply deployment:

```
kubectl apply -f kubernetes/deployment.yaml
```

Apply service:

```
kubectl apply -f kubernetes/service.yaml
```

Access service:

```
http://localhost:30007/status
```

---

# 🧱 Terraform Deployment

Terraform provisions Kubernetes resources automatically.

Initialize Terraform:

```
terraform init
```

Apply infrastructure:

```
terraform apply
```

---

# 🔁 Jenkins CI/CD Pipeline

The Jenkins pipeline performs the following stages:

* Clone repository from GitHub
* Build Docker image
* Tag Docker image
* Push image to Docker Hub
* Deploy infrastructure using Terraform
* Kubernetes runs the container

Pipeline configuration:

```
Jenkinsfile
```

---

# 📚 DevOps Concepts Demonstrated

✔ Continuous Integration (CI)
✔ Continuous Deployment (CD)
✔ Containerization
✔ Container Orchestration
✔ Infrastructure as Code (IaC)
✔ Automated Deployment Pipelines

---

# 🔮 Future Improvements

* Add Kubernetes autoscaling
* Integrate monitoring with Prometheus & Grafana
* Implement Helm charts
* Add automated testing in Jenkins pipeline

---

---

## 📌 Deployment Note

This README demonstrates the project **working locally**.  

The actual project is deployed on **AWS EC2**, using **Kubernetes and Containerd (Docker)**
