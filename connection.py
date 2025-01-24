import mysql.connector
import os
import re
from dotenv import load_dotenv


def get_all_texts():
    conn = mysql.connector.connect(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT texto, cod_idioma FROM texto")
    texts = []
    words_by_language = {"pt":[], "en":[], "es":[]}

    dados = cursor.fetchall()

    for texto, idioma in dados:
        texts.append({
            "cod_idioma": idioma.lower(),
            "texto": re.sub(r'[^a-zA-Z\s]', '', texto)
            })
        
    for item in texts:
        texto = item["texto"]
        idioma = item["cod_idioma"]

        words_by_language[idioma].extend(texto.split())

    cursor.close()
    conn.close()
    
    return words_by_language

print(get_all_texts())