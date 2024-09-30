import numpy as np

def calculate(list):
    # We check the lenght of the list. If it has not 9 elements, we raise an error message.
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # We convert list into a 3x3 matrix and store it in a variable. Also, we store that matrix flattered.    
    matrix = np.array(list).reshape(3,3)
    fl_matrix = matrix.flatten()

    # We make the calculations.
    a0_mean = matrix.mean(axis=0)
    a0_variance = matrix.var(axis=0)
    a0_std_dev = matrix.std(axis=0)
    a0_max = matrix.max(axis=0)
    a0_min = matrix.min(axis=0)
    a0_sum = matrix.sum(axis=0)

    a1_mean = matrix.mean(axis=1)
    a1_variance = matrix.var(axis=1)
    a1_std_dev = matrix.std(axis=1)
    a1_max = matrix.max(axis=1)
    a1_min = matrix.min(axis=1)
    a1_sum = matrix.sum(axis=1)
    
    fl_mean = fl_matrix.mean()   
    fl_variance = fl_matrix.var()
    fl_std_dev = fl_matrix.std()
    fl_max = fl_matrix.max()
    fl_min = fl_matrix.min()
    fl_sum = fl_matrix.sum()

    # We save all the calculations into a dictionary. As the values are stored as an array, we pass them to a list with Numpy's tolist() function.
    calculations = {
        'mean': [a0_mean.tolist(), a1_mean.tolist(), fl_mean.tolist()],
        'variance': [a0_variance.tolist(), a1_variance.tolist(), fl_variance.tolist()],
        'standard deviation': [a0_std_dev.tolist(), a1_std_dev.tolist(), fl_std_dev.tolist()],
        'max': [a0_max.tolist(), a1_max.tolist(), fl_max.tolist()],
        'min': [a0_min.tolist(), a1_min.tolist(), fl_min.tolist()],
        'sum': [a0_sum.tolist(), a1_sum.tolist(), fl_sum.tolist()]
    }
    return calculations