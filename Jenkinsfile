pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "nithyaravi8/ci-cd-sonarqube-docker"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/nithyaravi8198-tech/ci-cd-sonarqube-docker.git'
            }
        }

        stage('Build & Test') {
            steps {
                sh 'python -m unittest test_app.py'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=ci-cd-sonarqube-docker \
                    -Dsonar.sources=.
                    '''
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                    docker login -u $USER -p $PASS
                    docker push $DOCKER_IMAGE
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker run -d -p 5000:5000 $DOCKER_IMAGE'
            }
        }
    }
}