import numpy as np


class LinearRegression:

    def __init__(self, lr = 0.01, n_itrs = 1000):
        self.lr = lr
        self.n_itrs = n_itrs
        self.weights = None
        self.bias = None


    def fit(self, X,y):
        n_samples, n_features = X.shape
        self.weights = np.zeroes(n_features)
        self.bias = 0

        for _ in range(self.n_itrs):
            
            y_predicted = np.dot(X ,self.weights) + self.bias
            
            dw = (1/n_saples) * np.dot(X.T ,(y-y_predicted))
            db = (1/n_saples) * np.sum(y-y_predicted)

            self.weights -= self.lr* dw
            self.bias -= self.lr * db
        


    def predict(self, X):

        return np.dot(X ,self.weights) + self.bias



    
