pipeline {

    agent any
    
    environment {
        BRANCH_NAME = "${GIT_BRANCH}"
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
