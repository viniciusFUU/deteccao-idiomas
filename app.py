from treatment import y_train
import os
import mysql.connector

conn = mysql.connector.connect(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE")    
)

def add_lang(sigla, lang):
    y = y_train()
    
    if lang not in y:
        cursor = conn.cursor()
        insert_lang = f"insert into idiomas(cod_idioma, descricao_idioma) values ('{sigla}', '{lang}')"
        cursor.execute(insert_lang)
        conn.commit()
        
        return "Idioma inserido!"