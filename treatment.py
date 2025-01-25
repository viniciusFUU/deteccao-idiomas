import connection
import re

def tokenazing_words():
    texts = []
    words_by_language = {"pt":[], "en":[], "es":[]}

    dados = connection.get_all_words()

    for texto, idioma in dados:
        texts.append({
            "cod_idioma": idioma.lower(),
            "texto": re.sub(r'[^a-zA-Z\s]', '', texto)
            })
        
    for item in texts:
        texto = item["texto"]
        idioma = item["cod_idioma"]

        words_by_language[idioma].extend(texto.split())
    
    return words_by_language

def index_transformation():
    values = tokenazing_words()
    all_words = set()

    for word_list in values.values(  ):
        all_words.update(word_list)

    vocabulary = {word: i for i, word in enumerate(sorted(all_words))}
    return vocabulary

def data_prepare_to_x_training():
    index_values = index_transformation()
    token_values = tokenazing_words()

    x_train = []

    for value in token_values.values():
        train_list = []

        for word in value:
            for str, i in index_values.items():
                if str == word:
                    train_list.append(i)

        x_train.append(train_list)

    return x_train

def data_prepare_to_y_training():
    index_values = index_transformation()
    token_values = tokenazing_words()

    y_train = []

    for value, values in token_values.items():
        counter = 0
        
        for str, int in index_values.items():
            if str in values:
                counter+=1

        if len(values) == counter:
            y_train.append(value)  

    return y_train

print(data_prepare_to_y_training())