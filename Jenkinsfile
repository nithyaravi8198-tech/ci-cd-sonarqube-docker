pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "nithyaravi8/ci-cd-sonarqube-docker"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Code already checked out by Jenkins"
            }
        }

        stage('Build & Test') {
    steps {
        sh '''
        pip3 install --break-system-packages -r requirements.txt
        python3 -m unittest test_app.py
        '''
    }
}

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
/opt/sonar-scanner/bin/sonar-scanner \
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
        sh '''
        docker rm -f app-container || true
        docker run -d --name app-container -p 5000:5000 $DOCKER_IMAGE
        '''
    }
}
    }
}
