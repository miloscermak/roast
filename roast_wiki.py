import requests
from bs4 import BeautifulSoup
from anthropic import Anthropic
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_wiki_content(url):
    # Přidáme user-agent, aby nás Wikipedie neblokovala
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    # Najdeme hlavní obsah článku
    content = soup.find(id="mw-content-text")

    if not content:
        raise ValueError("Nepodařilo se najít obsah článku. Zkontrolujte, zda je URL platná.")

    # Najdeme všechny odstavce v hlavním obsahu
    content_div = content.find('div', class_='mw-parser-output')
    if not content_div:
        content_div = content

    paragraphs = content_div.find_all('p')

    # Vyfiltrujeme prázdné odstavce a vezmeme první smysluplné odstavce
    meaningful_paragraphs = [p.get_text().strip() for p in paragraphs if len(p.get_text().strip()) > 50]

    if not meaningful_paragraphs:
        raise ValueError("Nepodařilo se najít žádný obsah v článku.")

    # Spojíme první 5 odstavců pro lepší kontext
    text = ' '.join(meaningful_paragraphs[:5])
    return text

def generate_roast(text):
    api_key = st.secrets.get("ANTHROPIC_API_KEY")
    if not api_key:
        st.error("API klíč není nastaven správně")
        st.stop()
        
    client = Anthropic(api_key=api_key)
    
    prompt = f"""You will be writing a comedic "roast" based on a Wikipedia article about a specific person. Here is the Wikipedia text:

<wikipedia_text>
{text}
</wikipedia_text>

Your task is to write a roast of the person described in this Wikipedia article. A roast should be:
- Cynical and sarcastic in tone
- Use sharp, cutting humor
- Focus on the most characteristic or notable aspects of the person
- Be witty and clever rather than simply mean-spirited
- Highlight contradictions, failures, or absurdities in their life or career

Important guidelines:
- Keep your roast to a maximum of 200 words
- Base your commentary only on information provided in the Wikipedia text
- Focus on the person's actions, decisions, career, or public persona rather than physical appearance
- Use a tone that would be appropriate for a comedy roast - irreverent but not genuinely hateful
- Make your observations pointed and memorable

Write your roast in a single paragraph or short series of paragraphs. The goal is to create an entertaining, satirical take on this person's life and achievements based on the factual information provided.
"""
    
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
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