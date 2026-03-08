pipeline {
    agent any

      environment {
        DOCKER_IMAGE = "ragh1808/scientific-calculator:${BUILD_NUMBER}"
    }

    stages {

        stage('Clone Source Code') {
            steps {
                git branch: 'main', url: 'https://github.com/raghavtejas1808/Scientific-Calculator-Python.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'            }
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
                withDockerRegistry([credentialsId: 'dockerhub', url: '']) {
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