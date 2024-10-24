import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    calc_array = np.array(list).reshape((3, 3))
    calculations = {"mean": [
        calc_array.mean(axis=0).tolist(),
        calc_array.mean(axis=1).tolist(),
        np.mean(calc_array).tolist()
    ], "variance": [
        (calc_array.var(axis=0).tolist()),
        (calc_array.var(axis=1).tolist()),
        (np.var(calc_array).tolist())
    ], "standard deviation": [
        (calc_array.std(axis=0).tolist()),
        (calc_array.std(axis=1).tolist()),
        (np.std(calc_array).tolist())
    ], "max": [
        (calc_array.max(axis=0).tolist()),
        (calc_array.max(axis=1).tolist()),
        (np.max(calc_array).tolist())
    ], "min": [
        (calc_array.min(axis=0).tolist()),
        (calc_array.min(axis=1).tolist()),
        (np.min(calc_array).tolist())
    ], "sum": [
        (calc_array.sum(axis=0).tolist()),
        (calc_array.sum(axis=1).tolist()),
        (np.sum(calc_array).tolist())
    ]}

    return calculations
