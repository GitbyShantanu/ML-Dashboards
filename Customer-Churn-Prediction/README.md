# 📊 Customer Churn Prediction Dashboard

An end-to-end Machine Learning web application built using **Streamlit** to predict customer churn risk in real-time. Designed with a clean, responsive, and industry-standard UI suitable for business analytics and portfolio presentation.

---

## 🚀 Live Demo
- **Deployed App:** [Streamlit Cloud](https://share.streamlit.io) *(Add your live deployment link here)*

---

## 📌 Project Overview
Customer retention is crucial for sustainable business growth. This interactive dashboard enables customer success and analytics teams to:
- Input customer metrics (Age, Tenure, Monthly Charges, Support Calls).
- Predict in real time whether a customer is at **High Risk** or **Low Risk** of churning.
- Track high-level dataset metrics (Total Customers, Churned, Retained, Avg Monthly Charges).
- Inspect underlying historical customer data directly inside the interface.

---

## 🛠️ Tech Stack
- **Frontend / Dashboard:** Streamlit
- **Machine Learning:** scikit-learn, joblib
- **Data Manipulation:** pandas
- **Deployment Platform:** Streamlit Community Cloud

---

## 📂 Project Files

| File / Folder | Purpose |
| :--- | :--- |
| `Dashboard_Customer_Churn.py` | Main Streamlit web application |
| `Marvellous_ML_Customer_Churn.pkl` | Pre-trained Machine Learning classification model |
| `customer_churn.csv` | Dataset used for training and overview |
| `requirements.txt` | Python dependencies required for execution |
| `.streamlit/config.toml` | UI and theme configuration settings |
| `README.md` | Documentation and setup guide |

---

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GitbyShantanu/ML-Dashboards.git
   cd ML-Dashboards/Customer-Churn-Prediction
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run Dashboard_Customer_Churn.py
   ```

---

## 👤 Author
- **Developed by:** Shantanu Deshmukh
