📝 Todo App – Flask + Docker + Kubernetes + GitHub Actions

A complete CI/CD pipeline project that deploys a Python Flask Todo application using:

🐍 Flask (backend framework)

✅ Pytest (testing)

📦 Docker (containerization)

☸️ Kubernetes (orchestration)

🤖 GitHub Actions (CI/CD pipeline)

📂 Project Structure
flask-dep/
│── app.py              # Main Flask app
│── models.py           # Database models
│── routes.py           # App routes
│── requirements.txt    # Python dependencies
│── test_app.py         # Pytest test cases
│── Dockerfile          # Docker image build instructions
│── .dockerignore       # Excludes files from Docker build
│── .gitignore          # Excludes files from GitHub
│── pytest.ini          # Pytest configuration
│── k8s/                # Kubernetes manifests
│   ├── namespace.yaml
│   ├── pvc.yaml
│   ├── deployment.yaml
│   └── service.yaml
│── .github/workflows/
│   └── ci.yaml         # GitHub Actions pipeline

🚀 How It Works
1. Flask App

A simple Todo app with add, delete, and update functionality.

Uses SQLite (todo.db) for persistence.

2. Testing with Pytest

Run locally:

pytest -v


Expected output:

test_app.py::test_home PASSED
test_app.py::test_add_todo PASSED
test_app.py::test_delete_todo PASSED

3. Docker

Build and run container:

docker build -t todo-app:latest .
docker run -p 5000:5000 todo-app


👉 App available at: http://localhost:5000

Push to Docker Hub:

docker tag todo-app:latest <your-docker-username>/todo-app:latest
docker push <your-docker-username>/todo-app:latest

4. Kubernetes

Apply manifests:

kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/pvc.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml


Check resources:

kubectl get all -n todo-app


Access app:

Via NodePort → http://localhost:30050

Or via port-forwarding →

kubectl port-forward svc/todo-app-service -n todo-app 5000:5000

5. GitHub Actions (CI/CD)

The pipeline (.github/workflows/ci.yaml) automates:

1️⃣ Test → Runs pytest on each push.
2️⃣ Build & Push → Creates Docker image and pushes to DockerHub.
3️⃣ Deploy → Applies Kubernetes manifests.

📊 Workflow Visualization:

graph TD;
    A[Push Code] --> B[GitHub Actions]
    B --> C[Run Pytest ✅]
    C --> D[Build & Push Docker 🐳]
    D --> E[Deploy to Kubernetes ☸️]
    E --> F[App Running 🎉]

⚙️ Tech Stack

Backend: Python, Flask

Database: SQLite (persisted via PVC in K8s)

Testing: Pytest

Containerization: Docker

Orchestration: Kubernetes (with PVC storage)

CI/CD: GitHub Actions

🛠️ Commands Quick Reference
# Run tests
pytest -v  

# Docker build & run
docker build -t todo-app .
docker run -p 5000:5000 todo-app  

# Kubernetes
kubectl apply -f k8s/
kubectl get pods -n todo-app
kubectl port-forward svc/todo-app-service -n todo-app 5000:5000

📸 Screenshots

(Add app screenshots, GitHub Actions success screenshot, and Kubernetes output here for client clarity)

✅ Summary

This project shows how a Flask web app can be:

Tested automatically with pytest,

Packaged into a Docker container,

Deployed with Kubernetes,

Fully automated via GitHub Actions CI/CD pipeline.