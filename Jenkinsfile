pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        ansiColor('xterm')
    }

    triggers {
        githubPush()
    }

    environment {
        IMAGE_NAME = "ragh1808/scientific-calculator:${BUILD_NUMBER}"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo "Cloning project from GitHub..."
                git branch: 'main', url: 'https://github.com/raghavtejas1808/Scientific-Calculator-Python.git'
            }
        }

        stage('Build Application') {
            steps {
                echo "Preparing application build..."
                sh 'echo Build completed'
            }
        }

        stage('Run Tests') {
            agent {
                docker {
                    image 'python:3.9'
                }
            }
            steps {
                echo "Installing dependencies..."
                sh 'pip install -r requirements.txt'

                echo "Running test cases..."
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker image to DockerHub..."

                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "Checking Docker connection..."
                    docker info

                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                echo "Deploying application using Ansible..."
                sh 'ansible-playbook deploy.yml'
            }
        }
    }
}