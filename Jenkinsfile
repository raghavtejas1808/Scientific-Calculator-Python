pipeline {
    agent any

    options {
        ansiColor('xterm')
    }

    triggers {
        githubPush()
    }

    environment {
        IMAGE_NAME = "ragh1808/scientific-calculator:${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Build Application') {
            steps {
                echo "Build stage..."
                sh 'echo Build completed'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                docker run --rm \
                -v $PWD:/app \
                -w /app \
                python:3.9 \
                sh -c "PYTHONPATH=/app pip install -r requirements.txt && PYTHONPATH=/app pytest"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t ragh1808/scientific-calculator:latest .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker image..."

                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker push ragh1808/scientific-calculator:latest
                    '''
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                echo "Deploying application..."
                sh 'ansible-playbook deploy.yml'
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully 🚀"
        }

        failure {
            echo "Pipeline failed ❌"
        }
    }
}