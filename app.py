import streamlit as st
from roast_wiki import get_wiki_content, generate_roast
import os

def is_wiki_url(url):
    return "wikipedia.org" in url

st.set_page_config(page_title="Wiki Roaster", page_icon="🎭")

st.title("Wiki Roaster 🎭")
st.write("Zadejte URL článku z Wikipedie a nechte si vygenerovat vtipný roast!")

url = st.text_input("URL článku z Wikipedie")

if not st.secrets.get("ANTHROPIC_API_KEY"):
    st.error("⚠️ ANTHROPIC_API_KEY není nastaven!")
    st.stop()

if url:
    if not is_wiki_url(url):
        st.error("Prosím zadejte platnou URL z Wikipedie")
    else:
        with st.spinner("Generuji roast..."):
            try:
                wiki_text = get_wiki_content(url)
                roast = generate_roast(wiki_text)
                
                st.success("Roast byl vygenerován!")
                st.write("---")
                st.markdown(f"### Roast:\n{roast}")
                
            except Exception as e:
                st.error(f"Došlo k chybě: {str(e)}")

st.write("---")
st.markdown("Vytvořeno pomocí Claude Sonnet 4.5 API") 