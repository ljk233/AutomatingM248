
from __future__ import annotations
from typing import Any
from math import trunc, sqrt
from scipy.stats import norm
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class Solution:
    """
    Class to model the solution.
    """

    def __init__(self) -> None:
        """
        Cnstructs a new instance of type Solution.
        Initates var `soln` to an empty dict and `soln_str` to
        `"Solution:"`
        """

        self._soln: dict = dict()
        self._soln_str: str = "Soln{"

    def __str__(self) -> str:
        """
        Returns a string representation of the receiver's soln for
        printing. Solution is rounded to 6dp.
        """

        soln_builder: str = ""

        for k in self._soln.keys():
            soln_builder = self._conc(soln_builder, k, self._soln[k])

        self._soln_str = self._soln_str + soln_builder + "\n}"

        return self._soln_str

    def _conc(self, s1: str, s2: str, s3: str) -> str:
        """
        Concatenates the three args as a string.
        """

        join: str = ""

        # is this the first solution in the str to return?
        if "=" not in s1:
            join = "\n    "
        else:
            join = ",\n    "

        return s1 + join + s2 + "=" + str(s3)

    def _truncate(self, x) -> float:
        """
        Returns argument x truncated to 6dp. There is no rounding.
        """
        stepper = 10.0 ** 6
        return trunc(stepper * x) / stepper

    def update(self, name: str, answer) -> None:
        """
        Adds args name, answer as a k, v to receiver's soln.
        """

        self._soln[name] = self._truncate(answer)

    def no_trunc_update(self, name: str, answer) -> None:
        """
        Adds args name, answer as a k, v to receiver's soln.
        """

        self._soln[name] = answer


