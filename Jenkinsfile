pipeline {
    agent any

    environment {
        IMAGE_NAME = "sanidhyaydv/telecom-service:latest"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t telecom-service:latest .'
            }
        }

        stage('Tag Image') {
            steps {
                bat 'docker tag telecom-service:latest %IMAGE_NAME%'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'e0e74994-088e-472f-b545-e8716b02e279',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    bat 'docker login -u %USER% -p %PASS%'
                }
            }
        }

        stage('Push Image') {
            steps {
                bat 'docker push %IMAGE_NAME%'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    bat 'kubectl apply -f kubernetes/deployment.yaml'
                    bat 'kubectl apply -f kubernetes/service.yaml'
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    bat 'kubectl get pods'
                    bat 'kubectl get svc'
                }
            }
        }
    }

    post {
        success {
            echo '🚀 Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed!'
        }
    }
}