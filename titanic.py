import streamlit as st
import joblib as jl

st.title("Titanic Prediction")
model = jl.load('mymodel.pkl')


