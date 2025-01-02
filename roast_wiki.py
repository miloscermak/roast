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
    api_key = st.secrets.get("ANTHROPIC_API_KEY")
    if not api_key:
        st.error("API klíč není nastaven správně")
        st.stop()
        
    client = Anthropic(api_key=api_key)
    
    prompt = f"""
<examples>\n<example>\n<WIKI_ARTICLE>\nVystudoval kybernetiku na elektrotechnické fakultě ČVUT. V roce 1988 se jako dobrovolník zúčastnil experimentu Štola 88 simulující let k Marsu.[1][2]\n\nProfesně se zaměřuje zejména na technologické novinky a trendy, internet, média, ale věnuje se i kultuře, politice a dalším tématům. Působil v Lidových novinách (šéfkomentátor 2003–2005) a časopise Reflex (redaktor 1992–2003). Je spoluautorem postmoderního komiksu Hana a Hana. Pro Českou televizi připravoval např. pořady Zavináč, Bez obalu, Letem světem. Od roku 2001 je na částečný pracovní úvazek členem katedry žurnalistiky FSV UK. Od 1. června 2019 je externím spolupracovníkem Seznam.cz a působí jako komentátor serveru Seznam Zprávy. Působí také jako konzultant, je spolumajitelem firmy NextBig.cz.[3] Do února 2019 byl šéfredaktorem serveru iHNed.cz.\n\nSpolečně s Luďkem Staňkem tvoří komickou dvojici Čermák Staněk; natáčí spolu podcast Čermák Staněk Comedy Podcast a veřejně spolu vystupují na stand-upech a ve Werichově vile, kde svá vystoupení zkoušejí před menším publikem.\n\nV roce 2010 získal 1. místo v kategorii Osobnost roku v anketě Křišťálová Lupa.[4]\n\nJeho manželkou je Senta Čermáková, kterou si vzal dne 6. 9.1992 na Vyšehradě. Mají dvě děti, Vavřince (1994) a Jolanu (1996).\n\nTvorba\nKnihy\nAlza: Příběh firmy, která si do toho nenechala mluvit (BizBooks, 2022, spolu s Michalem Rybkou)\nPřišel Bůh do kavárny v Karlíně... (XYZ, 2018, spolu s Luďkem Staňkem)\nValčík na přivítanou a dalších třiatřicet povídek (2015)\nMuži, co zírají na ženy (a dalších 33 povídek z fleku) (2014)\nLovestory ve výtahu (a dalších 77 povídek z fleku) (XYZ, 2013)\nKrutopřísné povídky – \"Lži \"o českých politicích (Mladá Fronta, 2010)\nNikomu to neříkejte (rozšířené, 2. vydání, Extra Média, 2007)\nHana a Hana: Wow! (Extra Média, 2008)\nNikomu to neříkejte (Vydáno vlastním nákladem – Lulu.com, 2007)\nHana a Hana : ty kráso (BB/art, 2007)\nKdyby sólokapři měli křídla, aneb, Proč nás novináře nikdo nemá rád (Nakladatelství Lidové noviny, 2006)\nNemachruj, ta holka je nakreslená!, aneb, Únos z komiksu Hana a Hana (BB/art, 2006)\nHana a Hana : ty vogo (BB/art, 2005)\nHana a Hana : ty jo (BB/art, 2004)\n100 (dalších) tipů pro pozoruhodný Internet (Academia, 2001)\nJak se skáče na špek (Academia, 2001)\n100 fíglů a tipů pro Internet (Academia, 2001)\nInternet snadno a rychle (Atlas.cz, 2001)\nSouběžný portrét : Václav Klaus, Miloš Zeman (První Nakladatelství Knihcentrum, 1998)\nKlaus je mrtev, ať žije Klaus : pohled do zákulisí vysoké politiky (Duel, 1997)\nNanebevzetí Karla Kryla (Academia, 1997, ISBN 8020006613)\nPravděpodobné vzdálenosti: Rozhovor s Jaroslavem Hutkou (Academia, 1999)\nJak chutnají peníze : (nenápadný půvab českých milionářů) (Exact Publishing, 1995)\nPůlkacíř: Rozhovor s Karlem Krylem (Academia, 1993, ISBN 978-80-7335-194-6)\nPovolání: Děvka (Rozmluvy, 1992)\nKlec na policajta (Rozmluvy, 1991)\n</WIKI_ARTICLE>\n<ideal_output>\nHm, Miloš Čermák – živoucí důkaz toho, že i kybernetik může skončit jako stand-up komik. Představte si, že někdo vystuduje ČVUT, aby pak trávil večery ve Werichově vile vtipkováním s Luďkem Staňkem. To je jako kdyby Einstein zahodil teorii relativity a začal moderovat televizní pořad o vaření. Nebo ještě o něčem víc banálním.\nA ten experiment Štola 88 simulující let na Mars? Asi tam našel svůj smysl pro humor, protože kdo by nepobral trochu svérázný pohled na svět po tom, co strávil dobrovolně čas v podzemí s představou, že letí na rudou planetu. Možná proto pak napsal knihu \"Přišel Bůh do kavárny v Karlíně...\" – protože po takovém zážitku už člověku nic divnějšího nepřijde.\nJeho kariérní dráha je fascinující sbírkou chyb, maskovaných za originální rozhodnutí. Od šéfkomentátora Lidových novin přes autora komiksu Hana a Hana až po podcast, kde dva dospělí chlapi rozebírají život s vážností puberťáků. \nA ty jeho knihy! \"Muži, co zírají na ženy\" – kdyby to bylo v jednotném čísla, mohla to být Čermákova autobiografie.\nNejlepší je ale jeho timing – v roce 2010 vyhrál anketu Křišťálová Lupa v kategorii Osobnost roku. To muselo být opravdu slabé období pro český internet, když největší osobností byl muž, který se rozhodl opustit seriózní žurnalistiku ve prospěch stand-upu.\n</ideal_output>\n</example>\n</examples>\n\n


        Text to roast:
        {text}
                            "text": "Vaším úkolem je přečíst si životopisný článek z Wikipedie a napsat vtipný, sarkastický a ironický roast o dané osobě. Není třeba mít respekt, ale text by neměl být zlý ani vulgární.\n\nNejprve si přečtěte následující článek z Wikipedie \n<wiki_article>\n{{WIKI_ARTICLE}}\n</wiki_article>\n\nPečlivě si přečtěte článek a zaměřte se na následující aspekty:\n1. Klíčové životní události a úspěchy\n2. Osobnostní rysy nebo zvyky\n3. Kontroverzní nebo neobvyklé momenty\n4. Opakující se témata nebo vzorce v jejich životě\n\nPři psaní roastu dodržujte tyto pokyny:\n1. Buďte sarkastičtí a ironičtí\n2. Zaměřte se na slabá místa nebo zvláštnosti\n3. Používejte slovní hříčky, přehánění a vtipná přirovnání\n4. Buďte kritičtí\n5. Vyhněte se urážlivým komentářům o rase, pohlaví, náboženství nebo zdravotním stavu\n\nNapište roast o přibližně 200 slovech v češtině. Začněte vtipným úvodem, který nastaví tón zbytku textu. Poté se zaměřte na 3-4 klíčové body z jejich života nebo kariéry, které můžete vtipně okomentovat. Zakončete roast trefnou pointou nebo překvapivým zvratem.\n\nSvůj roast napište do <roast> tagů. Ujistěte se, že je text plynulý, soudržný a že jednotlivé vtipy na sebe navazují. Používejte bohatou slovní zásobu a různorodé větné struktury, aby byl text zajímavý a zábavný.
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