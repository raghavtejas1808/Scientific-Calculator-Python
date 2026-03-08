pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ragh1808/scientific-calculator"
    }

    stages {

        stage('Clone Source Code') {
            steps {
                git 'https://github.com/raghavtejas1808/scientific-calculator-devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Application') {
            steps {
                echo "Build step completed"
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-credentials', url: '']) {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Deploy using Ansible') {
            steps {
                sh 'ansible-playbook deploy.yml'
            }
        }
    }
}