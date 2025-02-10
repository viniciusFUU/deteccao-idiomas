from treatment import y_train, organized_words
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

def add_word(text):
    words = organized_words()
    langs = y_train()

    sigla = input("sigla: ")

    for lang, word in words.items():
        if sigla not in langs:
            input_lang = input("linguagem: ")

            add_lang(sigla, input_lang)

        if sigla in langs:
            if sigla == lang:
                if text not in word:
                    cursor = conn.cursor()
                    insert_word = f"INSERT INTO texto (texto, cod_idioma) VALUES ('{text}', '{sigla}')"

                    cursor.execute(insert_word)
                    conn.commit()

                    return f"{text} adicionado com sucesso"
                else:
                    return f"{text} já existe na lista"