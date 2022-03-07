pipeline {

    agent any
    
    environment {
        BRANCH_NAME = "${GIT_BRANCH}"
        SLACK_URL = "${SLACK_URL}"
    }
    stages {

        stage('Delete Folders & Check Version') {
            steps {        
                sh "echo 'Deleting folders...'"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh "echo 'Installing dependencies...'"
                sh "echo 'This is the slack_url ${SLACK_URL}'"
                sh "python3 --version"
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

        stage('Deploy') {
            steps {
                sh "echo 'Deploying app...'"            
            }
        }
    }
}
