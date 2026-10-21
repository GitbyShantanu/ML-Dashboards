# 📊 Customer Churn Prediction Dashboard

An end-to-end Machine Learning web application built using **Streamlit** to predict customer churn risk in real-time. Designed with a clean, responsive, and professional UI suitable for production and portfolio demonstration.

---

## 🚀 Live Demo
- **Deployed App:** [Streamlit Cloud](https://share.streamlit.io) *(Add your live deployment link here)*

---

## 📌 Project Overview
Customer churn is one of the most critical metrics for growing businesses. This application allows business analysts and customer success teams to:
- Input customer attributes (Age, Tenure, Monthly Charges, Support Calls).
- Predict whether the customer is at **High Risk** or **Low Risk** of churning.
- View key high-level dataset metrics (Total Customers, Churned, Retained, Avg Charges).
- Inspect the underlying training data preview directly within the dashboard.

---

## 🛠️ Tech Stack
- **Frontend / UI:** [Streamlit](https://streamlit.io/)
- **Machine Learning / Processing:** [scikit-learn](https://scikit-learn.org/), [joblib](https://joblib.readthedocs.io/), [pandas](https://pandas.pydata.org/)
- **Language:** Python 3.10+
- **Deployment:** Streamlit Community Cloud

---

## 📂 Directory Structure
`	ext
Customer-Churn-Prediction/
├── .streamlit/
│   └── config.toml                  # Streamlit configuration & theme settings
├── Dashboard_Customer_Churn.py      # Main Streamlit application
├── Marvellous_ML_Customer_Churn.pkl # Trained Machine Learning model
├── customer_churn.csv               # Dataset used for overview & training
├── requirements.txt                 # Python dependencies
└── README.md                        # Documentation
`

---

## ⚙️ Local Setup & Run

1. **Clone the repository:**
   `ash
   git clone https://github.com/GitbyShantanu/ML-Dashboards.git
   cd ML-Dashboards/Customer-Churn-Prediction
   `

2. **Create and activate a virtual environment (optional but recommended):**
   `ash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   `

3. **Install dependencies:**
   `ash
   pip install -r requirements.txt
   `

4. **Launch the Streamlit app:**
   `ash
   streamlit run Dashboard_Customer_Churn.py
   `

---

## 👤 Author
- **Developed by:** Shantanu Deshmukh
- **Organization:** Marvellous Infosystems
