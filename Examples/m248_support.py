
def get_y_mean(x_mean: float, a: float, b: float = 0) -> float:
    """
    Returns the mean E(X) of Y=aX+b, where X is some other rv.
    """
    return a * x_mean + b


def get_y_var(x_var: float, a: float) -> float:
    """
    Returns the variance V(Y) of Y=aX+b, where X is some other rv.
    """
    return a ** 2 * x_var


def get_z_from_x(x: float, mean: float, std: float) -> float:
    """
    Returns the value of the standard normal variable z, given a value for x
    with known mean and std for x.

    Return value is to 2dp (to support studies in M248)
    """
    return round((x-mean) / std, 2)


def get_x_from_a(a: float, mean: float, std: float) -> float:
    """
    Returns the value of a normal variable x with known mean and std for x, 
    and the a-quantile value for standard normal variable z.

    Return value is to 2dp (to support studies in M248)
    """
    return round(std * a + mean, 3)
