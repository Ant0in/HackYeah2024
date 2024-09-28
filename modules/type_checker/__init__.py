

from modules.type_checker.clustering import Clustering
from modules.type_checker.tfidf import TFIDF


class ThemeChecker:

    def __init__(self, url: str, lang: str = 'english') -> None:
        
        self.url: str = url
        self.language: str = lang

    def run(self, dependencies: list) -> set:

        _ncomp: int = 5; _nbest: int = 2

        raw_str: str = dependencies[0]['parsed_pages'][self.url]
        docs: list = ThemeChecker.split_string(raw_str, _ncomp)
        ret: list = list()
        
        # Running TFIDF vectorization to get TFIDVcontainer object
        _TFIDFcontainer = TFIDF.calculateTFIDF(doc_corpus=docs, lang=self.language)
        # Using LDA and KMEANS algorithm to cluster the TFIDF vector
        _lda = Clustering.lda(TFIDF_matrix=_TFIDFcontainer.matrix, comp=_ncomp)
        _km = Clustering.kmeans(TFIDF_matrix=_TFIDFcontainer.matrix, comp=_ncomp)
        # Getting the 2n best fit terms for TFIDF matrix.
        for cluster_num in range(_ncomp):
            kcenter = _km[cluster_num]
            lcenter = _lda[cluster_num]
            ktop = kcenter.argsort()[-_nbest:][::-1]
            ltop = lcenter.argsort()[-_nbest:][::-1]
            ret += [_TFIDFcontainer.terms[k] for k in ktop]
            ret += [_TFIDFcontainer.terms[l] for l in ltop]

        return {'themes': frozenset(ret)}
    
    @staticmethod
    def split_string(s: str, n: int) -> list:

        words = s.split()
        total_words = len(words)
        
        words_per_chunk = total_words // n
        extra_words = total_words % n

        result = []
        start_index = 0

        for i in range(n):
            end_index = start_index + words_per_chunk + (1 if i < extra_words else 0)
            result.append(" ".join(words[start_index:end_index]))
            start_index = end_index

        return result


