#Tasrif Nur Himel
# 1/n sum(y-y')^2

import numpy as np

y_pred = np.array([1,1,0,0,1])
y_true = np.array([0.30,0.7,1,0,0.5])

def _mean(y_pred, y_true):
    total_error = 0
    for yp, yt in zip(y_pred, y_true):
        print(yt,yp)

        total_error += (yt - yp)*(yt - yp)
    m = total_error / len(y_true)

    print(f'Mean Squre Error is: {m}')



_mean(y_pred, y_true)