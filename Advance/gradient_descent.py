# Name : Tasrif Nur Himel

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

        cost = 1/n * sum((y - y_predicted) * (y - y_predicted))
        #cost = 1/n * sum([val**2 for val in (y - y_predicted)])
        dm = -2/n * sum(x * (y - y_predicted)) # by doing d/dm(mse)
        dc = -2/n * sum(y - y_predicted) # by doing d/dc(mse)
        m = m - learning_rate * dm
        c = c - learning_rate * dc
        print(f"m = {m} --- c = {c}, Cost = {cost}")

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
gradient_descent(x,y)