import streamlit as st
from app.clustering import show_clustering
from app.recommendation import show_recommendation

from streamlit_option_menu import option_menu

st.set_page_config(page_title="Shopper Spectrum", layout="wide")

def main():
    with st.sidebar:
        selected = option_menu(
            menu_title="Shopper Spectrum",
            options=["Customer Segmentation", "Product Recommendation"],
            icons=["people", "gift"],
            default_index=0,
        )

    if selected == "Customer Segmentation":
        show_clustering()
    elif selected == "Product Recommendation":
        show_recommendation()

if __name__ == "__main__":
    main()
