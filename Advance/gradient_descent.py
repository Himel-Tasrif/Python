import numpy as np

# y = 2x + 3 that mean today we prove that m = 2 and c = 3

def gradient_descent(x,y):
    m = c = 0
    n = len(x)
    iteration = 1000
    learning_rate = 0.05
    for i in range(iteration):
        y_predicted = m*x + c
        # mean squre error(mse) = 1/n * sum(y' - (m*x + c))
        # now, for coef(m) we need to do derivation of mse , i mean d/dm(mse)
        dm = -2/n * sum(x * (y - y_predicted))
        dc = -2/n * sum(y - y_predicted)
        m = m - learning_rate * dm
        c = c - learning_rate * dc
        print(f"m = {m} and c = {c}")

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
gradient_descent(x,y)