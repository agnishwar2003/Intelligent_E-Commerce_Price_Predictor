# 🛒 Intelligent E-Commerce Price Predictor

An end-to-end Machine Learning & Data Analytics project that extracts live product data from [Croma.com](https://www.croma.com), performs cleaning and EDA, trains ML models to predict prices, and deploys a real-time Streamlit app for interactive predictions.

---

### 🚀 Project Overview

This project demonstrates how AI and Data Science can assist in e-commerce pricing strategy through:
- 🔎 Data scraping with Selenium
- 📊 Exploratory analysis with Power BI
- 🧠 Machine Learning using Random Forest & Gradient Boosting
- 🌐 Deployment via Streamlit for real-time price prediction

---

### 🛠 Tech Stack

- **Python**
- **Selenium** (Web Scraping)
- **Pandas** (Data Processing)
- **Scikit-learn** (ML Modeling)
- **Streamlit** (App Deployment)
- **Power BI** (Analytics Dashboard)
- **Joblib** (Model Saving)

---

### 📦 Features

- ✅ Scrapes product data from 6 categories on Croma:
  - Smartphones, Laptops, TVs, Fridges, ACs, Washing Machines
- ✅ Cleans and preprocesses product name, brand, price, and URL
- ✅ Power BI dashboard for interactive insights
- ✅ ML models for predicting product price
- ✅ Streamlit app for real-time price prediction based on user input

---

### 🔢 Model Performance

| Model               | MAE (₹)   | RMSE (₹)  | R² Score |
|--------------------|-----------|-----------|----------|
| Gradient Boosting  | 6,483.72  | —         | 0.9088   |
| Random Forest       | 7,564.17  | 10,748.45 | 0.8986   |

---

### 📈 Power BI Dashboard

Interactive dashboard showing:
- Category-wise price trends
- Top 10 expensive products
- Product counts
- Filterable product cards with links

#### Dashboard:

![Screenshot 2025-07-07 232106](https://github.com/user-attachments/assets/799a44d5-b775-45b4-8d87-0bcef1796225)

#### Dashboard Live View:

- 📥 [View Report or Demo (Google Drive)](https://drive.google.com/file/d/15OTenoOLEKYXIhbBX-nPqJhL9shV2-CF/view?usp=sharing)

---

### 🎯 Streamlit Web App

Users can:
- Select a category
- Enter the product brand
- Paste the product title or description

🔮 And get an **instant predicted price** based on ML model output.

> ![Streamlit App](![Screenshot 2025-07-07 153936](https://github.com/user-attachments/assets/1f23bc07-efa4-4049-a423-9a0a86e17f2c))

> ![Streamlit App]((![Screenshot 2025-07-07 153658](https://github.com/user-attachments/assets/f2be76d3-4f39-4782-8183-61101058524b)))

#### Dashboard Live View:

- 📥 [View Report or Demo (Google Drive)](https://drive.google.com/file/d/1ViLWBeUrgT0Y9IEhEapggU70o1q9jMTS/view?usp=sharing)

---

### 📁 Project Structure

```text
📦 ecommerce-price-predictor
├── croma_raw_products.csv           # Raw scraped data
├── croma_cleaned_products.csv       # Cleaned dataset
├── price_predictor_model.pkl        # Trained ML model (joblib)
├── streamlit_app.py                 # Streamlit UI code
├── powerbi_dashboard.pbix           # Power BI dashboard file
└── README.md                        # Project documentation

```

📬 Contact
📧 Email: agnishwar.das.2003@gmail.com

🔗 LinkedIn: [linkedin.com/in/yourprofile](https://www.linkedin.com/in/agnishwar-das-715416252/)

### Acknowledgements

Croma.com – for providing real-world product data

Scikit-learn – ML toolkit

Streamlit – App deployment

Power BI – Dashboard and data exploration

