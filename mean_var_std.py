import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError ('List must contain nine numbers.')

  else:
    list_matrix = np.array(list).reshape(3,3)
    calculations = {
      'mean': [np.mean(list_matrix, axis=0).tolist(), np.mean(list_matrix, axis=1).tolist(), 
       np.mean(list_matrix).tolist()],
      'variance': [np.var(list_matrix, axis=0).tolist(), np.var(list_matrix, axis=1).tolist(), 
       np.var(list_matrix).tolist()],
      'standard deviation': [np.std(list_matrix, axis=0).tolist(), np.std(list_matrix, axis=1).tolist(),np.std(list_matrix).tolist()],
      'max': [np.max(list_matrix, axis=0).tolist(), np.max(list_matrix, axis=1).tolist(), np.max(list_matrix)],
      'min': [np.min(list_matrix, axis=0).tolist(), np.min(list_matrix, axis=1).tolist(), np.min(list_matrix)],
      'sum': [np.sum(list_matrix, axis=0).tolist(), np.sum(list_matrix, axis=1).tolist(), np.sum(list_matrix)]
    } 

    return calculations