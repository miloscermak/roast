import requests
from bs4 import BeautifulSoup
from anthropic import Anthropic
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_wiki_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Získáme hlavní obsah článku
    content = soup.find(id="mw-content-text")
    paragraphs = content.find_all('p')
    
    # Spojíme první 3 odstavce pro kontext
    text = ' '.join([p.get_text() for p in paragraphs[:3]])
    return text

def generate_roast(text):
    client = Anthropic(api_key=st.secrets.get("ANTHROPIC_API_KEY"))
    
    prompt = f"""
    Jsi komik specializující se na roasty. Přečti si tento text o osobě a vytvoř vtipný, ale ne příliš krutý roast:
    
    {text}
    
    Vytvoř krátký roast o 2-3 větách.
    """
    
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=300,
        temperature=0.9,
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )
    
    return message.content

def main():
    url = input("Zadejte URL článku z Wikipedie: ")
    try:
        wiki_text = get_wiki_content(url)
        roast = generate_roast(wiki_text)
        print("\nRoast:\n", roast)
    except Exception as e:
        print(f"Došlo k chybě: {e}")

if __name__ == "__main__":
    main() 