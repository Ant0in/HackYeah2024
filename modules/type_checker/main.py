

from clustering import Clustering
from tfidf import TFIDF


class ThemeChecker:

    def __init__(self, dependencies: list[str], raw: list[str], lang: str = 'english') -> None:
        
        self.dependencies: list[str] = dependencies
        self.raw_doc: list[str] = raw
        self.language: str = lang

    def run(self) -> set:

        _ncomp: int = 5; _nbest: int = 2

        ret: list = list()
        # Running TFIDF vectorization to get TFIDVcontainer object
        _TFIDFcontainer = TFIDF.calculateTFIDF(doc_corpus=self.raw_doc, lang=self.language)
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

        return set(ret)



if __name__ == '__main__':
    
    raw: list[str] = [
        "le chat est très mignon", 
        "les chats aiment les croquettes",
        "j'aime mon chat qui est vraiment adorable",
        "le chien est aussi un bon animal de compagnie",
        "les animaux aiment jouer dans le parc"
    ]

    print(ThemeChecker(dependencies=..., raw=raw, lang='french').run())