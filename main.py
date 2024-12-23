import streamlit as st
from scrape import scrapingWebsite

st.title("AI Web Scraper")
url = st.text_input("Enter Website URL:")

if st.button("Scrape"):
    st.write("Scraping...")
    result = scrapingWebsite(url)
    print(result)