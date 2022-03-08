pipeline {

    agent any
    
    environment {
        GIT_COMMIT = "${GIT_COMMIT}"
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
                // sh "python3 --version"
                // sh "echo '${GIT_COMMIT}'"
                sh "docker --version"
            }
        }

        stage('SonarQube Analysis') {
            steps{
                script {
                    withSonarQubeEnv('SonarCloud') {
                        sh "${scannerHome}/bin/sonar-scanner -X"
                    }
                }
            }
        }

        stage('Building Project') {
            steps {
                sh "echo 'Installing dependencies...'"
                sh "docker build -t ${USER}/${PROJECT_NAME}:${GIT_COMMIT} -t ${USER}/${PROJECT_NAME}:latest ."
                sh "echo $DOCKER_HUB_PSW | docker login -u $DOCKER_HUB_USR --password-stdin"
                sh "docker push ${USER}/${PROJECT_NAME}:${GIT_COMMIT}"
                sh "docker push ${USER}/${PROJECT_NAME}:latest"
                sh "source ./scripts/deploy_image.sh"
            }
        }

        // stage('Test') {
        //     steps {
        //         sh "echo 'Testing...'"
        //     }
        // }

        // stage('Build') {
        //     steps {
        //         sh "echo 'Building app...'"            
        //     }
        // }
    }
}
