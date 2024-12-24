import streamlit as st
from scrape import (
    scrapingWebsite,
    extractBody,
    cleanText,
    splitText
)
from parser import parseChunks

st.set_page_config(page_title="ScrapeAI")
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL:")

if st.button("Scrape"):
    st.write("Scraping...")
    result = scrapingWebsite(url)
    content = extractBody(result)
    st.write("Content Extracted")
    cleanContent = cleanText(content)
    print("Cleaned Content")

    st.session_state.text = cleanContent

    # with st.expander("See Scraped Text"):
    #     st.text_area("Scraped Text", cleanContent, height=400)

if "text" in st.session_state:
    parseDescription = st.text_input("Enter Parsing Description:")

    if st.button("Parse"):
        if parseDescription:
            st.write("Parsing...")
            chunks = splitText(st.session_state.text)
            result = parseChunks(chunks, parseDescription)
            st.write(result)