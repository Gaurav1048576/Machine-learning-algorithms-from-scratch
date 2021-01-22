import numpy as np

class PCA:

    def __init__(self,n_components):
        self.n_componenets = n_components
        self.mean =None
        self.coponents = None


    def fit(self,X):
        #ean
        self.mean = np.mean(X,axis=0)
        X=X-self.mean

        #cov
        
        cov= np.cov(X.T)
        #eigenvect, vals
        eigenvalues, eigenvectors = np.lonalg.eig(cov)
        
        #sort
        eigenvectors = eigenvectors.T
        idxs=np.argsort(eigenvalues)[::-1]
        eigenvalues =eigenvalues[idxs]
        eigenvectors =eigenvectors[idxs]
        #store first n
        self.coponents = eigenvectors[0:self.n_coponents]

    def transform(self,X):
        X=X-self.mean
        return np.dot(X, self.coponents.T)
