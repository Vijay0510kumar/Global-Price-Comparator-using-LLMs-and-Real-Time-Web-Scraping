import streamlit as st
import requests

st.title("🌍 Price Comparison Tool")

country = st.selectbox("Select Country", ["IN"])
query = st.text_input("Enter Product", "boAt Airdopes 311 Pro")

if st.button("Compare Prices"):
    with st.spinner("Fetching prices..."):
        res = requests.post("http://localhost:8080/search", json={
            "country": country,
            "query": query
        })

        if res.status_code == 200:
            data = res.json()
            for r in data:
                st.markdown(f"""
                ### {r['productName']}
                - ₹{r['price']} ({r['currency']})
                - [🔗 Buy Now]({r['link']})
                - Seller: {r['seller']}
                ---
                """)
        else:
            st.error("API request failed")
