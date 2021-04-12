from math import sqrt
from scipy.stats import t


def get_two_sample_t_interval(alpha: float, a, b):
    """
    Calculates an exact CI for the difference between two means, d=a-b.

    a and b should be pd.DataFrame columns or Series, or np.arrays.
    """

    n1 = a.dropna().size  # size of a
    n2 = b.dropna().size  # size of b

    pooled_var = (((n1-1)*a.var(ddof=1) + (n2-1)*b.var(ddof=1))
                  / (n1+n2-2))

    t_scale = sqrt(pooled_var*(1/n1 + 1/n2))

    return t(df=n1+n2-2,
             loc=a.mean() - b.mean(),
             scale=t_scale).interval(alpha=alpha)
