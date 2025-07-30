# 🛍️ Shopper Spectrum: Customer Segmentation and Product Recommendation System

Welcome to the Shopper Spectrum project! This AI-powered web app helps e-commerce platforms segment their customers based on purchasing behavior (RFM Analysis) and recommend products using collaborative filtering.

---

## 📁 Project Structure
├── .streamlit/
├── app/
│ ├── init.py
│ ├── clustering.py
│ ├── main.py
│ ├── model.py
│ ├── recommendation.py
│ ├── utils.py
├── assets/
│ ├── canvas_bag.jpg
│ ├── jute_bag.png
│ ├── minimal_bag.jpg
│ ├── printed_tot.avif
├── components/
├── model/
│ ├── kmeans_model.pkl
│ ├── scaler.pkl
├── style/
│ └── custom.css
├── requirements.txt
└── README.md

---

## 💡 Features

- 🔍 **Customer Segmentation** using KMeans clustering on RFM features.
- 🎯 **Product Recommendations** based on item similarity and user preferences.
- 🎨 **Modern UI** with product images and custom CSS.
- 📊 **Charts & Visualizations** using Plotly and Seaborn.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd shopper-spectrum
