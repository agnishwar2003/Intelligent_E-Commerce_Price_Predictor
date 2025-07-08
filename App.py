import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load(r"D:\Placement Material\Practice\price_predictor_model.pkl")  # Make sure you have saved this

# Streamlit App UI
st.set_page_config(page_title="Product Price Predictor", layout="centered")
st.title("🛒 Product Price Predictor")
st.markdown("Predict the price of electronics based on category, brand, and product details.")

# --- User Input ---
category = st.selectbox("Category", ["Smartphones", "Laptops", "TVs", "Fridges", "ACs", "Washing Machines"])
brand = st.text_input("Brand", placeholder="e.g., Samsung, HP, LG")
product = st.text_area("Product Description", placeholder="e.g., Samsung Galaxy A15 5G (6GB RAM, 128GB, Black)")

# --- Prediction ---
if st.button("Predict Price"):
    if not brand or not product:
        st.warning("Please fill in both brand and product fields.")
    else:
        # Prepare input
        input_df = pd.DataFrame([{
            'Category': category,
            'Brand': brand,
            'Product': product
        }])
        # Predict
        predicted_price = model.predict(input_df)[0]
        st.success(f"💰 Predicted Price: ₹{predicted_price:,.2f}")
