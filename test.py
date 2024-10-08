import numpy as np
import pandas as pd

def sum(a, b):
    return a+b

a = np.ones((2, 2))
b = np.ones((2, 2)) + 3

print(sum(a, b))