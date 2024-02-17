import streamlit as st
import re
from data import questions_list
from pymongo import MongoClient



# client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
# db = client["mydatabase"]  # Replace "mydatabase" with your database name
# collection = db["userdetails"]  # Replace "userdetails" with your collection name



def quiz_app():
    st.markdown("<h1 style='text-align: center;'>IEEE Induction Quiz</h1>", unsafe_allow_html=True)
    st.markdown("---")

    questions = questions_list

    score = 0

    for i, q in enumerate(questions):
        st.subheader(f"Question {i + 1}: {q['question']}")
        user_answer = st.radio("Select an answer:", q["options"], index=None)
        if user_answer == q["correct_answer"]:
            score += 1
    return score




def home():
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




if 'final_points' not in st.session_state:
    st.session_state.final_points = 0




if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = 1

    if st.session_state.page == 1:
        name, roll, email, branch = home()
        # st.session_state.name = name
        # st.session_state.roll = roll
        # st.session_state.email = email
        # st.session_state.branch = branch
        submitted = st.button("Next")
        if submitted:
            if not name :
                st.write("Please enter your name.")
            elif not name.isalpha():
                st.write("Name should not contain any characters.")
            elif not roll:
                st.write("Please enter your registration number.")
            elif not roll.isdigit():
                st.write("Registration Number should not contain any other characters.")
            elif not (len(roll)>=10 and len(roll)<13):
                st.write("Enter a valid registration number.")
            elif not email:
                st.write("Please enter your e-mail.")
            elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
                st.write("E-mail address is not valid.")
            elif not branch:
                st.write("Please select your branch.")
            else:
                st.session_state.page = 2


    elif st.session_state.page == 2:
        st.session_state.final_points = quiz_app()
        st.write("")
        if st.button("Previous"):
            st.session_state.page = 1
        elif st.button("Submit"):
            # name = st.session_state.name
            # roll = st.session_state.roll
            # email = st.session_state.email
            # branch = st.session_state.branch

            # user_data = {
            #     "Name": name,
            #     "Roll_No": roll,
            #     "Email": email,
            #     "Branch": branch
            # }
            # collection.insert_one(user_data)
            # st.write("Quiz Submitted Successfully!")
            st.session_state.page = 3
    
    
    elif st.session_state.page == 3:
        st.balloons()
        st.markdown("""
            <style>
                .centered {
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 70vh; /* 100% of the viewport height */
                }
            </style>
        """, unsafe_allow_html=True)
        html_text = f"<div class='centered'><div><h1>Congratulations!!👏</h1><h1 class='centered-text'><b>You scored {st.session_state.final_points} out of 30</b></h1></div></div>"
        st.markdown(html_text, unsafe_allow_html=True)
