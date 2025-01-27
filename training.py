from treatment import y_train, x_train, organized_words

def langs_probabillity():
    y = y_train()
    x = x_train()
    qtd_langs = len(x)

    qtd_langs_list = {}
    probability_list = {}

    for lang in y:
        qtd_langs_list[lang] = qtd_langs_list.get(lang, 0) + 1

    for lang, count in qtd_langs_list.items():
        probability_list[lang] = round(count / qtd_langs, 2)

    return probability_list

def words_probabillity():
    org_words = organized_words()
    x = x_train()
    y = y_train()
    qtd_words_by_lang = {}
    words_probabillity_list = {}

    for lang, list in org_words.items():
        qtd_words_by_lang[lang] = qtd_words_by_lang.get(lang, 0) + len(list)   

    for lang, words in org_words.items():
        idx = 0
        counter = 0
        lang_probabillity = {}

        for word in words:
            for w in words:
                if w == word:
                    counter+=1
            lang_probabillity[word] = round(counter / len(words), 2)

        words_probabillity_list[lang] = lang_probabillity

    return words_probabillity_list

print(words_probabillity())