#Tasrif Nur Himel

# Mean Squre Error:
# 1/n sum(y-y')^2

import numpy as np
# if manual
y_pred = np.array([1,1,0,0,1])
y_true = np.array([0.30,0.7,1,0,0.5])

def _mean(y_pred, y_true):
    total_error = 0
    for yp, yt in zip(y_pred, y_true):
        print(yt,yp)

        total_error += (yt - yp)*(yt - yp)

    print(f'Total Squred Error: {total_error}')

    m = total_error / len(y_true)

    print(f'Mean Squre Error is: {m}')



_mean(y_pred, y_true)

# If Using Numpy

print(f'By Using Numpy---- Mean Squre Error: {np.mean(np.square(y_true - y_pred))}')