import streamlit as st
import joblib
import numpy as np

def main():
    pipe = joblib.load('titanic_pipe.pkl')

    st.title("Titanic Prediction")
    st.header("Insert possible values")

    class_ship = st.selectbox(
        "In which class are you on the ship?",
        ("1", "2", "3"),
    )

    sex = st.selectbox(
        "What's your sex?",
        ("M", "F"),
    )

    age = st.number_input("Insert your age", min_value=1, max_value=120)

    sib_flag = st.selectbox(
        "Do you have a spouse or sibling onboard with you?",
        ("Yes", "No"),
    )

    sib = st.number_input("If yes, how many?", min_value=1, max_value=10, key=1) if sib_flag == "Yes" else 0

    parch_flag = st.selectbox(
        "Do you have parents or children onboard with you?",
        ("Yes", "No"),
    )

    parch = st.number_input("If yes, how many?", min_value=1, max_value=10, key=2) if parch_flag == "Yes" else 0

    fare = st.number_input("How much did you pay for a ticket?", min_value=1, max_value=100000)

    embarked = st.selectbox(
        "Where did you embark from?",
        ("Southampton", "Cherbourg", "Queenstown"),
    )

    embarked_code = {'Southampton': 'S', 'Cherbourg': 'C', 'Queenstown': 'Q'}[embarked]

    values = np.array([class_ship, sex, age, sib, parch, fare, embarked_code]).reshape(1, -1)

    if st.button("Predict Survival"):
        
        prediction = pipe.predict(values)[0]
        
        if prediction == 1:
            st.success("Congratulations! You would survive the Titanic voyage!")
        else:
            st.error("Unfortunately, you would not survive the Titanic voyage.")

if __name__=='__main__':
    main()