from treatment import y_train, x_train, organized_words
from collections import Counter

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
    words_probability_list = {}

    for lang, words in org_words.items():
        word_counts = Counter(words)
        total_words = sum(word_counts.values())
        lang_probability = {}

        for word, count in word_counts.items():
            lang_probability[word] = round(count / total_words, 2)

        words_probability_list[lang] = lang_probability

    return words_probability_list

print(words_probabillity())