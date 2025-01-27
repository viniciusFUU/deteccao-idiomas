import connection
import re

def organized_words():
    texts = []
    words_by_language = {"pt":[], "en":[], "es":[]}

    dados = connection.get_all_words()

    for texto, idioma in dados:
        texts.append({
            "cod_idioma": idioma.lower(),
            "texto": re.sub(r'[^\w\s]', '', texto.lower())
            })
        
    for item in texts:
        texto = item["texto"]
        idioma = item["cod_idioma"]

        words_by_language[idioma].extend(texto.split())
    
    return words_by_language

def indexing_words():
    values = organized_words()
    all_words = set()

    for word_list in values.values():
        all_words.update(word_list)

    vocabulary = {word: i for i, word in enumerate(sorted(all_words))}

    return vocabulary

def separing_for_groups_the_words():
    index_values = indexing_words()
    organized_values = organized_words()

    x_train = []

    for value in organized_values.values():
        train_list = []

        for word in value:
            for str, i in index_values.items():
                if str == word:
                    train_list.append(i)

        x_train.append(train_list)

    return x_train

def lang_position():
    index_values = indexing_words()
    organized_values = organized_words()

    y_train = []

    for lang, words in organized_values.items():
        print(lang, words)
        if all(word in index_values for word in words):
            y_train.append(lang)

    return y_train

def definition_of_priority(text):
    text_joined = text.lower().split()
    count_definitition = 0
    idioma = ""

    organized_word = organized_words()

    for lang, words in organized_word.items():
        counter = 0

        for word in words:
            if word in text_joined:
                counter+=1
            
        if counter > count_definitition:
            count_definitition = counter
            idioma = lang

    return idioma