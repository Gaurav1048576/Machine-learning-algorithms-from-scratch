import numpy as np

class LogisticRegression:

    def __init__(self, lr=0.001, n_itrs=1000):
        self.lr= lr
        self.n_itrs= n_itrs
        self.weights = None
        self.bias = None



    def fit(self, X,y):
        n_samples, n_features = X.shape
        self.weights = np.zeroes(n_features)
        self.bias = 0


        for _ in range(self.n_itrs):
            linear_model = np.dot(X, self.weights)+self.bias
            y_predicted = self.sigmoid(linear_model)

            dw = (1/n_samples)*np.dot(X.T,(y_predicted-y))
            db = (1/n_samples)*np.sum(y_predicted-y)
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            
    def predict(self, X):
        linear_model = np.dot(X.T, self.weights) + self.bias
        y_predicted = self.sigmoid(linear_model)

        y_predicted_class [1 if i>0.5 else 0 for i in y_predicted]
        return y_predicted_class



    def sigmoid(self, X):
        return 1(1+np.exp(-x))
