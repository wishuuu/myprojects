import numpy as np
from functions import sigmoid, sigmoid_back, cost

class Net:
    def __init__(self, layers, rate):
        """inicjacja sieci

        Args:
            layers [array[dict['input','output']]]: [kazdy element tablicy jest slownikiem z polami input i output oznaczajacymi ilosc neuronow na wejsciu i wyjsciu kazdej warstwy]
            rate [float]: [predkosc uczenia sie sieci]
        """
        self.layers = []
        self.biases = []
        self.activations = []

        self.learning_rate = rate
        
        for i in range(len(layers)):
            self.layers.append(np.random.randn(layers[i]["output"], layers[i]["input"])* 0.1 + 0.001)
            self.biases.append(np.random.randn(layers[i]["output"], 1) * 0.1 + 0.001)
            self.activations.append("sig")

    def single_layer_forward(self, A_prev, idx):
        """oblicenie wyniku pojedynczej warstwy

        Args:
            A_prev [np.array]: [tablica numpy zawierajaca input warstwy]
            idx [int]: [indeks warstwy]

        Returns:
            [np.array]: [wynik funkcji po zastosowaniu funkcji aktywacji]
            [np.array]: [wynik funkcji przed zastosowaniem funkcji aktywacji]
        """
        Z_curr = np.dot(self.layers[idx], A_prev) + self.biases[idx]

        act_func = sigmoid

        return act_func(Z_curr), Z_curr

    def full_forward(self, X):
        """obliczanie wyniku calej sieci

        Args:
            X [np.array]: [input sieci]

        Returns:
            [np.array]: [output sieci]
            [list[np.array]]: [historia outputow warstw po zastosowaniu funkcji aktywacji]
            [list[np.array]]: [historia outputow warstw przed zastosowaniem funkcji aktywacji]
        """
        A_hist = []
        Z_hist = []

        A_curr = X

        for idx in range(len(self.layers)):
            A_prev = A_curr

            A_curr, Z_curr = self.single_layer_forward(A_prev, idx)

            A_hist.append(A_prev)
            Z_hist.append(Z_curr)
            

        return A_curr, A_hist, Z_hist

    def single_layer_backward(self, dA_curr, Z_curr, A_prev, idx):
        """obliczenie gradientu pojedynczej warstwy

        Args:
            dA_curr [np.array]: [pochodna output warstwy dla ktorej jest obliczany gradient]
            Z_curr [np.array]: [output warstwy dla ktorej jest obliczany gradient przed uzyciem funkcji aktywacji]
            A_prev [np.array]: [input warstwy dla ktorej jest obliczany gradient po uzyciu funkcji aktywacji]
            idx [int]: [indeks warstwy dla ktorej jest obliczany gradien]

        Returns:
            [np.array]: [pochodna input warstwy dla ktorej jest obliczany gradient po uzyciu funkcji aktywacji]
            [np.array]: [gradient wag warstwy]
            [np.array]: [gradient bias warstwy]
        """
        m = A_prev.shape[1]

        back_func = sigmoid_back

        dZ_curr = back_func(dA_curr, Z_curr)
        dW_curr = np.dot(dZ_curr, A_prev.T) / m
        db_curr = np.sum(dZ_curr, axis=1, keepdims=True) / m
        dA_prev = np.dot(self.layers[idx].T, dZ_curr)

        return dA_prev, dW_curr, db_curr

    def full_backward(self, Y_pred, Y, A_hist, Z_hist):
        """obliczanie gradientu wszystkich warstw

        Args:
            Y_pred [np.array]: [output obliczony przez siec]
            Y [np.array]: [oczekiwany output sieci]
            A_hist [list[np.array]]: [historia outputow warstw po zastosowaniu funkcji aktywacji]
            Z_hist [list[np.array]]: [historia outputow warstw przed zastosowaniem funkcji aktywacji]

        Returns:
            [list[np.array]]: [tablica gradientow wag wszystkich warstw]
            [list[np.array]]: [tablica gradientow bias wszystkich warstw]
        """
        gradients_W = []
        gradients_b = []
        m = Y.shape[1]
        Y = Y.reshape(Y_pred.shape)

        dA_prev = - (np.divide(Y, Y_pred) - np.divide(1 - Y, 1 - Y_pred))

        for idx in reversed(range(len(self.layers))):     
            dA_curr = dA_prev

            A_prev = A_hist[idx]
            Z_curr = Z_hist[idx]
            W_curr = self.layers[idx]
            b_curr = self.biases[idx]

            dA_prev, dW_curr, db_curr = self.single_layer_backward(dA_curr, Z_curr, A_prev, idx)

            gradients_W.append(dW_curr)
            gradients_b.append(db_curr)

        gradients_W = gradients_W[::-1]
        gradients_b = gradients_b[::-1]

        return gradients_W, gradients_b

    def update(self, gradients_W, gradients_b):
        """funkcja zmieniajaca warstwy na podstawie obliczonych gradientow

        Args:
            gradients_W [list[np.array]]: [tablica gradientow wag wszystkich warstw]
            gradients_b [list[np.array]]: [tablica gradientow bias wszystkich warstw]
        """
        for idx, layer in enumerate(self.layers):
            layer -= gradients_W[idx] * self.learning_rate
        for idx, bias in enumerate(self.biases):
            bias -= gradients_b[idx] * self.learning_rate

    def train(self, X, Y):
        """funkcja trenujaca siec

        Args:
            X [np.array]: [input sieci]
            Y [np.array]: [oczekiwany output sieci]

        Returns:
            [np.array]: [laczny koszt (blad) sieci]
        """
        Y_pred, A_hist, Z_hist = self.full_forward(X)
        pred_cost = cost(Y_pred, Y)

        gradients_W, gradients_b = self.full_backward(Y_pred, Y, A_hist, Z_hist)
        self.update(gradients_W, gradients_b)

        return pred_cost

