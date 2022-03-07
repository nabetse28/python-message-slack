pipeline {

    agent any
    
    environment {
        BRANCH_NAME = "${GIT_BRANCH}"
        SLACK_URL = "${SLACK_URL}"
        DOCKER_HUB = credentials('dockerhub')
        USER = "${USER}"
        PROJECT_NAME = "${PROJECT_NAME}"
    }
    stages {

        stage('Checking Tools') {
            steps {
                sh "echo 'Checking tools...'"
                sh "docker --version"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh "echo 'Installing dependencies...'"
                sh "docker build -t {}/"
            }
        }

        stage('Test') {
            steps {
                sh "echo 'Testing...'"
            }
        }

        stage('Build') {
            steps {
                sh "echo 'Building app...'"            
            }
        }
    }
}
