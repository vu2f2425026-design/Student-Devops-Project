pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/vu2f2425026-design/Student-Devops-Project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-app:%BUILD_NUMBER% -t student-app:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                // returnStatus keeps the build alive when no old container exists yet
                bat(script: 'docker stop student-container', returnStatus: true)
                bat(script: 'docker rm student-container', returnStatus: true)
                bat 'docker run -d -p 5000:5000 --name student-container student-app:latest'
            }
        }

        stage('Verify Deployment') {
            steps {
                sleep 5
                bat 'curl -f http://localhost:5000/health'
            }
        }
    }

    post {
        success { echo 'Pipeline status: SUCCESS' }
        failure { echo 'Pipeline status: FAILED - check the stage logs above' }
    }
}
