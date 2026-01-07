pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/subanu03/trigger.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build --no-cache -t trigger-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat '''
                docker rm -f trigger-container 2>nul
                docker run -d -p 5000:5000 --name trigger-container trigger-app
                '''
            }
        }
    }
}
