import streamlit as st
import joblib
import pandas as pd
from utils import location_list, make_list, model_list, year_list

def load_trained_data():
    pipeline = joblib.load("car_price_model.pkl")

    st.title("Jiji Car Price Prediction App")

    condition = st.selectbox("Condition", ['New', 'Local used', 'Foreign used'])
    transmission = st.selectbox("Transmission", ['Automatic', 'Manual'])
    make = st.selectbox("Make", make_list) 
    model_name = st.selectbox("Model", model_list)
    year = st.selectbox("Year", year_list)
    location = st.selectbox("Location", location_list) 


    if st.button("Predict Price"):
        input_data = pd.DataFrame([{
            'condition': condition,
            'transmission': transmission,
            'make': make,
            'model': model_name,
            'year': year,
            'location': location
        }])

        # input_data = encode_input(input_data)

        # prediction = pipeline.predict(input_data)[0]

        # st.success(f"Estimated Car Price: ₦{int(prediction):,.2f}")
        try:
            predicted_price = pipeline.predict(input_data)[0]
            st.success(f"💰 Estimated Car Price: ₦{int(predicted_price):,}")
            st.write("Raw prediction output:", predicted_price)
            st.dataframe(input_data)
        except Exception as e:
            st.error(f"Prediction failed: {e}")
    
    st.markdown("---")
    st.caption("Powered by Ola-Dev")

if __name__ == "__main__":
    load_trained_data()
