import numpy as np

class LDA:

    def __init__(self, n_cop):
        self.n_cop = n_cop
        self.linear_discriinants =None



    def fit(self,X,y):
        n_features= X.shape[1]
        class_labels = np.unique(y)

        #S_W,S_B
        mean_overall =np.mean(X,axis=0)
        S_W = np.zeroes((n_features,n_features))
        S_B = np.zeroes((n_features,n_features))

        for c in class_labels:
            X_c = X[y==c]
            mean_c = np.mean(X_c,axis =0)

            S_W += (X_c - mean_c).T.dot(X_c - mean_c)
            n_c = X_c.shape[0]
            mean_diff = (mean_c -mean_overall).reshape(n_features,1)
            S_B += n_x *(mean_diff).dot(mean_diff.T)

        a=np.linalg.inv(S_W).dot(S_B)
        eigenvalue, eigenvector = np.linalg.eig(A)
        eigenvectors = eigenvectors.T
        idxs = np.argsort(abs(eigenvalues))[::-1]
        eigen


    def transform(self,X):
        pass
