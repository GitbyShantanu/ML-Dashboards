import streamlit as st
import pandas as pd
import joblib

# =============================================
# Page Configuration
# =============================================
st.set_page_config(
    page_title="Customer Churn Prediction | Marvellous Infosystems",
    page_icon="📊",
    layout="wide"
)

# =============================================
# Clean Font
# =============================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# =============================================
# Header
# =============================================
st.title("📊 Marvellous Infosystems")
st.caption("Customer Churn Prediction Dashboard · ML Dashboard v1.0 · by Shantanu")


# =============================================
# Load Model & Data
# =============================================
model = joblib.load("Marvellous_ML_Customer_Churn.pkl")
df = pd.read_csv("customer_churn.csv")

# =============================================
# Sidebar — Customer Input Form
# =============================================
with st.sidebar:
    st.header("🔍 Customer Input")

    age = st.number_input("Customer Age", min_value=1, max_value=100, value=30)
    tenure = st.number_input("Tenure (Months)", min_value=0, max_value=120, value=12)
    charges = st.number_input("Monthly Charges (₹)", min_value=0, max_value=50000, value=500)
    calls = st.number_input("Support Calls", min_value=0, max_value=50, value=2)

    st.divider()
    predict_btn = st.button("⚡ Run Prediction", use_container_width=True)

    st.divider()
    st.caption("Built by **Shantanu** | Marvellous Infosystems")

# =============================================
# KPI Overview (from dataset)
# =============================================
st.subheader("📈 Dataset Overview")

total_customers = len(df)
churned = int(df["Churn"].sum()) if "Churn" in df.columns else 0
retained = total_customers - churned
avg_charges = df["MonthlyCharges"].mean() if "MonthlyCharges" in df.columns else 0
avg_tenure = df["Tenure"].mean() if "Tenure" in df.columns else 0

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Customers", total_customers)
k2.metric("Churned", churned)
k3.metric("Retained", retained)
k4.metric("Avg Monthly Charges", f"₹{avg_charges:.0f}")

st.divider()

# =============================================
# Prediction Results
# =============================================
st.subheader("🎯 Prediction Result")

if predict_btn:
    new_customer = pd.DataFrame({
        "Age": [age],
        "Tenure": [tenure],
        "MonthlyCharges": [charges],
        "SupportCalls": [calls]
    })

    prediction = model.predict(new_customer)[0]

    result_col, summary_col = st.columns([1, 1])

    with result_col:
        if prediction == 1:
            st.error("🚨 **HIGH CHURN RISK** — This customer is likely to churn. Consider retention strategies.")
        else:
            st.success("✅ **LOW CHURN RISK** — This customer is unlikely to churn. No immediate action needed.")

    with summary_col:
        st.markdown("**Customer Profile Submitted:**")
        profile_df = pd.DataFrame({
            "Parameter": ["Age", "Tenure", "Monthly Charges", "Support Calls"],
            "Value": [f"{age} years", f"{tenure} months", f"₹{charges}", f"{calls} calls"]
        })
        st.dataframe(profile_df, use_container_width=True, hide_index=True)

else:
    st.info("👈 Enter customer details in the sidebar and click **Run Prediction** to see results.")

st.divider()

# =============================================
# Dataset Preview
# =============================================
st.subheader("🗂️ Training Data Preview")
st.dataframe(df, use_container_width=True, hide_index=True)

# =============================================
# Footer
# =============================================
st.divider()
st.caption("© 2026 Marvellous Infosystems | Customer Churn Prediction Dashboard | Developed by Shantanu Deshmukh")
