pipeline {

    agent any
    
    environment {
        BRANCH_NAME = "${GIT_BRANCH}"
        SLACK_URL = "${SLACK_URL}"
        DOCKER_HUB = credentials('dockerhub')
        USER = "${USER}"
        PROJECT_NAME = "${PROJECT_NAME}"
        scannerHome = tool 'SonarCloud'
    }
    stages {

        stage('Checking Tools') {
            steps {
                sh "echo 'Checking tools...'"
                sh "python3 --version"
                // sh "docker --version"
            }
        }

        stage('SonarQube Analysis') {
            steps{
                script {
                    withSonarQubeEnv('sonarqube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('Building Project') {
            steps {
                sh "echo 'Installing dependencies...'"
                sh "docker build -t ${USER}/${PROJECT_NAME}:latest"
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
