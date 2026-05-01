import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Titanic Survival Prediction", layout="wide")

# ---------------- BACKGROUND IMAGE WITH DARK OVERLAY ----------------
page_bg_img = """
<style>
.stApp {
    background-image: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
    url("https://media-cldnry.s-nbcnews.com/image/upload/t_social_share_1024x768_scale,f_auto,q_auto:best/rockcms/2023-05/230517-titanic-3d-mb-1259-76694d.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# ---------------- FORCE WHITE TEXT ----------------
white_text_css = """
<style>

/* General text */
html, body, [class*="css"] {
    color: white !important;
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
    color: white !important;
}

/* Labels */
label {
    color: white !important;
}

/* Sidebar */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Buttons */
.stButton button {
    color: white !important;
    background-color: rgba(255,255,255,0.1);
    border: 1px solid white;
}

/* Input fields */
input, textarea {
    color: white !important;
    background-color: rgba(0,0,0,0.4) !important;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    color: white !important;
    background-color: rgba(0,0,0,0.4) !important;
}

</style>
"""
st.markdown(white_text_css, unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("best_titanic_model.pkl", "rb"))

# ---------------- TITLE ----------------
st.title("Titanic Survival Prediction 🚢")

# ---------------- INPUTS ----------------
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", 1, 100, 25)
fare = st.number_input("Fare", 0.0, 500.0, 50.0)
embarked = st.selectbox("Embarked", ["S", "C", "Q"])
sibsp = st.number_input("Siblings/Spouses", 0, 10, 0)
parch = st.number_input("Parents/Children", 0, 10, 0)

title = st.selectbox("Title", ["Mr", "Miss", "Mrs", "Other"])

family_size = sibsp + parch + 1
is_alone = 1 if family_size == 1 else 0

# ---------------- PREPROCESS ----------------
sex = 0 if sex == "male" else 1

title_map = {"Mr": 0, "Miss": 1, "Mrs": 2, "Other": 3}
title = title_map[title]

embarked_map = {"S": 0, "C": 1, "Q": 2}
embarked = embarked_map[embarked]

# ---------------- DATAFRAME ----------------
input_data = pd.DataFrame({
    'Pclass': [pclass],
    'Sex': [sex],
    'Age': [age],
    'Fare': [fare],
    'Embarked': [embarked],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Title': [title],
    'FamilySize': [family_size],
    'IsAlone': [is_alone]
})

# ---------------- PREDICTION ----------------
if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Survived")
    else:
        st.error("❌ Did Not Survive")