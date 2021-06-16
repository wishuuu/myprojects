import numpy as np
import random

def split_data(X, y):
    X_test = []
    X_train = []
    y_test = []
    y_train = []

    for idx, label in enumerate(X):
        if idx%10 == 0:
            X_test.append(label)
        else:
            X_train.append(label)

    for idx, label in enumerate(y):
        if idx%10 == 0:
            y_test.append(label)
        else:
            y_train.append(label)

    return X_train, y_train, X_test, y_test


f = open("data/iris.txt", 'r')
line = f.readline()

X = []
y = []

while line != "":
    data = line.split(sep = ",")
    X.append(data[0:4])
    if data[-1] == "Iris-setosa\n":
        y.append(['1','0','0'])
    elif data[-1] == "Iris-versicolor\n":
        y.append(['0','1','0'])
    elif data[-1] == "Iris-virginica\n":
        y.append(['0','0','1'])
    line = f.readline()

f.close()

    
X_train, y_train, X_test, y_test = split_data(X, y)

f_train = open("data/train.txt", 'w')
f_test = open("data/test.txt", 'w')

for i in range(len(X_train)):
    f_train.write(X_train[i][0]+','+X_train[i][1]+','+X_train[i][2]+','+X_train[i][3]+';')
    f_train.write(y_train[i][0]+','+y_train[i][1]+','+y_train[i][2]+'\n')

for i in range(len(X_test)):
    f_test.write(X_test[i][0]+','+X_test[i][1]+','+X_test[i][2]+','+X_test[i][3]+';')
    f_test.write(y_test[i][0]+','+y_test[i][1]+','+y_test[i][2]+'\n')


f_train.close()
f_test.close()