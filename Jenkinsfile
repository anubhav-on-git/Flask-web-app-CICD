pipeline {
    agent any

    stages {
        // jenkins already does checkout automatically when using pipeline from SCM
        // stage('Clone Repo') {
        //     steps {
        //         git 'https://github.com/anubhav-on-git/Flask-web-app-CICD.git'
        //     }
        // }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Stop Old Containers') {
            steps {
                sh 'docker-compose down'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }

    }
}