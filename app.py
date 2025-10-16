# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 22:04:06 2025

@author: Benjamin
"""
import numpy as np
import pickle
import pandas as pd
import streamlit as st
import os

# Load the trained model
loaded_model = pickle.load(open('house_sales_data.sav', 'rb'))

def house_price_prediction(bedrooms, bathrooms, floors,
                            condition, yr_built, city, country,):
                            
     
    # Create DataFrame from input
    new_house = pd.DataFrame([{
        'bedrooms': 3.0,
        'bathrooms': 1.5,
        'floors': 1.5,
        'condition': 3,
        'yr_built': 1955,
        'city': 36,
        'country': 0
    }])
    
    # Predict price
    predicted_price = loaded_model.predict(new_house)
    
    # Return the prediction
    return predicted_price[0]
# Main Streamlit app
def main():
    st.title("house Price Prediction")

    # Input fields for all features
    bedrooms = st.text_input('bedrooms (numeric code, e.g., 3.0)')
    bathrooms = st.text_input('bathrooms (e.g., 1.5)')
    floors = st.text_input('floors) (e.g., 1.50)')
    condition = st.text_input('condition (e.g., 3)')
    yr_built = st.text_input('yr_built (numeric code, e.g., 1955)')
    city = st.text_input('city (e.g., 36)')
    country = st.text_input('country (e.g., 0)')
    

    if st.button('Predict house Price'):
        try:
        # Convert inputs to numeric types
         bedrooms = int(bedrooms)
         bathrooms = int(bathrooms)
         floors = float(floors)
         condition = int(condition)
         yr_built = int(yr_built)
         city = int(city)
         country = float(country)
        

        # Call the prediction function (just fix indentation)
         price = house_price_prediction(
            bedrooms, bathrooms, floors,
            condition, yr_built, city, country,
        )

         st.success(f'The predicted price for the house is: RWF {price:.2f}')
        except ValueError:
            
         st.error("Please enter valid numeric values for all inputs.")
if __name__ == '__main__':

    main()         


