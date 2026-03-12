import streamlit as st
import pandas as pd
from src.predict import *

data = pd.read_csv('data/data.csv')

st.title('House Price Prediction')
bedrooms = st.number_input('Bedrooms')
bathrooms = st.number_input('Bathrooms')
sqft_living = st.number_input('Sqft Living')
sqft_lot = st.number_input('Sqft Lot')
floors = st.number_input('Floors')
condition = st.number_input('Condition', min_value=0, max_value=5)
waterfront = st.number_input('Waterfront', min_value=0, max_value=1)
yr_built = st.number_input('Year of Built')
state_zip = st.selectbox('Zip Code', list(data.statezip))
view = st.number_input('View', min_value=0, max_value=1)

input_data = {
    "sqft_living": sqft_living,
    "sqft_lot": sqft_lot,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "floors": floors,
    "waterfront": waterfront,
    "view": view,
    "condition": condition,
    "yr_built": yr_built,
    "statezip": state_zip,
}

if st.button("Predict"):
    predicted_price = predict(input_data)
    st.write(f"Predicted House Price: ${predicted_price}")
