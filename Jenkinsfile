pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/sanidhyayadav01/telecom-devops-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t telecom-service .'
            }
        }

        stage('Tag Image') {
            steps {
                bat 'docker tag telecom-service sanidhyaydv/telecom-service'
            }
        }

        stage('Push Image') {
            steps {
                bat 'docker push sanidhyaydv/telecom-service'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f kubernetes/deployment.yaml'
                bat 'kubectl apply -f kubernetes/service.yaml'
            }
        }

    }
}