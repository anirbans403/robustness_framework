import random
from string import ascii_letters


def inject_typo(word):
    flag = True
    ns = ""
    for c in word:
        if c in ascii_letters and flag:
            ns = ns + ascii_letters[(ascii_letters.index(c) + 1) % len(ascii_letters)]
            flag = False
        else:
            ns += c
    return ns


def perturb_c1(query):
    words = query.split()
    w_len = len(words)

    if w_len > 1:
        w1_index = random.randrange(1, w_len - 1)
        w2_index = random.randrange(1, w_len - 1)
        word1 = words[w1_index]
        word2 = words[w2_index]
        words[w1_index] = inject_typo(word1)
        words[w2_index] = inject_typo(word2)
    return " ".join(words)


def perturb_c2(query):
    c_len = len(query)
    if c_len > 1:
        c1_index = random.randrange(1, c_len - 1)
        c2_index = random.randrange(1, c_len - 1)
        c1 = query[c1_index]
        c2 = query[c2_index]
        query = query[: c1_index - 1] + "x" + query[c1_index:]
        query = query[: c2_index - 1] + "x" + query[c2_index:]

    return query


def perturb_c3(query):
    return str(query) + "@%"
