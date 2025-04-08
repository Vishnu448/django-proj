pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.10'
        VENV_DIR = "${WORKSPACE}/venv"
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub repository
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                sh '''
                    # Create and activate virtual environment
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    
                    # Install dependencies
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    
                    # Install Chrome browser and chromedriver
                    sudo apt-get update
                    sudo apt-get install -y google-chrome-stable
                '''
            }
        }
        
        stage('Start Django Server') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    
                    # Run migrations (if needed)
                    cd django_app
                    python manage.py migrate
                    
                    # Start Django server in background
                    python manage.py runserver 0.0.0.0:8000 &
                    echo $! > django_server.pid
                    
                    # Give it a moment to start up
                    sleep 5
                '''
            }
        }
        
        stage('Run Selenium Tests') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    
                    # Run the tests
                    pytest selenium_tests/test_login.py -v --html=test-reports/report.html
                '''
            }
            post {
                always {
                    // Archive the test videos
                    archiveArtifacts artifacts: 'test_videos/*.mp4', allowEmptyArchive: true
                    
                    // Archive the test reports
                    archiveArtifacts artifacts: 'test-reports/*.html', allowEmptyArchive: true
                    
                    // Kill the Django server
                    sh 'if [ -f django_app/django_server.pid ]; then kill $(cat django_app/django_server.pid); rm django_app/django_server.pid; fi'
                }
            }
        }
    }
    
    post {
        always {
            // Clean workspace
            cleanWs()
        }
    }
}