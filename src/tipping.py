import numpy as np

def hazard(C, h0, gamma):
    return h0 * np.exp(gamma * C)
