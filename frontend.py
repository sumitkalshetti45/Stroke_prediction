import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("rfmodel.pkl", "rb") as file:
    model = pickle.load(file)

# Page setup
st.set_page_config(page_title="Stroke Risk Predictor", page_icon="🧠", layout="wide")

# Title
st.title("🧠 Stroke Risk Prediction App")
st.markdown("Provide patient details below to estimate the risk of **stroke**.")

# Using expanders to group inputs
with st.expander("👤 Personal Information", expanded=True):
    gender = st.radio("Gender", ["Male", "Female", "Other"])
    gender_map = {"Male": 0, "Female": 1, "Other": 2}

    age = st.slider("Age (Years)", 0, 100, 30)

    ever_married = st.radio("Ever Married", ["No", "Yes"])
    ever_married_map = {"No": 0, "Yes": 1}

with st.expander("❤️ Health Conditions", expanded=True):
    hypertension = st.radio("Hypertension (High BP)", ["No", "Yes"])
    hypertension_map = {"No": 0, "Yes": 1}

    heart_disease = st.radio("Heart Disease", ["No", "Yes"])
    heart_disease_map = {"No": 0, "Yes": 1}

with st.expander("🏠 Lifestyle & Work", expanded=True):
    work_type = st.selectbox(
        "Work Type", ["Children", "Govt_job", "Never_worked", "Private", "Self-employed"]
    )
    work_type_map = {"Children": 0, "Govt_job": 1, "Never_worked": 2, "Private": 3, "Self-employed": 4}

    residence_type = st.radio("Residence Type", ["Rural", "Urban"])
    residence_map = {"Rural": 0, "Urban": 1}

    smoking_status = st.selectbox(
        "Smoking Status", ["Never smoked", "Formerly smoked", "Smokes", "Unknown"]
    )
    smoking_status_map = {"Never smoked": 0, "Formerly smoked": 1, "Smokes": 2, "Unknown": 3}

with st.expander("🧪 Measurements", expanded=True):
    avg_glucose_level = st.number_input("Average Glucose Level (mg/dL)", min_value=40.0, max_value=300.0, step=0.1)
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, step=0.1)

# Predict button
if st.button("🔍 Predict Stroke Risk"):
    input_data = np.array([
        gender_map[gender],
        age,
        hypertension_map[hypertension],
        heart_disease_map[heart_disease],
        ever_married_map[ever_married],
        work_type_map[work_type],
        residence_map[residence_type],
        avg_glucose_level,
        bmi,
        smoking_status_map[smoking_status]
    ]).reshape(1, -1)

    prediction = model.predict(input_data)[0]

    st.markdown("---")
    st.subheader("📊 Prediction Result")
    if prediction == 1:
        st.error("⚠️ High Risk of Stroke! 🚑 Consult a doctor immediately.")
    else:
        st.success("✅ Low Risk of Stroke 💪 Keep maintaining a healthy lifestyle.")
