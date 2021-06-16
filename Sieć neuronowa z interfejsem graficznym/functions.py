import numpy as np


def sigmoid(Z):
    return 1/(1 + np.exp(-Z))


def sigmoid_back(dA, Z):
    sig = sigmoid(Z)
    return dA * sig * (1 - sig)

def cost(Y_pred, Y):
    m = Y_pred.shape[1]
    cost = -1 / m * (np.dot(Y.T, np.log(Y_pred)) + np.dot(1 - Y.T, np.log(1 - Y_pred)))
    return np.squeeze(cost)

def accuracy(Y_pred, Y):
    return np.argmax(Y_pred) == np.argmax(Y)

def one_hot_to_index(vector):
    return np.argmax(vector)

def index_to_one_hot(index, size):
    output = np.zeros(1, size)
    output[index] = 1
    return output

def normalization(input, f):
    for i in range(len(input)):
        input[i] = f(input[i])
    return input