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
            when {branch pattern: "(dev|prod|PR-.*)", comparator: "REGEXP"}
            steps {
                sh "echo 'Checking tools...'"
                sh "docker --version"
                sh "helm version"
            }
        }

        stage('Installing Dependencies & Testing') {
            when {branch pattern: "(dev|prod|PR-.*)", comparator: "REGEXP"}
            steps{
                script {
                    sh "python3 -m venv venv"
                    sh "source ./venv/bin/activate"
                    sh "pip install -r requirements.txt"
                    sh "coverage run -m pytest"
                    sh "coverage xml"
                    sh "deactivate"
                }
            }
        }


        stage('SonarQube Analysis') {
            when {branch pattern: "(dev|prod|PR-.*)", comparator: "REGEXP"}
            steps{
                script {
                    withSonarQubeEnv('SonarCloud') {
                        sh "${scannerHome}/bin/sonar-scanner -X"
                    }
                }
            }
        }

        stage('Building Project') {
            when {branch pattern: "(dev|PR-.*)", comparator: "REGEXP"}
            steps {
                sh "echo 'Installing dependencies...'"
                sh "docker build -t ${USER}/${PROJECT_NAME}:${GIT_COMMIT} -t ${USER}/${PROJECT_NAME}:latest ."
                sh "echo $DOCKER_HUB_PSW | docker login -u $DOCKER_HUB_USR --password-stdin"
                sh "docker push ${USER}/${PROJECT_NAME}:${GIT_COMMIT}"
                sh "docker push ${USER}/${PROJECT_NAME}:latest"
            }
        }
        stage('Deploying Application') {
            when {branch pattern: "(prod)", comparator: "REGEXP"}
            steps {
                sh "source ./scripts/deploy_image.sh"
            }
        }

    }
}
