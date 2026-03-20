pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t telecom-service:latest .'
            }
        }

        stage('Tag Image') {
            steps {
                bat 'docker tag telecom-service:latest sanidhyaydv/telecom-service:latest'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'e0e74994-088e-472f-b545-e8716b02e279', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat 'docker login -u %USER% -p %PASS%'
                }
            }
        }

        stage('Push Image') {
            steps {
                bat 'docker push sanidhyaydv/telecom-service:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f kubernetes/deployment.yaml --validate=false'
                bat 'kubectl apply -f kubernetes/service.yaml --validate=false'
            }
        }

        stage('Deploy with Terraform') {
            steps {
                dir('terraform') {
                    bat 'terraform init'
                    bat 'terraform apply -auto-approve'
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'kubectl get pods'
                bat 'kubectl get svc'
            }
        }
    }
}