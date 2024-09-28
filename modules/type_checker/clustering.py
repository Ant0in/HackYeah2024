from sklearn.cluster import KMeans
from sklearn.decomposition import LatentDirichletAllocation


class Clustering:

    @staticmethod
    def kmeans(TFIDF_matrix, comp: int = 3) -> object:
        
        _kmeans = KMeans(n_clusters=comp)
        _kmeans.fit(TFIDF_matrix)
        return _kmeans.cluster_centers_

    @staticmethod
    def lda(TFIDF_matrix, comp: int = 3) -> object:
        
        _lda = LatentDirichletAllocation(n_components=comp)
        _lda.fit(TFIDF_matrix)
        return _lda.components_
