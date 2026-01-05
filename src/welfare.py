import numpy as np

def utility(E):
    return np.log(E)

def cdr_cost(R, phi):
    return 0.5 * phi * R**2
