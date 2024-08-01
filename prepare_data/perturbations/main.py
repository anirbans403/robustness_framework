from prepare_data.perturbations.character import perturb_c1, perturb_c2, perturb_c3
from prepare_data.perturbations.word import perturb_w1, perturb_w2, perturb_w3
from prepare_data.perturbations.sentence import perturb_s1, perturb_s2, perturb_s3


def all_perturbation(queries):
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