class Discrete():
    """
    Models a discrete random variable.
    """

    def __init__(self, x: list[int], pr: list[float]) -> None:
        """
        Constructor for objects of type Discrete.
        Assigns var k=x, v=pr to dictionary var _fn, and assigns var
        _soln to an empty dictionary.

        @params
        =======
        `x`
            A list of integers that represents the range of X.

        `pr`
            A list of floats that represents the Pr(X = x). Element
            `pr[i]` should correspond to the event Pr(X=`x[i]`).
        """

        self._soln: dict = dict()
        self._fn: dict = dict()

        ix: int = 0  # counter variable

        while (ix < len(x)):
            self._fn[x[ix]] = pr[ix]
            ix += 1

        # @properties

        # instance methods

    # static methods

    def parse_pr_range(geq_x1: str, leq_x2: str) -> None:
        """
        Static method. Parses a probablity range, printing the cdfs
        that need to be used to calculate the probability.

        @params
        `geq_x1`
            boolean, is the first inequality Pr(x1<=X ...)?

        `leq_x2`
            boolean, is the second inequality Pr(... X<=x2)?
        """

        x1: str = "x1"
        x2: str = "x2"
        ineq1: str = "<"
        ineq2: str = "<="

        # parse ineq1:
        if (geq_x1):
            x1 = "{x1}-1"
            ineq1 = "<="

        if (not leq_x2):
            x2 = "{x2}-1"
            ineq2 = "<"

        print(f"P(x1{ineq1}X{ineq2}x2)=F({x2})-F({x1})")

    # instance methods

    def pmf(self, k: int, to_printer: bool = True) -> Any:
        """
        Calculates the Pr(X=k). If arg `x` is not in the range of X,
        then returns None. If arg `to_printer` is True, then prints the
        solution to the screen. Otherwise returns the answer as a float.

        @params
        =======
        `k`
            Integer in the range of X.

        `to_printer`
            Whether to print the answer to the screen, or return a
            float. Default is True.

        @returns
        ========
            `None` or float.
        """

        if k not in self._fn.keys():
            print(f"Error: {k} is not in the range of X")
            return None

        # create new solution object
        soln: Solution = Solution()

        soln.update(name=f"P(X={k})", answer=self._fn[k])

        if to_printer:
            print(soln)
        else:
            return self._fn[k]

    def cdf(self, x: int, to_printer: bool = True) -> Any:
        """
        Calculates the Pr(X <= x). If arg `to_printer` is True, then
        prints the solution to the screen. Otherwise returns the answer
        as a float.

        @params
        =======
        `x`
            Integer in the range of X.

        `to_printer`
            Whether to print the answer to the screen, or return a
            float. Default is True.

        @returns
        ========
            `None` or float.
        """

        # create new solution object
        soln: Solution = Solution()

        F: float = 0

        for i in self._fn.keys():
            if (i <= x):
                F += self.pmf(i, to_printer=False)
            else:
                break

        soln.update(name=f"Pr(X<={x})", answer=F)

        if to_printer:
            print(soln)
        else:
            return F

    def sf(self, x: int, to_printer: bool = True) -> Any:
        """
        Calculates the Pr(X > x). If arg `to_printer` is True, then
        prints the solution to the screen. Otherwise returns the answer
        as a float.

        @params
        =======
        `x`
            Integer in the range of X.

        `to_printer`
            Whether to print the answer to the screen, or return a
            float. Default is True.

        @returns
        ========
            `None` or float.
        """

        # create new solution object
        soln: Solution = Solution()

        pr: float = 1 - self.cdf(x, to_printer=False)

        soln.update(name=f"Pr(X>{x})", answer=pr)

        if to_printer:
            print(soln)
        else:
            return pr

    def mean(self, to_printer: bool = True) -> Any:
        """
        Calculates E(X). If arg to_printer is True, then prints the
        solution to the screen. Otherwise returns the answer as a float.

        @returns
        ========
            `None` or float.
        """
        # create new solution object
        soln: Solution = Solution()

        mean: float = 0

        for i in self._fn.keys():
            mean = mean + (i * self.pmf(i, to_printer=False))

        # update soln
        soln.update("E(X)", mean)

        if to_printer:
            print(soln)
        else:
            return mean

    def mean_sq(self, to_printer: bool = True) -> Any:
        """
        Calculates E(X2). If arg to_printer is True, then prints the
        solution to the screen. Otherwise returns the answer as a
        float.

        @returns
        ========
            `None` or float.
        """
        # create new solution object
        soln: Solution = Solution()

        mean_sq: float = 0

        for i in self._fn.keys():
            mean_sq = mean_sq + (i**2 * self.pmf(i, to_printer=False))

        # update soln
        soln.update("E(X2)", mean_sq)

        if to_printer:
            print(soln)
        else:
            return mean_sq

    def var(self, to_printer: bool = True) -> Any:
        """
        Calculates V(X). If arg to_printer is True, then prints the
        solution to the screen. Otherwise returns the answer as a float.

        @returns
        ========
            `None` or float.
        """

        # create new solution object
        soln: Solution = Solution()

        mean_sq: float = self.mean_sq(to_printer=False)
        sq_mean: float = self.mean(to_printer=False)**2

        var: float = mean_sq - sq_mean

        # update soln
        soln.update("E(X2)", mean_sq)
        soln.update("mu2", sq_mean)
        soln.update("V(X)", var)

        if to_printer:
            print(soln)
        else:
            return var

    def std(self, to_printer: bool = True) -> Any:
        """
        Calculates S(X). If arg to_printer is True, then prints the
        solution to the screen. Otherwise returns the answer as a float.

        @returns
        ========
            `None` or float
        """

        # create new solution object
        soln: Solution = Solution()

        mean_sq: float = self.mean_sq(to_printer=False)
        sq_mean: float = self.mean(to_printer=False)**2
        var: float = self.var(to_printer=False)

        try:
            std: float = sqrt(var)
        except ValueError:
            print(f"Error: V(X)={round(var, 6)} is negative!")
            return None

        # update soln
        soln.update("E(X2)", mean_sq)
        soln.update("mu2", sq_mean)
        soln.update("V(X)", var)
        soln.update("S(X)", std)

        if to_printer:
            print(soln)
        else:
            return var

    def is_valid(self) -> None:
        """
        Prints a str describing if the PMF of X is a valid probability
        function.

        There are two check: Checks if sum(Pr) = 1 and whether all
        Pr(X) in (0,1].
        """

        # create new solution object
        soln: Solution = Solution()

        # find max(X)
        upper: int = max(list(self._fn.keys()))

        # get sum(Pr)
        sum_pr: float = self.cdf(x=upper, to_printer=False)
        is_one: float = sum_pr == 1.0

        # is Pr in range?
        in_range: bool = True

        for k in self._fn.keys():
            pr: float = self.pmf(k, to_printer=False)
            if (pr <= 0 or pr > 1):
                in_range = False
                break

        soln.no_trunc_update("is valid", is_one and in_range)

        if not is_one:
            soln.update("sum(Pr)", sum_pr)
        if not in_range:
            soln.update(f"Pr(X={k})", pr)

        print(soln)

    def quantile(self, a: float, to_printer: bool = True) -> None:
        """
        Calculates q_{a}. If arg to_printer is True, then prints the
        solution to the screen. Otherwise returns the answer as a float.

        @returns
        ========
            `None` or float
        """

        # create new solution object
        soln: Solution = Solution()

        for x in self._fn.keys():
            if self.cdf(x, to_printer=False) >= a:
                break

        # update soln
        soln.update("x", x)

        if to_printer:
            print(soln)
        else:
            return x


