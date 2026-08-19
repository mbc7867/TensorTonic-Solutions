import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x_arr = np.asarray(x, dtype=float)
    x_mean = np.mean(x)
    n = len(x_arr)
    var_sum = 0
    if n < 2:
        raise ValueError("Need at least 2 samples for t-test")
    for i in range(n):
        var_sum += (x_arr[i] - x_mean)**2
    s = np.sqrt(var_sum/(n-1))

    t_stat = (x_mean - mu0)*np.sqrt(n)/s
    return float(t_stat)