from treatment import y_train, x_train

def probabillity():
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

print(probabillity())