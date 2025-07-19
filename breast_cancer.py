import pandas as pd
import streamlit as st
import joblib
import numpy as np


def breast_cancer():
    model = joblib.load("breast_cancer_model.pkl")
    feature_names = [
        'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
        'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean',
        'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se',
        'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se',
        'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst',
        'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst',
        'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst'
    ]

    st.set_page_config(page_title="Breast Cancer Classifier", layout='centered')
    st.title("🩺 Breast Cancer Prediction App")
    st.write("Enter the patient's data to predict whether the tumor is **Benign (B)** or **Malignant (M)**.")

    with st.form("input_form"):
        cols = st.columns(3)
        user_input = []
        for i, feature in enumerate(feature_names):
            value = cols[i % 3].number_input(f"{feature}", step=0.01)
            user_input.append(value)

        submitted = st.form_submit_button("Predict")
    
    if submitted:
        input_df = pd.DataFrame([user_input], columns=feature_names)
        prediction = model.predict(input_df)[0]
        probabilty = model.predict_proba(input_df)[0]

        confidence = round(np.max(probabilty) * 100, 2)
        predicted_label = "Malignant" if prediction == 'M' else 'Benign'

        st.subheader("Prediction Result")
        st.write(f"**Prediction:** {predicted_label}")
        st.write(f"**Confidence:** {confidence} %")

        if prediction == 'M':
            st.error("🔴 The tumor is likely **Malignant**.")
        else:
            st.success("🟢 The tumor is likely **Benign**.")
    
    st.markdown("---")
    st.markdown(
        "<center><small>🧡 Coded with love by <strong>Lukman Olamide</strong></small></center>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    breast_cancer()