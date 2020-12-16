
class cts_rv(object):
    """
    A class that models the probability distribustion of a continuous rv.
    """

    # instance variables
    f: object
    a: float
    b: float

    def __init__(self, pdf: object, lower: float, upper: float) -> None:
        """
        Constructor for a continuous random variable.
        """
        self.f = pdf  # the p.d.f
        self.a = lower  # the lower bound a X
        self.b = upper  # the upper bound of X

    """-----------------------------------------------------------------------
    Getters
    -----------------------------------------------------------------------"""

    def get_f(self) -> None:
        """
        Getter for variable f
        """

        return self.f

    def get_a(self) -> None:
        """
        Getter for variable a, the minimum of X
        """

        return self.a

    def get_b(self) -> None:
        """
        Getter for variable b, the maximum of X
        """

        return self.b

    """-----------------------------------------------------------------------
    Public methods
    -----------------------------------------------------------------------"""

    def hasProbability(self, x1: float, x2: float) -> float:
        """
        Calculates P(x1 < X < x2). Both x1 and x2 should be defined.

        If P(X < x), then pass x1 as the minium of X.
        Else if P(X > x)
        """
