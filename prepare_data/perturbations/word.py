import random
import nltk
from nltk.corpus import wordnet
from nltk import word_tokenize

# nltk.download("punkt")
# nltk.download("averaged_perceptron_tagger")


def return_syn(word):
    """
    Returns a synonym for the given word using WordNet. If no suitable synonym is found,
    the original word is returned.

    Parameters:
    word (str): The word for which to find a synonym.

    Returns:
    str: A synonym of the word, or the original word if no synonym is found.
    """
    for syn in wordnet.synsets(word):
        for name in syn.lemma_names():
            if name != word and name is not None:
                return name
    return word

def perturb_w1(query):
    """
    Replaces at most two words in the query with their synonyms. The words are randomly selected.

    Parameters:
    query (str): The query in which to replace words with their synonyms.

    Returns:
    str: The query with at most two words replaced by their synonyms.
    """
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
    """
    Identifies and returns the indices of all prepositions in the given prompt.

    Parameters:
    prompt (str): The text to be analyzed for prepositions.

    Returns:
    list: A list of indices representing the positions of prepositions in the prompt.
    """
    words = word_tokenize(prompt)
    prep_index_list = []
    index = -1
    for _, y in nltk.pos_tag(words):
        index += 1
        if y == "IN":
            prep_index_list.append(index)
    return prep_index_list

def perturb_w2(query):
    """
    Deletes at most two prepositions from the query that do not alter its overall meaning.
    The prepositions are randomly selected.

    Parameters:
    query (str): The query in which to delete prepositions.

    Returns:
    str: The query with at most two prepositions removed.
    """
    prep = return_all_prep(query)
    if len(prep) > 2:
        prep = list(random.sample(set(prep), 2))

    words = query.split()
    for i in range(len(words)):
        if i in prep:
            words[i] = ""
    return " ".join(words)

def perturb_w3(query):
    """
    Adds semantically neutral words ("okay" and "done") to the beginning and end of the query.

    Parameters:
    query (str): The query to which neutral words will be added.

    Returns:
    str: The query with "okay" added at the beginning and "done" at the end.
    """
    return "okay " + query + " done."
