import streamlit as st
import requests

# Function to fetch search results using Google Custom Search API
def fetch_search_results(query, api_key, cx):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"
    response = requests.get(url)
    if response.status_code == 200:
        search_results = response.json()
        return search_results.get('items', [])
    else:
        return None

# Streamlit UI
st.title('LegalDrafts')

# Input fields
query = st.text_input('Enter your search query:')
api_key = "AIzaSyD1uGJv5c5uDoGFNDGttzxf_DgKCTLIhIc"
cx = "e77ea39b05be343b0"  # Replace with your Custom Search Engine ID

# Button to trigger search
if st.button('Search'):
    if query:
        search_results = fetch_search_results(query, api_key, cx)
        if search_results:
            for item in search_results:
                st.markdown(f"**{item['title']}**")
                st.write(item['link'])
                st.write(item['snippet'])
        else:
            st.write("No results found.")
    else:
        st.write("Please enter a search query.")
