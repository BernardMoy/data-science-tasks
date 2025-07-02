import numpy as np

def calculate(list):
    if len(list) < 9: 
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array([np.array(list[n:n+3]) for n in range(0, 9, 3)])
    calculations = {} 

    # Find mean 
    mean_axis_1 = np.mean(matrix, axis = 0)
    mean_axis_2 = np.mean(matrix, axis = 1)
    calculations['mean'] = [mean_axis_1.tolist(), mean_axis_2.tolist(), np.mean(matrix)]

    # Find variance 
    var_axis_1 = np.var(matrix, axis = 0) 
    var_axis_2 = np.var(matrix, axis = 1)
    calculations['variance'] = [var_axis_1.tolist(), var_axis_2.tolist(), np.var(matrix)]

    # Find standard d
    std_axis_1 = np.std(matrix, axis = 0) 
    std_axis_2 = np.std(matrix, axis = 1)
    calculations['standard deviation'] = [std_axis_1.tolist(), std_axis_2.tolist(), np.std(matrix)]

    # Find max min 
    max_axis_1 = np.max(matrix, axis = 0) 
    max_axis_2 = np.max(matrix, axis = 1)
    calculations['max'] = [max_axis_1.tolist(), max_axis_2.tolist(), np.max(matrix)]

    min_axis_1 = np.min(matrix, axis = 0) 
    min_axis_2 = np.min(matrix, axis = 1)
    calculations['min'] = [min_axis_1.tolist(), min_axis_2.tolist(), np.min(matrix)]

    sum_axis_1 = np.sum(matrix, axis = 0) 
    sum_axis_2 = np.sum(matrix, axis = 1)
    calculations['sum'] = [sum_axis_1.tolist(), sum_axis_2.tolist(), np.sum(matrix)]

    # Return final result 
    return calculations