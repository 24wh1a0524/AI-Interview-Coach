# 🤖 AI Interview Coach

An AI-powered web application that helps students and job seekers practice interviews, answer questions using voice, receive automated feedback, and track their interview performance.

The project also demonstrates a complete **DevOps CI/CD workflow** using GitHub, Jenkins, Docker, and Docker Compose.

---

## 📌 Project Overview

**AI Interview Coach** is designed to provide an interactive interview practice environment.

Users can:

* Upload their resume
* Generate interview questions
* Answer questions using voice
* Submit answers for evaluation
* Receive scores and feedback
* Track their overall interview performance through a dashboard

The application is containerized using Docker and deployed using Jenkins CI/CD.

---

## 🎯 Objectives

* Help students prepare for technical and HR interviews.
* Provide an easy platform for interview practice.
* Evaluate answers automatically.
* Provide feedback to improve answer quality.
* Track interview performance.
* Demonstrate DevOps practices such as continuous integration and deployment.

---

## ✨ Features

### 📄 Resume Upload

Users can upload their resume through the web interface.

### 🎯 Interview Question Generation

The application generates interview questions for practice.

### 🎤 Voice Answer

Users can answer interview questions using voice input through the browser.

### 📝 Answer Evaluation

Answers are evaluated based on factors such as answer length and relevance.

### 📊 Performance Dashboard

The dashboard displays:

* Number of questions answered
* Individual question scores
* Average score
* Overall performance percentage
* Feedback for each answer

### 🚀 CI/CD Pipeline

The project uses Jenkins to automate:

1. Source code checkout
2. Backend Docker image building
3. Frontend Docker image building
4. Application deployment
5. Deployment verification

---

## 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │     GitHub      │
                    │  Source Code    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Jenkins     │
                    │    CI / CD      │
                    └────────┬────────┘
                             │
                 ┌───────────┴───────────┐
                 │                       │
                 ▼                       ▼
        ┌─────────────────┐     ┌─────────────────┐
        │ Backend Docker  │     │ Frontend Docker │
        │    Container    │     │    Container    │
        │    FastAPI      │     │ React + Nginx   │
        │    Port 8000    │     │    Port 3000    │
        └────────┬────────┘     └────────┬────────┘
                 │                       │
                 └───────────┬───────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ AI Interview    │
                    │     Coach       │
                    └─────────────────┘
```

---

## 🛠️ Technologies Used

### Frontend

* React
* Vite
* JavaScript
* HTML
* CSS

### Backend

* Python
* FastAPI
* Uvicorn

### Database

* PostgreSQL *(planned/extendable)*

### AI / Speech

* AI-based interview question generation
* Browser Speech Recognition
* Whisper / OpenAI / Gemini can be integrated for advanced AI features

### DevOps

* Git
* GitHub
* Docker
* Docker Compose
* Jenkins
* Nginx
* GitHub Actions *(extendable)*
* Prometheus & Grafana *(extendable)*

---

## 📂 Project Structure

```text
AI-Interview-Coach/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── ...
│   ├── package.json
│   ├── Dockerfile
│   └── ...
│
├── Dockerfile.jenkins
├── docker-compose.yml
├── Jenkinsfile
├── .gitignore
└── README.md
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/24wh1a0524/AI-Interview-Coach.git
```

### 2. Navigate to the project

```bash
cd AI-Interview-Coach
```

---

## ▶️ Run Backend

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn main:app --reload
```

Backend will be available at:

```text
http://localhost:8000
```

FastAPI documentation:

```text
http://localhost:8000/docs
```

---

## ▶️ Run Frontend

Open another terminal and navigate to:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend will normally be available at:

```text
http://localhost:5173
```

---

# 🐳 Run Using Docker

The project can also be run using Docker Compose.

From the project root:

```bash
docker-compose up -d --build
```

Check running containers:

```bash
docker ps
```

The application will be available at:

### Frontend

```text
http://localhost:3000
```

### Backend

```text
http://localhost:8000
```

### FastAPI Swagger Documentation

```text
http://localhost:8000/docs
```

To stop the application:

```bash
docker-compose down
```

---

# 🔄 Jenkins CI/CD Pipeline

Jenkins is used to automate the build and deployment process.

The pipeline performs the following stages:

```text
Checkout
   ↓
Build Backend Docker Image
   ↓
Build Frontend Docker Image
   ↓
Deploy Application
   ↓
Verify Deployment
```

### Jenkins Pipeline Stages

#### 1. Checkout

Jenkins retrieves the latest source code from GitHub.

#### 2. Build Backend Docker Image

```bash
docker build -t ai-interview-backend ./backend
```

#### 3. Build Frontend Docker Image

```bash
docker build -t ai-interview-frontend ./frontend
```

#### 4. Deploy Application

Docker Compose starts the backend and frontend containers.

#### 5. Verify Deployment

Jenkins checks the running Docker containers using:

```bash
docker ps
```

---

## 🔐 Environment Variables

Sensitive information such as API keys should **never be committed to GitHub**.

Use a `.env` file for secrets.

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

The `.env` file should remain in `.gitignore`.

---

## 🔒 Security

The project follows basic security practices:

* API keys are kept outside GitHub.
* `.env` files are ignored using `.gitignore`.
* Docker containers are used to isolate application services.
* CORS is configured for the frontend application.

**Never upload real API keys or passwords to GitHub.**

---

## 📊 Application Workflow

```text
User
 │
 ▼
Open AI Interview Coach
 │
 ▼
Upload Resume
 │
 ▼
Generate Interview Questions
 │
 ▼
Answer Interview Question
 │
 ├── Text Answer
 │
 └── Voice Answer
 │
 ▼
Submit Answer
 │
 ▼
Answer Evaluation
 │
 ▼
Score + Feedback
 │
 ▼
Performance Dashboard
```

---

## 🚀 DevOps Workflow

```text
Developer
    │
    ▼
Write / Update Code
    │
    ▼
Git
    │
    ▼
GitHub
    │
    ▼
Jenkins
    │
    ├── Checkout
    │
    ├── Build Docker Images
    │
    ├── Deploy with Docker Compose
    │
    └── Verify Containers
    │
    ▼
Running Application
```

---

## 📈 Future Enhancements

The following features can be added in future versions:

* PostgreSQL database integration
* Resume parsing and personalized questions
* Advanced AI-based answer evaluation
* OpenAI/Gemini integration
* Whisper-based speech-to-text
* User authentication and login
* Interview history
* Personalized performance analytics
* Prometheus monitoring
* Grafana dashboards
* GitHub Actions integration
* Kubernetes deployment
* Cloud deployment using AWS/Azure

---

## 🎓 Academic Relevance

This project combines **Artificial Intelligence and DevOps** to create an automated interview preparation platform.

It demonstrates practical knowledge of:

* Web application development
* REST APIs
* React frontend development
* FastAPI backend development
* Docker containerization
* Docker Compose
* Git and GitHub
* Jenkins CI/CD
* Automated deployment

---

## 👥 Project Type

**Project:** AI Interview Coach

**Domain:** Artificial Intelligence + Web Development + DevOps

**Application Type:** Web Application

**Deployment:** Docker + Docker Compose + Jenkins

---

## 📜 License

This project is created for educational and academic purposes.

```

This version is suitable for your **GitHub repository, college project documentation, demo, and viva**. It also clearly separates features you have implemented from technologies/features that are planned for future enhancement.
```