class StandardNormal():
    """
    A concenience class of static methods that helps to model the
    standard normal probability distribution N(0,1).
    The answers are rounded to the same level of accuracy as those
    given in the tables at the back of the handbook.
    """

    dist: norm = norm(0, 1)

    def cdf(z: float) -> float:
        """
        Returns the phi(z) of the standard normal distribuition rounded
        to 4dp.
        """

        pr: float = StandardNormal.dist.cdf(z)

        return round(pr, 4)

    def sf(z: float) -> float:
        """
        """

        pr: float = StandardNormal.dist.sf(z)

        return round(pr, 4)

    def z(x: float, mean, std) -> float:
        """
        Returns the z-value for a given x from Norm(mu, var)
        rounded to 2 dp.
        """

        z: float = (x-mean)/std

        return round(z, 2)

    def q(alpha: float) -> float:
        """
        Returns the alpha-quantile of Z.
        """

        q: float = StandardNormal.dist.ppf(alpha)

        if (alpha >= 0.5 and alpha <= 0.53):
            return round(q, 5)
        elif (alpha >= 0.54 and alpha <= 0.84):
            return round(q, 4)
        else:
            return round(q, 3)


class Normal():
    """
    A convenience class that works with scipy.norm to help solve
    various problems involving the normal distribution.
    """

    def __init__(
        self, mu: float, std: float = None, var: float = None
    ) -> None:
        """
        Constructor for object of type Normal that model the normal
        distribution N(mu, var).

        One of args std or var must be passed. If both are passed, then
        construction uses arg std.
        """

        if std is not None:
            self._dist: norm = norm(loc=mu, scale=std)
        elif var is not None:
            self._dist: norm = norm(loc=mu, scale=sqrt(var))
        else:
            print("Object not constructed, check parameters.")

    # instance methods

    def cdf(self, x: float, to_printer: bool = True) -> Any:
        """
        Calculates the Pr(X <= x). If arg `to_printer` is True, then
        prints the solution to the screen. Otherwise returns the answer
        as a float.

        @params
        =======
        `x`
            A float.

        `to_printer`
            Whether to print the answer to the screen, or return a
            float. Default is True.

        @returns
        ========
            `None` or float.
        """

        # create new solution object
        soln: Solution = Solution()

        # get answers
        Pr: float = self._dist.cdf(x)
        z: float = (
            StandardNormal.z(x, self._dist.mean(), self._dist.std())
        )

        # update solution
        if z < 0:
            soln.no_trunc_update(
                name=f"Line 1: F({x})",
                answer=f"phi({z})"
            )
            soln.no_trunc_update(
                name="Line 2:    ",
                answer=f"1-phi({-1*z})"
            )
        else:
            soln.no_trunc_update(
                name=f"Line 1: F({x})",
                answer=f"phi({z})"
            )

        soln.update(name="Answer:    ", answer=Pr)

        if to_printer:
            print(soln)
        else:
            return Pr

    def gt(
        self, x: float, to_printer: bool = True, to_plot: bool = False
    ) -> Any:
        """
        Calculates the Pr(X > x). If arg `to_printer` is True, then
        prints the solution to the screen. Otherwise returns the answer
        as a float.

        @params
        =======
        `x`
            A float

        `to_printer`
            Whether to print the answer to the screen, or return a
            float. Default is True.

        @returns
        ========
            `None` or float.
        """

        # create new solution object
        soln: Solution = Solution()

        # get answers
        Pr: float = self._dist.sf(x)
        z: float = StandardNormal.z(x, self._dist.mean(), self._dist.std())
        pr_z: float = StandardNormal.cdf(z)

        # update solution
        if (z < 0):
            soln.no_trunc_update(
                name=f"Line 1: P(X>{x})",
                answer=f"1-F({x})"
            )
            soln.no_trunc_update(
                name="Line 2:    ",
                answer=f"1-phi({z})"
            )
            soln.no_trunc_update(
                name="Line 3:    ",
                answer=f"1-{{1-phi({-1*z})}}"
            )
            soln.no_trunc_update(
                name="Line 4:    ",
                answer=f"phi({-1*z})"
            )
        else:
            soln.no_trunc_update(
                name=f"Line 1: P(X>{x})",
                answer=f"1-F({x})"
            )
            soln.no_trunc_update(
                name="Line 2:    ",
                answer=f"1-phi({z})"
            )
            soln.no_trunc_update(
                name="Line 3:    ",
                answer=f"1-{pr_z}"
            )

        soln.update(name="Answer:    ", answer=Pr)

        if to_plot:
            self.plot(fill_from=x, fill_to=self._dist.ppf(0.99))

        if to_printer:
            print(soln)
        else:
            return Pr

    def pr(self, x1: float, x2: float) -> None:
        """
        Calculates the Pr(x1< X < x2). Prints the solution to the
        screen.

        @params
        `x1`, `x2`
            A float
        """

        # create new solution object
        soln: Solution = Solution()

        # get answers
        # sorry for all the local vars guys - LK
        pr_x1: float = self._dist.cdf(x1)
        pr_x2: float = self._dist.cdf(x2)
        pr: float = pr_x2 - pr_x1
        z1: float = StandardNormal.z(x1, self._dist.mean(), self._dist.std())
        z2: float = StandardNormal.z(x2, self._dist.mean(), self._dist.std())
        pr_z1: float = StandardNormal.cdf(z1)
        pr_z2: float = StandardNormal.cdf(z2)
        pr_min_z1: float = StandardNormal.cdf(-1*z1)
        pr_min_z2: float = StandardNormal.cdf(-1*z2)

        # update solution
        soln.no_trunc_update(
            name=f"Line 1: P({x1}<X<{x2})",
            answer=f"F({x2})-F({x1})"
        )
        soln.no_trunc_update(
            name="Line 2:    ",
            answer=f"phi({z2})-phi({z1})"
        )

        # case 1: both z1, z2 >= mean
        if (z1 >= 0 and z2 >= 0):
            soln.no_trunc_update(
                name="Line 3:    ",
                answer=f"{pr_z2}-{pr_z1}"
            )

        # case 2: x1 < mean, x2 > mean
        elif (z1 < 0 and z2 >= 0):
            soln.no_trunc_update(
                name="Line 3:    ",
                answer=f"phi({z2})-{{1-phi({-1*z1})}}"
            )
            soln.no_trunc_update(
                name="Line 4:    ",
                answer=f"phi({z2})+phi({-1*z1})-1"
            )
            soln.no_trunc_update(
                name="Line 5:    ",
                answer=f"{pr_z2}+{pr_min_z1}-1"
            )

        # case 3: both x1, x2 < mean
        else:
            soln.no_trunc_update(
                name="Line 3:    ",
                answer=f"{{1-phi({-1*z2})}}-{{1-phi({-1*z1})}}"
            )
            soln.no_trunc_update(
                name="Line 4:    ",
                answer=f"phi({-1*z1})-phi({-1*z2})+1-1"
            )
            soln.no_trunc_update(
                name="Line 5:    ",
                answer=f"{pr_min_z1}+{pr_min_z2}"
            )

        soln.update(name="Answer:    ", answer=pr)

        print(soln)

    def quantile(self, a: float, to_printer: bool = True) -> None:
        """
        Calculates q_{a}. If arg to_printer is True, then prints the
        solution to the screen. Otherwise returns the answer as a float.

        @params
        `a`
            Float, the quantile to return q_{a}.

        `to_printer`
            Whether to print the answer to the screen, or return a
            float. Default is True.

        @returns
            `None` or float
        """

        # create new solution object
        soln: Solution = Solution()

        # get answers
        x: float = self._dist.ppf(a)
        q = StandardNormal.q(a)

        # update solution
        if a < 0.5:
            soln.no_trunc_update(f"q({a})", f"-q({1-a})={q}")
        else:
            soln.update(f"q({a})", q)

        soln.update("x", x)

        if to_printer:
            print(soln)
        else:
            return x

    def take_sampling_distribution(
        self, n: int, sample_mean: bool = True
    ) -> Normal:
        """
        Takes a sampling distribution for the distribution of the
        receiver. If arg `sample_mean` is true, takes the sampling
        distribution of the sample mean. Otherwise, takes the
        distribution of the sample total.

        Returns an object of type Normal.
        """

        if sample_mean:
            new_mean: float = self._dist.mean()
            new_var: float = self._dist.var()/n

            # print output
            print("Taking the sampling distribution of the sample mean.\n")

        else:
            new_mean: float = self._dist.mean()*n
            new_var: float = self._dist.var()*n

            # print output
            print("Taking the distribution of the sample total.\n")

        print("Target distribution")
        print("===================")
        self.describe()
        print("")

        sampling_dist: Normal = Normal(mu=new_mean, var=new_var)

        print("Sampling distribution")
        print("=====================")
        sampling_dist.describe()

        return sampling_dist

    def plot(
        self,
        fill_from: float = None,
        fill_to: float = None
    ) -> None:
        """
        Plots the receiver's distribution normal distribution.
        If fill_between is declared, then shade between boundaries.
        """

        # get the range of X
        x = np.linspace(
            self._dist.ppf(0.01),
            self._dist.ppf(0.99),
            100
        )

        # create the plot
        ax = sns.lineplot(
            x=x,
            y=self._dist.pdf(x),
            lw=5,
            color="red"
        )

        # identify the shaded region
        if fill_from is not None and fill_to is not None:
            x_fill = np.linspace(
                start=fill_from,
                stop=fill_to,
                num=100
            )
            y_fill = self._dist.pdf(x_fill)
            plt.fill_between(
                x_fill,
                y_fill,
                alpha=0.5
            )

        ax.set_title("Normal distribution")

        plt.show()

    def describe(self) -> None:
        """
        Prints a representation of the receiver's distribution.
        """

        # create new solution object
        soln: Solution = Solution()

        # update solution
        soln.no_trunc_update("model", "Normal")
        soln.update("mean", self._dist.mean())
        soln.update("var", self._dist.var())

        print(soln)


class ConfidenceInterval():
    """
    A convenience class that works with scipy.norm and scipy.t to
    calculate and return z- and t-intervals.
    """
