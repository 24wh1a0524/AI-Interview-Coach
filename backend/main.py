from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware


# Create FastAPI application
app = FastAPI()


# Allow React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Home
@app.get("/")
def home():
    return {
        "message": "AI Interview Coach Backend Running"
    }


# Upload Resume
@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename
    }


# Sample Interview Questions
@app.get("/questions")
def questions():
    return {
        "questions": [
            "Tell me about yourself.",
            "Explain your main project.",
            "What are your technical skills?",
            "What are your strengths?",
            "Why should we hire you?"
        ]
    }


# Generate Interview Questions
@app.get("/generate-questions")
def generate_questions():

    questions = [
        "Tell me about yourself.",
        "Explain your main project.",
        "What technologies have you worked with?",
        "What are your strengths and weaknesses?",
        "Why should we hire you?"
    ]

    return {
        "questions": questions
    }


# Evaluate Answer
@app.post("/evaluate-answer")
def evaluate_answer(question: str, answer: str):

    question = question.strip()
    answer = answer.strip()

    if len(answer) == 0:
        return {
            "score": 0,
            "feedback": "Please provide an answer."
        }

    words = answer.split()
    word_count = len(words)

    # Basic score based on answer length
    if word_count < 10:
        score = 3
    elif word_count < 25:
        score = 5
    elif word_count < 50:
        score = 7
    elif word_count < 80:
        score = 8
    else:
        score = 9

    # Check whether the answer contains words related
    # to the question
    question_words = set(question.lower().split())
    answer_words = set(answer.lower().split())

    common_words = question_words.intersection(answer_words)

    # Ignore very common words
    ignored_words = {
        "the", "is", "are", "a", "an", "and",
        "to", "of", "your", "you", "what",
        "why", "how", "tell", "me", "about"
    }

    useful_common_words = common_words - ignored_words

    if len(useful_common_words) >= 2 and score < 10:
        score += 1

    if score > 10:
        score = 10

    # Feedback
    if score <= 3:
        feedback = "Your answer is too short. Explain your answer with more details."

    elif score <= 5:
        feedback = "Your answer is a good start. Add more details and examples."

    elif score <= 7:
        feedback = "Good answer. Try connecting your answer more clearly to the question."

    elif score <= 9:
        feedback = "Very good answer. You provided useful details related to the question."

    else:
        feedback = "Excellent answer. Your response is detailed and relevant."

    return {
        "question": question,
        "answer": answer,
        "score": score,
        "feedback": feedback,
        "word_count": word_count
    }

