import numpy as np

def calculate(list):
    list_matrix = np.array(list).reshape(3,3)
    calculations = {
      'mean': [np.mean(list_matrix, axis=0), np.mean(list_matrix, axis=1), 
       np.mean(list_matrix)],
      'variance': [np.var(list_matrix, axis=0), np.var(list_matrix, axis=1), 
       np.var(list_matrix)],
      'standard deviation': [np.std(list_matrix, axis=0), np.std(list_matrix, axis=1),                np.std(list_matrix)],
      'max': [np.max(list_matrix, axis=0), np.max(list_matrix, axis=1), np.max(list_matrix)],
      'min': [np.min(list_matrix, axis=0), np.min(list_matrix, axis=1), np.min(list_matrix)],
      'sum': [np.sum(list_matrix, axis=0), np.sum(list_matrix, axis=1), np.sum(list_matrix)]
    } 

    return calculations