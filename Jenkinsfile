pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                // REPLACE username with your GitHub username.
                // 'branch: main' matters: the git step defaults to master.
                git branch: 'main', url: 'https://github.com/vu2f2425026-design/Student-Devops-Project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // venv avoids the "externally-managed-environment" pip error on newer Ubuntu
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t student-app:${BUILD_NUMBER} -t student-app:latest .'
            }
        }

        // Optional (assignment item 2): push to Docker Hub.
        // Needs a Jenkins "Username with password" credential with ID dockerhub-creds.
        // stage('Push to Docker Hub') {
        //     steps {
        //         withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
        //                 usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
        //             sh '''
        //                 echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin
        //                 docker tag student-app:latest $DH_USER/student-app:latest
        //                 docker push $DH_USER/student-app:latest
        //             '''
        //         }
        //     }
        // }

        stage('Deploy Container') {
            steps {
                sh 'docker stop student-container || true'
                sh 'docker rm student-container || true'
                sh 'docker run -d -p 5000:5000 --name student-container student-app:latest'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    sleep 5
                    curl -f http://localhost:5000/health
                '''
            }
        }
    }

    post {
        success { echo 'Pipeline status: SUCCESS' }
        failure { echo 'Pipeline status: FAILED - check the stage logs above' }
    }
}
