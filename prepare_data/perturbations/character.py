import random
from string import ascii_letters

def inject_typo(word):
    """
    Introduces a typo in the first alphabetic character of the given word by replacing 
    it with the next letter in the ASCII sequence. Non-alphabetic characters remain unchanged.

    Parameters:
    word (str): The word in which to inject a typo.

    Returns:
    str: The word with a typo introduced at the first alphabetic character.
    """
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
    """
    Introduces typos in at most two words of the given query by randomly selecting 
    two words and altering their first alphabetic character using the inject_typo function.

    Parameters:
    query (str): The query in which to introduce typos.

    Returns:
    str: The query with typos introduced in at most two words.
    """
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
    """
    Alters at most two characters in the given query by randomly selecting 
    two characters and replacing them with the letter 'x'.

    Parameters:
    query (str): The query in which to alter characters.

    Returns:
    str: The query with at most two characters altered.
    """
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
    """
    Adds two extraneous characters ("@%") to the end of the given query.

    Parameters:
    query (str): The query to which extraneous characters are to be added.

    Returns:
    str: The query with "@%" appended to the end.
    """
    return str(query) + "@%"
