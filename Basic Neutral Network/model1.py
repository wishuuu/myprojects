import numpy as np
from functions import sigmoid
from functions import sigmoid_p
#Neural network class
class NN():
    def __init__(self, rate):
        self.w1 = np.random.randn()
        self.w2 = np.random.randn()
        self.b1 = np.random.randn()

        self.learnig_rate = rate

    #Calculates value in range(-inf, inf) for given input
    def calc(self, x1, x2):
        return x1*self.w1 + x2*self.w2 + self.b1

    def error(self, pred, targ):
        return (pred - targ) ** 2

    def error_p(self, pred, targ):
        return 2 * (pred - targ)

    #Calculates value for given input and returns it in range (-1, 1)
    def output(self, x1, x2):
        return sigmoid(calc(x1, x2))

    def train(self, x1, x2, targ):
        network_output = self.calc(x1, x2)
        pred = sigmoid(network_output)
        error = self.error(pred, targ)

        derror_pred = self.error_p(pred, targ)
        dpred_doutput = sigmoid_p(network_output)

        doutput_dw1 = x1
        doutput_dw2 = x2
        doutput_db = 1

        derror_dw1 = derror_pred * dpred_doutput * doutput_dw1
        derror_dw2 = derror_pred * dpred_doutput * doutput_dw2
        derror_db = derror_pred * dpred_doutput * doutput_db

        self.w1 = self.w1 - self.learnig_rate * derror_dw1
        self.w2 = self.w2 - self.learnig_rate * derror_dw2
        self.b1 = self.b1 - self.learnig_rate * derror_db
