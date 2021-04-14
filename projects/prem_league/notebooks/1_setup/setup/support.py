

def add_bandings_poisson_proc(x: int) -> str:
    """
    Returns banding of X, defined as the nearest multiple of 10.

    -  If x > 90, then set x to 90.
    -  Else if x is 0, then set x to 10.
    -  Otherwise, while the remainder of x/10 is not 0, increment
    x by 1.

    @param, x, int
        an integer representing the waiting time before a goal is
        scored.

    @return, int
        the nearest greater multiple of 10
    """

    if (x >= 90):
        x = "90+"
    elif (x == 0):
        x = "10"
    else:
        while (x % 10 != 0):
            x += 1
        x = str(x)

    return x


def add_bandings_uniform_goals(x: int) -> str:
    """
    Returns banding of X, defined as the nearest multiple of 10.

    -  If x is 0, then set x to 10.
    -  Otherwise, while the remainder of x/10 is not 0, increment
    x by 1.

    @param, x, int
        an integer representing the waiting time before a goal is
        scored.

    @return, int
        the nearest greater multiple of 10
    """

    if (x == 0):
        x = "10"
    else:
        while (x % 10 != 0):
            x += 1
        x = str(x)

    return x
