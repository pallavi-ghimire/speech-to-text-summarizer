import networkx as nx
import numpy as np
import math


from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer


def final(transcribe, num):
    def textrank(document):
        bow_matrix = CountVectorizer().fit_transform(sentences)
        normalized = TfidfTransformer().fit_transform(bow_matrix)
        similarity_graph = normalized * normalized.T
        nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
        scores = nx.pagerank(nx_graph)
        return sorted(((scores[i], s) for i, s in enumerate(sentences)),
                      reverse=True)

    def tokenize_all(doc):
        # insert the check statement here
        sentence_tokenizer = PunktSentenceTokenizer()
        sentences = sentence_tokenizer.tokenize(doc)
        return sentences

    text = transcribe
    sentences = tokenize_all(text)
    variable = textrank(sentences)

    # here, you are deleting the statements with the most value
    if(len(sentences) < 10):
        perc = math.ceil((int(num) / 100) * len(sentences))
    else:
        perc = math.floor((int(num) / 100) * len(sentences))
    del variable[:perc]

    stmts = []
    for vals in variable:
        stmts.append(vals[1])

    # here, you remove the sentences with less value from the original text
    for s in sentences[:]:
        if s in stmts:
            sentences.remove(s)

    return sentences
