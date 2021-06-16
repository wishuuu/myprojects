import pickle
import numpy as np
from sklearn.datasets import make_moons

import neural as NN
from functions import cost ,accuracy
import matplotlib.pyplot as plt

'''
Test sprawdzajacy czy utworzona siec jest w stanie klasyfikowac punkty wygenerowane przez dataset make_moon z biblioteki sklearn
'''

def train_and_save():
    X, y = make_moons(n_samples = 1000, noise = 0.2, random_state=100)

    X = X.reshape(-1, 2, 1)
    y = y.reshape(-1, 1, 1)

    layers = [  {'input':2, 'output':5},
                {'input':5, 'output':6},
                {'input':6, 'output':4},
                {'input':4, 'output':3},
                {'input':3, 'output':1},]

    Net = NN.Net(layers, 0.1)

    EPOCHS = 10000
    print_rate = 0.01

    for EPOCH in range(EPOCHS):
        for idx in range(len(X)):
            cost = Net.train(X[idx], y[idx])
        if EPOCH%(EPOCHS*print_rate) == 0:
            print(str(EPOCH), "/" + str(EPOCHS) +". Cost: " ,str(cost))
            print('y[0]:')
            print(y[0].reshape(1, -1))
            print('Output:')
            print(print(Net.full_forward(X[0])[0].reshape(1, -1)))
            print('Neurons:')
            print(Net.full_forward(X[0])[1][4].reshape(1, -1))
            print(Net.full_forward(X[0])[1][3].reshape(1, -1))
            print(Net.full_forward(X[0])[1][2].reshape(1, -1))
            print(Net.full_forward(X[0])[1][1].reshape(1, -1))
            print(Net.full_forward(X[0])[1][0].reshape(1, -1))
            print('--------------------------------')

    print(cost)

    with open('moon_net.pkl', 'wb') as output:
        pickle.dump(Net, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(X, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(y, output, pickle.HIGHEST_PROTOCOL)

def load_and_test():
    with open('moon_net.pkl', 'rb') as input:
        Net = pickle.load(input)
        X = pickle.load(input)
        y = pickle.load(input)

    cost_sum = 0
    acc = 0
    for idx in range(len(X)):
        pred = Net.full_forward(X[idx])[0]
        cost_sum += cost(pred, y[idx])
        if round(pred[0][0], 0) == y[idx][0][0]:
            acc += 1

    print('Cost: ' + str(cost_sum/len(X)))
    print('Accuracy: ' + str(acc/len(X)))

def load_and_visualize():
    with open('moon_net.pkl', 'rb') as input:
        Net = pickle.load(input)
        X = pickle.load(input)
        y = pickle.load(input)

    xplot = X[:,0].reshape(-1, 1)
    yplot = X[:,1].reshape(-1, 1)
    colors = y.reshape(-1, 1)

    plt.scatter(xplot, yplot, c=colors, cmap='coolwarm')
    plt.show()

    
# uwaga trening sieci dla podanych paremetrów może zająć dużo czasu
# w pliku już zapisana jest wytrenowana sieć

#train_and_save()
load_and_visualize()
load_and_test()