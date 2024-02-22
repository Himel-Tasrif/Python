# Tasrif Nur Himel

# Implement Log Loss or Binary Cross Entropy

# -1/n sum(ylog(y') + ((1-y)log(1-y'))

import numpy as np
y_pred = np.array([1,1,0,0,1])
y_true = np.array([0.30,0.7,1,0,0.5])
epsilon = 1e-15

def log_loss(y_pred, y_true):

    new_y_pred = [max(i,epsilon)for i in y_pred]
    new_y_pred1 = [min(i,1-epsilon)for i in new_y_pred]
    new_y_pred2 = np.array(new_y_pred1)

    return -np.mean(y_true*np.log(new_y_pred2) + ((1-y_true)*np.log(1-new_y_pred2)))


print(f'The Log Loss or Binary Cross Entropy is : {log_loss(y_pred, y_true)}')