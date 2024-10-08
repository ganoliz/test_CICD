import numpy as np


def sum_array(_x: np.ndarray, _y: np.ndarray) -> np.ndarray:
    """
    This function take input _x and _y and returns its sum.
    :param _x:
    :param _y:
    :return:
    """
    return _x + _y


a = np.ones((2, 2))
b = np.ones((2, 2)) + 3

print(sum_array(a, b))
