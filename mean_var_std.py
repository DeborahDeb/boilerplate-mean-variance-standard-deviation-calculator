import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    ls = np.array(list)
    ma = ls.reshape((3,3))

    mean = [ma.mean(axis=0).tolist(), ma.mean(axis=1).tolist(), ls.mean().tolist()]
    var = [ma.var(axis=0).tolist(), ma.var(axis=1).tolist(), ls.var().tolist()]
    std = [ma.std(axis=0).tolist(), ma.std(axis=1).tolist(), ls.std().tolist()]
    max_val = [ma.max(axis=0).tolist(), ma.max(axis=1).tolist(), ls.max().tolist()]
    min_val = [ma.min(axis=0).tolist(), ma.min(axis=1).tolist(), ls.min().tolist()]
    sum_val = [ma.sum(axis=0).tolist(), ma.sum(axis=1).tolist(), ls.sum().tolist()]

    return {
        'mean': mean,
        'variance': var,
        'standard deviation': std,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }

if __name__ == "__main__":
    print(calculate([0,1,2,3,4,5,6,7,8]))
