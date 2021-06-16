import neural as NN
from functions import normalization, one_hot_to_index, cost, accuracy

import numpy as np

def create_net(layers, learning_rate):
    return NN.Net(layers, learning_rate)

def load_data(path):
    f_test = open(path)

    lines = f_test.readlines()
    np.random.shuffle(lines)

    X = []
    y = []

    for line in lines:
        data = line.split(';')
        X.append(data[0].split(','))
        y.append(data[1].split(','))

    X = np.array(X)
    y = np.array(y)

    X = X.astype(np.float)
    y = y.astype(np.float)

    X = X.reshape(-1, X.shape[-1], 1)
    y = y.reshape(-1, y.shape[-1], 1)

    return X, y

def train(Net, X_train, y_train, EPOCHS = 1000):
    for EPOCH in range(EPOCHS):
        flag = 1
        for idx in range(len(X_train)):
            Net.train(X_train[idx], y_train[idx])
            if EPOCH % (EPOCHS/100) == 0 and flag:
                print(str(EPOCH / (EPOCHS/100)) + '%')
                flag = 0

def test(Net, X_test, y_test):
    avr_cost = 0
    acc = 0
    for idx in range(len(X_test)):
        pred = Net.full_forward(X_test[idx])[0]
        avr_cost += cost(pred, y_test[idx])
        acc += accuracy(pred, y_test[idx])
    return avr_cost / len(X_test), acc / len(X_test)