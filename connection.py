import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def get_all_words():
    conn = mysql.connector.connect(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT texto, cod_idioma FROM texto")

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados

def get_all_langs():
    conn = mysql.connector.connect(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT cod_idioma FROM idiomas")

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados