import streamlit as st

def show_recommendation():
    st.title("🎁 Product Recommendation System")

    customer_id = st.text_input("Enter Customer ID")

    if customer_id:
        st.subheader(f"Recommended Products for {customer_id}")
        st.image("assets/minimal_bag.jpg", width=200, caption="Minimal Bag")
        st.image("assets/jute_bag.png", width=200, caption="Jute Bag")
        st.image("assets/printed_tot.avif", width=200, caption="Printed Tote Bag")
        st.image("assets/canvas_bag.jpg", width=200, caption="Canvas Bag")
        st.success("These are example static recommendations. Add your logic for real ones.")
