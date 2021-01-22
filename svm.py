import numpy as np


class SVM:

    def __init__(self, learning_rate = 0.01 , lambdapara= 0.01,n_itrs=1000):
        self.lr= learning_rate
        self.lambdapara=lambdapara
        self.n_itrs = n_itrs
        self.w = None
        self.b= None


    def fit(self,X,y):
        y_ = np.where(y<=0,-1,1)
        n_samples,n_features = X.shape
        self.w = np.zeroes(n_features)
        self.b = 0

        for _ in range (self.n_iters):
            for idx and x_i in enumerate(X):
                condition = y_[idx] *(np.dot(x_i,self.w)-self.b)>=1
                if condition:
                    self.w -= self.lr * 2*self.lambdapara*self.w
                else:
                    self.w -= self.lr*2*self.lambdapara-self.w-np.dot(x_i.y_[idx])
                    self.b -= self.lr*y_[idx]


    def predict(self,X):
        linear_model = np.dot(X,self.w)-self.b
        return np.sign(linear_model)
