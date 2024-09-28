
from sklearn.feature_extraction.text import TfidfVectorizer

class TFIDF:
    
    @staticmethod
    def calculateTFvec(word_vec: list[str]) -> dict[str, float]:

        _ret: dict[str, float] = dict()
        for w in word_vec:
            if w not in _ret: _ret[w] = 1
            else: _ret[w] += 1
            
        wc: int = len(word_vec)
        assert wc > 0, f'wc = {wc}'

        return {k: (v / wc) for k, v in _ret.items()}
    
    @staticmethod
    def calculateIDF(doc_corpus: list[list[str]]) -> dict[str, float]:

        _idf: dict[str, float] = dict()
        total_docs = len(doc_corpus)
        
        for doc in doc_corpus:
            for word in set(doc):
                _idf[word] = _idf.get(word, 0) + 1
        
        return {word: log((1 + total_docs / (1 + count)), 10) for word, count in _idf.items()}

    @staticmethod
    def calculateTFIDFvec(doc_corpus: list[list[str]]) -> dict:

        idf_scores = TFIDF.calculateIDF(doc_corpus)
        
        tfidf_corpus = []
        for doc in doc_corpus:
            tf_vec = TFIDF.calculateTFvec(doc)
            tfidf_vec = {word: tf_vec[word] * idf_scores[word] for word in tf_vec}
            tfidf_corpus.append(tfidf_vec)
        
        return tfidf_corpus
    
    @staticmethod
    def mergeTFIDFvec(tfidf_corpus: list[dict]) -> dict:
        
        _merged: dict = dict()
        for tfidfvec in tfidf_corpus:
            for word, weight in tfidfvec.items():
                if word in _merged: _merged[word] += weight
                else: _merged[word] = weight
        return _merged

    @staticmethod
    def run(doc_corpus: list[list[str]]) -> dict[str: float]:

        _tfidf_corpus: list[dict] = TFIDF.calculateTFIDFvec(doc_corpus=doc_corpus)
        _merged_tfidf: dict[str: float] = TFIDF.mergeTFIDFvec(tfidf_corpus=_tfidf_corpus)
        return _merged_tfidf


if __name__ == '__main__':
      
    dc: list = [
        "le gentil petit chat dans la forêt uwu très mignon",
        "le chat aime bien les croquettes miam miam les bonnes croquettes",
        "j'ai un chat super mignon uwu très mignon il est super cool et très beau",
        "petit chat se balade dans la prairie"
    ]

    tfidf = TFIDF.run(doc_corpus=[i.split(' ') for i in dc])