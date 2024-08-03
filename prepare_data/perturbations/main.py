from prepare_data.perturbations.character import perturb_c1, perturb_c2, perturb_c3
from prepare_data.perturbations.word import perturb_w1, perturb_w2, perturb_w3
from prepare_data.perturbations.sentence import perturb_s1, perturb_s2, perturb_s3


def all_perturbation(queries):
    """
    Applies a series of perturbations to a list of input queries at character, word, and sentence levels. 
    For each query, nine different perturbations are applied:
    - Character-level: introduce typos, alter characters, and add extraneous characters.
    - Word-level: replace words with synonyms, delete non-essential words, and add neutral words.
    - Sentence-level: append irrelevant handles, paraphrase sentences, and alter syntactic structure.

    Parameters:
    queries (list of str): A list of queries to be perturbed.

    Returns:
    tuple: A tuple containing nine lists, each corresponding to one type of perturbation applied across all queries:
        - c1p_sent: Queries with character-level perturbation type 1 (typos).
        - c2p_sent: Queries with character-level perturbation type 2 (character alteration).
        - c3p_sent: Queries with character-level perturbation type 3 (extraneous characters).
        - w1p_sent: Queries with word-level perturbation type 1 (synonym replacement).
        - w2p_sent: Queries with word-level perturbation type 2 (word deletion).
        - w3p_sent: Queries with word-level perturbation type 3 (neutral word addition).
        - s1p_sent: Queries with sentence-level perturbation type 1 (irrelevant handle addition).
        - s2p_sent: Queries with sentence-level perturbation type 2 (paraphrasing).
        - s3p_sent: Queries with sentence-level perturbation type 3 (syntactic alteration).
    """
    c1p_sent = []
    c2p_sent = []
    c3p_sent = []
    w1p_sent = []
    w2p_sent = []
    w3p_sent = []
    s1p_sent = []
    s2p_sent = []
    s3p_sent = []
    c = 0
    for query in queries:
        c = c + 1
        if query is None:
            c1p_sent.append("")
            c2p_sent.append("")
            c3p_sent.append("")
            w1p_sent.append("")
            w2p_sent.append("")
            w3p_sent.append("")
            s1p_sent.append("")
            s2p_sent.append("")
            s3p_sent.append("")
        else:
            c1p_sent.append(perturb_c1(query))
            c2p_sent.append(perturb_c2(query))
            c3p_sent.append(perturb_c3(query))
            w1p_sent.append(perturb_w1(query))
            w2p_sent.append(perturb_w2(query))
            w3p_sent.append(perturb_w3(query))
            s1p_sent.append(perturb_s1(query))
            s2p_sent.append(perturb_s2(query))
            s3p_sent.append(perturb_s3(query))

    return (
        c1p_sent,
        c2p_sent,
        c3p_sent,
        w1p_sent,
        w2p_sent,
        w3p_sent,
        s1p_sent,
        s2p_sent,
        s3p_sent,
    )
