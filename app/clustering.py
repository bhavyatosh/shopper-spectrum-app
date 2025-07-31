import streamlit as st
import pandas as pd
import joblib
import os

model_path = os.path.join("model", "kmeans_model.pkl")
scaler_path = os.path.join("model", "scaler.pkl")

def show_clustering():
    st.title("🧠 Customer Segmentation using KMeans")

    uploaded_file = st.file_uploader("Upload a transaction CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("📊 Raw Data", df.head())

        try:
            scaler = joblib.load(scaler_path)
            model = joblib.load(model_path)
        except Exception as e:
            st.error("❌ Error loading model or scaler: " + str(e))
            return

        try:
            numeric_df = df.select_dtypes(include=['float64', 'int64'])
            scaled_data = scaler.transform(numeric_df)
            clusters = model.predict(scaled_data)
            df["Cluster"] = clusters
            st.success("✅ Clusters assigned successfully.")
            st.write(df.head())

            st.bar_chart(df["Cluster"].value_counts())

        except Exception as e:
            st.error(f"⚠️ Error during clustering: {e}")
