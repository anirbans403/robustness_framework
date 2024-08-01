import random
import nltk
from nltk.corpus import wordnet
from nltk import word_tokenize

# nltk.download("punkt")
# nltk.download("averaged_perceptron_tagger")


def return_syn(word):
    for syn in wordnet.synsets(word):
        for name in syn.lemma_names():
            if name != word and name is not None:
                return name
    return word


def perturb_w1(query):
    words = query.split()
    w_len = len(words)
    if w_len > 1:
        w1_index = random.randrange(1, w_len - 1)
        w2_index = random.randrange(1, w_len - 1)

        word1 = words[w1_index]
        word2 = words[w2_index]
        words[w1_index] = return_syn(word1)
        words[w2_index] = return_syn(word2)
    return " ".join(words)


def return_all_prep(prompt):
    words = word_tokenize(prompt)
    prep_index_list = []
    index = -1
    for _, y in nltk.pos_tag(words):
        index += 1
        if y == "IN":
            prep_index_list.append(index)
    return prep_index_list


def perturb_w2(query):
    prep = return_all_prep(query)
    if len(prep) > 2:
        prep = list(random.sample(set(prep), 2))

    words = query.split()
    for i in range(len(words)):
        if i in prep:
            words[i] = ""
    return " ".join(words)


def perturb_w3(query):
    return "okay " + query + " done."
