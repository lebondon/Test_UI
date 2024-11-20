import streamlit as st
import joblib
import numpy as np

pipe = joblib.load('titanic_pipe.pkl')

#Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#  'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#   dtype='object'

st.title("Titanic Prediction")
st.header("inserisci dei possibili valori")

class_ship=st.selectbox(
    "In which class are you on the ship?",
    ("1", "2", "3"),
)

sex=st.selectbox(
    "what's your sex?",
    ("M", "F"),
)

age=st.number_input("insert your age",min_value=1,max_value=120)

sib_flag=st.selectbox(
    "do you have a spouse or sibling onboard with you?",
    ("Yes", "No"),
)

sib=st.number_input("if yes how many?",min_value=1,max_value=10,key=1)

parch_flag=st.selectbox(
    "do you have parents or childrens onboard with you?",
    ("Yes", "No"),
)

parch=st.number_input("if yes how many?",min_value=1,max_value=10,key=2)

fare=st.number_input("How much did you pay for a ticket?",min_value=1,max_value=100000)

embarked=st.selectbox(
    "Where did you embark from?",
    ("Southampton", "Cherbourg", "Queenstown"),
)

if sib_flag=='No':
    sib=0

if parch_flag=='No':
    parch=0

if embarked=='Southampton':
    embarked='S'
if embarked=='Cherbourg':
    embarked='C'
if embarked=='Queenstown':
    embarked='Q'

values=[class_ship,sex,age,sib,parch,fare,embarked]

print(pipe.predict([class_ship,sex,age,sib,parch,fare,embarked]))





















