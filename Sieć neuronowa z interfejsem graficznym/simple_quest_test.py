import numpy as np

import neural as NN

'''
Test sprawdzajacy czy utworzona siec jest w stanie poradzić sobie z bardzo łatwym zadaniem
'''

layers = [  {'input':2, 'output':2},
            {'input':2, 'output':2}]


Net = NN.Net(layers, 0.1)

input1 = np.array([[0.4], [0.5]])
input2 = np.array([[0.3], [0.6]])

target1 = np.array([[0], [1]])
target2 = np.array([[1], [0]])

for i in range(10000):
    cost1 = Net.train(input1, target1)
    cost2 = Net.train(input2, target2)

print("Output 1:")
print(Net.full_forward(input1)[0])
print("Output 2:")
print(Net.full_forward(input2)[0])
print("Cost 1:")
print(cost1)
print("Cost 2:")
print(cost2)