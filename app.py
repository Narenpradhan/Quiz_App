import streamlit as st

def quiz_app():
    st.markdown("<h1 style='text-align: center;'>IEEE Induction Quiz</h1>", unsafe_allow_html=True)
    st.markdown("---")

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

def page_1():
    st.markdown("<h1 style='text-align: center;'>Fill Up Your Details</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("")
    st.write("")
    name = st.text_input("Enter Your Full Name", placeholder="Hritesh Roshan Mahapatra")
    st.write("")
    roll = st.text_input("Enter Your Registration Number", placeholder="1234567890")
    st.write("")
    email = st.text_input("Enter Your Email", placeholder="example@email.com")
    st.write("")
    branch = st.radio("Select Your Branch", ["Computer Science and Engineering", "Chemical Engineering", "Civil Engineering", "Electrical Engineering", "Electrical and Electronics Engineering", "Electronics and Telecommunication Engineering", "Information Technology", "Mechanical Engineering", "Metallurgical and Materials Engineering", "Production Engineering"],index=None)
    st.write("")
    return name, roll, email, branch

if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = 1

    if st.session_state.page == 1:
        name, roll, email, branch = page_1()
        submitted = st.button("Next")
        if submitted:
            if not name:
                st.write("Please enter your name.")
            elif not roll:
                st.write("Please enter your registration number.")
            elif not email:
                st.write("Please enter your e-mail.")
            elif not branch:
                st.write("Please select your branch.")
            else:
                st.session_state.page = 2

    elif st.session_state.page == 2:
        quiz_app()
        st.write("")
        if st.button("Previous"):
            st.session_state.page = 1
