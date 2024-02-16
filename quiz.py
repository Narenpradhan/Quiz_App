import streamlit as st

def quiz_app():
    st.title("Quiz App")

    # Define your quiz questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["Elephant", "Whale", "Giraffe", "Horse"],
            "correct_answer": "Whale"
        },
        {
            "question": "What is the powerhouse of the cell?",
            "options": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic reticulum"],
            "correct_answer": "Mitochondria"
        }
    ]

    # Initialize score
    score = 0

    # Display each question and get user's answer
    for i, q in enumerate(questions):
        st.subheader(f"Question {i + 1}: {q['question']}")
        user_answer = st.radio("Select an answer:", q["options"], index=None)
        if user_answer == q["correct_answer"]:
            score += 1

    # Display final score
    st.write(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_app()