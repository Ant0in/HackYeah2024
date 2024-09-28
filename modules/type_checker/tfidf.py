

from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from dataclasses import dataclass



@dataclass
class TFIDFcontainer:
    matrix: object
    terms: list
    scores: list


class TFIDF:
    
    @staticmethod
    def calculateTFIDF(doc_corpus: list[str], lang: str = 'english') -> TFIDFcontainer:
        # Vectorize doc_corpus using TFIDF algorithm.
        _stopwords: list[str] = TFIDF.get_stopwords(lang=lang)
        _vectorizer: TfidfVectorizer = TfidfVectorizer(stop_words=_stopwords)
        _tfidf_matrix = _vectorizer.fit_transform(doc_corpus)
        
        _terms = _vectorizer.get_feature_names_out()
        _scores = _tfidf_matrix.toarray()[0]
        return TFIDFcontainer(matrix=_tfidf_matrix, terms=_terms, scores=_scores)

    @staticmethod
    def get_stopwords(lang: str) -> list[str]:
        # Get the stopwords to ignore from given language 'lang'.
        try:
            #TFIDF.download_NLTKstopwords()
            stw: list[str] = nltk.corpus.stopwords.words(lang)
            return stw
        except: return 'english'
    
    @staticmethod
    def download_NLTKstopwords() -> None:
        # Download the NLTK stopwords. Call only if not downloaded.
        nltk.download('stopwords')


