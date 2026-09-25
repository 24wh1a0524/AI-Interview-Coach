pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Backend Docker Image') {
            steps {
                sh 'docker build -t ai-interview-backend ./backend'
            }
        }

        stage('Build Frontend Docker Image') {
            steps {
                sh 'docker build -t ai-interview-frontend ./frontend'
            }
        }

        stage('Verify Docker') {
            steps {
                sh 'docker --version'
                sh 'docker images'
            }
        }
    }
}