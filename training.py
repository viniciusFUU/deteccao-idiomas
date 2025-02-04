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

def nav_bayles(text):
    L_probabillity = langs_probabillity()
    W_probabillity = words_probabillity()
    lang_scores = {}
    
    total_word_probability = sum(W_probabillity[lang].get(text, 0) for lang in W_probabillity)

    if total_word_probability == 0:
        return f"A palavra '{text}' não foi encontrada no vocabulário treinado."

    for lang, lang_prob in L_probabillity.items():
        if text in W_probabillity.get(lang, {}):
            word_prob = W_probabillity[lang][text]
            lang_scores[lang] = (word_prob * lang_prob) / total_word_probability

    if lang_scores:
        best_lang = max(lang_scores, key=lang_scores.get)
        best_prob = round(lang_scores[best_lang] * 100, 2)
        return f"A palavra '{text}' é do idioma '{best_lang}'."
    else:
        return f"A palavra '{text}' não foi encontrada em nenhum idioma."