pipeline {
    agent any

    stages {

        stage('Move to project directory and Build and run the application') {
            steps {
                dir('D:\\Anubhav\\Projects\\Devops_Project_1\\DevOps-Project-Two-Tier-Flask-App') {
                    // Your build steps here
                    bat 'docker build -t flask-app .'
                    bat 'docker-compose down'
                    bat 'docker-compose up --build -d'
                }
            }
        }

    }
}