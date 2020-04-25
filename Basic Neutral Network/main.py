import numpy as np
from model1 import NN
from functions import sigmoid
from functions import sigmoid_p

def generate_numbers(x, y1, y2):
    X1 = np.random.random(x) * y1
    X2 = np.random.random(x) * y1
    X1 = np.append(X1, np.random.random(x) * y2)
    X2 = np.append(X2, np.random.random(x) * y2)
    y1 = np.append(np.zeros(x), np.ones(x))
    return X1, X2, y1

X1, X2, y1 = generate_numbers(10, 2, 7)

print([[X1[i], X2[i], y1[i]] for i in range(X1.shape[0])])

model = NN(0.1)
for j in range(10000):
    for i in range(X1.shape[0]):
        model.train(X1[i], X2[i], y1[i])

for i in range(X1.shape[0]):
    print(model.error(model.output(X1[i], X2[i])), y1[i]))
