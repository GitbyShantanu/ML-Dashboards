import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="Customer Churn Predictor | Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Header
st.title("📊 Customer Churn Predictor")
st.caption("Customer Retention and Risk Analytics Platform | Developed by Shantanu Deshmukh")

# Paths and Model Loading
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "customer_churn_model.pkl"))
df = pd.read_csv(os.path.join(BASE_DIR, "customer_churn.csv"))

# KPI Overview
st.subheader("📈 Dataset KPI Overview")
total_customers = len(df)
churned = int(df["Churn"].sum()) if "Churn" in df.columns else 0
retained = total_customers - churned
avg_charges = df["MonthlyCharges"].mean() if "MonthlyCharges" in df.columns else 0

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Customers", total_customers)
k2.metric("Churned Customers", churned)
k3.metric("Retained Customers", retained)
k4.metric("Avg Monthly Charges", f"₹{avg_charges:.0f}")

st.divider()

# Input Section (Main Page for Mobile & Desktop Friendly UX)
st.subheader("📝 Enter Customer Details")
st.write("Fill in the customer information below to predict churn probability:")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Customer Age", min_value=1, max_value=100, value=30)
    tenure = st.number_input("Tenure (Months)", min_value=0, max_value=120, value=12)

with col2:
    charges = st.number_input("Monthly Charges (₹)", min_value=0, max_value=50000, value=500)
    calls = st.number_input("Customer Care Calls", min_value=0, max_value=50, value=2)

st.write("")
predict_btn = st.button("⚡ Predict Churn Risk", type="primary", use_container_width=True)

# Prediction Result Section
if predict_btn:
    new_customer = pd.DataFrame({
        "Age": [age],
        "Tenure": [tenure],
        "MonthlyCharges": [charges],
        "SupportCalls": [calls]
    })
    prediction = model.predict(new_customer)[0]

    st.divider()
    st.subheader("🎯 Prediction Outcome")
    
    result_col, summary_col = st.columns([1, 1])
    with result_col:
        if prediction == 1:
            st.error("🚨 **HIGH CHURN RISK** — This customer is likely to discontinue the service. Retention measures recommended.")
        else:
            st.success("✅ **LOW CHURN RISK** — This customer is satisfied and unlikely to churn. No immediate action required.")
    
    with summary_col:
        st.markdown("**Customer Profile Submitted:**")
        profile_df = pd.DataFrame({
            "Parameter": ["Age", "Tenure", "Monthly Charges", "Customer Care Calls"],
            "Value": [f"{age} years", f"{tenure} months", f"₹{charges}", f"{calls} calls"]
        })
        st.dataframe(profile_df, use_container_width=True, hide_index=True)

st.divider()

# Historical Data Preview
st.subheader("🗂️ Historical Data Preview")
st.dataframe(df, use_container_width=True, hide_index=True)

# Footer
st.divider()
st.caption("© 2026 Customer Churn Analytics Platform | Designed and Developed by Shantanu Deshmukh")
