
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from numpy import ndarray

class TFIDF:

    @staticmethod
    def caculateTFIDFvec(doc_corpus: list[list[str]], language: str = 'english') -> dict:
        # Vectorize doc_corpus using TFIDF algorithm.
        _stopwords: list[str] = TFIDF.get_stopwords(lang=language)
        _vectorizer: TfidfVectorizer = TfidfVectorizer(stop_words=_stopwords)

        _tfidf_matrix = _vectorizer.fit_transform(doc_corpus)
        _terms: ndarray = _vectorizer.get_feature_names_out()
        _scores: ndarray = _tfidf_matrix.toarray()[0]

        tfidf_scores = {_terms[i]: _scores[i] for i in range(len(_terms))}
        return tfidf_scores

    @staticmethod
    def get_stopwords(lang: str) -> list[str]:
        # Get the stopwords to ignore from given language 'lang'.
        stw: list[str] = nltk.corpus.stopwords.words(lang)
        return stw
    
    def download_NLTKstopwords() -> None:
        # Download the NLTK stopwords. Call only if not downloaded.
        nltk.download('stopwords')



if __name__ == '__main__':
      
    dc: list = [
        "le gentil petit chat dans la forêt uwu très mignon",
        "le chat aime bien les croquettes miam miam les bonnes croquettes",
        "j'ai un chat super mignon uwu très mignon il est super cool et très beau",
        "petit chat se balade dans la prairie"
    ]

    tfidf = TFIDF.caculateTFIDFvec(dc, 'french')
    print(tfidf)