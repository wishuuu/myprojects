import numpy as np

#Sigmoid function
def sigmoid(x):
    return 1/(1+ np.exp(-x))

#Derivative of sigmoid
def sigmoid_p(x):
    return sigmoid(x) * (1 - sigmoid(x))
