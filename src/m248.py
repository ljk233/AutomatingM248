
from __future__ import annotations
from abc import abstractmethod
from math import sqrt, trunc
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


class StandardDiscrete():
    """
    A class used to represent a standard discrete probability model.
    """

    def __init__(self, a_dist: object = None) -> None:
        """
        Constructor for objects of type Standard Distribution.
        """

        self._dist: object = a_dist
        self._lower: int = 0  # minimum value of the range

    # ========================================================================
    # Properties
    # ========================================================================

    @property
    def mean(self) -> float:
        """
        Returns the mean of the receiver, truncated to 6 decimal
        places.
        """

        return StandardDiscrete._truncate(self._dist.mean())

    @property
    def var(self) -> float:
        """
        Returns the variance of the receiver, truncated to 6 decimal
        places.
        """

        return StandardDiscrete._truncate(self._dist.var())

    @property
    def std(self) -> float:
        """
        Returns the standard deviation of the receiver, truncated to 6
        decimal places.
        """

        return StandardDiscrete._truncate(self._dist.std())

    @property
    def lower(self) -> int:
        """
        Returns the lower boundary of the range.
        """

        return self._lower

    # ========================================================================
    # static helper methods
    # ========================================================================

    def _print_line_break() -> None:
        """
        Prints a standardised line break of 20x'='.
        """

        print("====================")

    def _truncate(x) -> float:
        """
        Returns argument x truncated to 6dp. There is no rounding.
        """

        stepper = 10.0 ** 6
        return trunc(stepper * x) / stepper

    # ========================================================================
    # helper methods
    # ========================================================================

    def _print_header(self, pr: str) -> None:
        """
        Prints the header of the calculation in the form
        "Outputting calculation for arg pr from arg dist".
        """

        print(f"Outputting calcuations for {pr} from {self}")
        StandardDiscrete._print_line_break()

    def _print_first_line(self, pr: str, a: int, b: int) -> None:
        """
        Prints the first line of the calculation.
        """

        # local variables
        pr_expanded: str = f"p({a})"
        k: int = a + 1

        while (k <= b):
            elem: str = f" + p({k})"
            pr_expanded = pr_expanded + elem
            k += 1

        print(f"{pr} = {pr_expanded}")

    def _print_first_line_greater(self, pr: str, a: int, b: int) -> None:
        """
        Prints the first line of the calculation for the sf
        """

        # local variables
        pr_expanded: str = f"1 - p({a})"
        k: int = a + 1

        while (k <= b):
            elem: str = f" - p({k})"
            pr_expanded = pr_expanded + elem
            k += 1

        print(f"{pr} = {pr_expanded}")

    def _print_sub_calculations(self, a: int, b: int) -> None:
        """
        Prints the secod line of the calculation.
        """

        # local variables
        pr_expanded: str = (
            f"    = {StandardDiscrete._truncate(self._dist.pmf(a))}"
        )
        k: int = a + 1

        while (k <= b):
            elem: str = f" + {StandardDiscrete._truncate(self._dist.pmf(k))}"
            pr_expanded = pr_expanded + elem
            k += 1

        print(f"{pr_expanded}")

    def _print_sub_calculations_greater(self, a: int, b: int) -> None:
        """
        Prints the secod line of the calculation.
        """

        pr_expanded: str = (
            f"    = 1 - {StandardDiscrete._truncate(self._dist.pmf(a))}"
        )
        k: int = a + 1

        while (k <= b):
            elem: str = f" - {StandardDiscrete._truncate(self._dist.pmf(k))}"
            pr_expanded = pr_expanded + elem
            k += 1

        print(f"{pr_expanded}")

    def _print_soln(self, soln: float) -> None:
        """
        Prints the footer of the calculation in the form
        "{pr} = {soln}". Argument soln is truncated to 6 dp.
        """

        print(f"    = {StandardDiscrete._truncate(soln)}")

    # ========================================================================
    # instance methods
    # ========================================================================

    def pmf(self, x: int) -> None:
        """
        Returns the probability mass function of the receiver truncated
        to 6dp.
        """

        # local variables
        pr: str = f"P(X={x})"
        soln: float = self._dist.pmf(x)

        # print calculations
        self._print_header(pr)
        self._print_first_line(pr, a=x, b=x)
        self._print_soln(soln)

    def cdf(
        self,
        x: int
    ) -> None:
        """
        Outputs the calculations needed to solve F(x).
        Values are truncated to 6dp.
        """

        # local variables
        pr: str = f"P(X<={x})"
        soln: float = self._dist.cdf(x)

        # print calculation
        self._print_header(pr)
        self._print_first_line(pr, a=self.lower, b=x)
        self._print_sub_calculations(a=self.lower, b=x)
        self._print_soln(soln)

    def gt(
        self,
        x: int
    ) -> None:
        """
        Outputs the calculations needed to solve P(X>x) = 1 - F(x).
        Values are truncated to 6dp.
        """

        # declare local variables
        pr_header: str = f"P(X>{x})"
        pr_calc: str = f"P(X>{x}) = 1 - P(X<={x})"
        soln: float = self._dist.sf(x)

        # print calculation
        self._print_header(pr_header)
        self._print_first_line_greater(pr_calc, a=self.lower, b=x)
        self._print_sub_calculations_greater(a=self.lower, b=x)
        self._print_soln(soln)

    def lt(self, x: int) -> None:
        """
        Outputs the calculations needed to solve P(X<x).
        Values are truncated to 6dp.
        """

        # local variables
        pr_header: str = f"P(X<{x})"
        pr_calc: str = f"P(X<{x}) = P(X<={x-1})"
        soln: float = self._dist.cdf(x-1)

        # print calculation
        self._print_header(pr_header)
        self._print_first_line(pr_calc, a=self.lower, b=x-1)
        self._print_sub_calculations(a=self.lower, b=x-1)
        self._print_soln(soln)

    def geq(self, x: int) -> None:
        """
        Outputs the calculations needed to solve Pr(X>=x).
        Values are truncated to 6dp.
        """

        # declare local variables
        pr_header: str = f"P(X>={x})"
        pr_calc: str = f"P(X>={x}) = 1 - P(X<={x-1})"
        soln: float = 1 - self._dist.cdf(x-1)

        # print calculation
        self._print_header(pr_header)
        self._print_first_line_greater(pr_calc, a=self.lower, b=x-1)
        self._print_sub_calculations_greater(a=self.lower, b=x-1)
        self._print_soln(soln)

    def plot(self) -> None:
        """
        Plots the pmf of the distribution as a bar chart
        """

        fig, ax = plt.subplots(1, 1)

        x = np.arange(
                self._dist.ppf(0.01),
                self._dist.ppf(0.99) + 1
        )

        int_x: list = list()
        for j in x:
            int_x.append(int(j))

        pr: list = list()
        for i in x:
            pr.append(self._dist.pmf(i))

        sns.barplot(
            x=int_x,
            y=pr,
            color="royalblue"
        )

        plt.title(label=f"Probability mass function of {self}")
        plt.show()

    @abstractmethod
    def __str__(self) -> str:
        """
        @abstract.
        Returns a standard string of the the receiver.
        """

        return "a dist"


class Binomial(StandardDiscrete):
    """
    Class to model a binomial distribution.
    """

    def __init__(self, n: int, p: float) -> None:
        """
        Constructor for an object of type binomial.
        """

        self._n = n
        self._p = p

        super().__init__(a_dist=stats.binom(n, p))

    def __str__(self) -> str:
        """
        """

        return (
            f"B{self._n, self._p}"
        )


class Geometric(StandardDiscrete):
    """
    Class to model a geometric distribution.
    """

    def __init__(self, p: float) -> None:
        """
        Constructor for an object of type binomial.
        """

        super().__init__(a_dist=stats.geom(p))
        self._lower = 1
        self._p = p

    def cdf(self, x) -> None:
        """
        @Override.
        Prints the F(x) of G(p).
        """

        pr: str = f"P(X<={x})"
        soln: float = self._dist.cdf(x)

        self._print_header(pr)
        print(
            f"{pr} = F({x})"
            f"\n    = 1 - {1-self._p}^{{{x}}}",
            f"\n    = {StandardDiscrete._truncate(soln)}"
        )

    def gt(self, x) -> None:
        """
        @Override.
        Prints the P(X>x) of G(p).
        """

        pr: str = f"P(X>{x})"
        soln: float = self._dist.sf(x)

        self._print_header(pr)
        print(
            f"{pr} = 1 - F({x})",
            f"\n    = {1 - self._p}^{{{x}}}",
            f"\n    = {StandardDiscrete._truncate(soln)}"
        )

    def geq(self, x) -> None:
        """
        @Override.
        Prints the P(X>=x) of G(p).
        """

        pr: str = f"P(X>={x})"
        soln: float = self._dist.sf(x-1)

        self._print_header(pr)
        print(
            f"{pr} = 1 - F({x-1})",
            f"\n    = 1 - (1 - {1 - self._p}^{{{x-1}}})",
            f"\n    = {StandardDiscrete._truncate(soln)}"
        )

    def lt(self, x) -> None:
        """
        @Override.
        Prints the P(X<x) of G(p).
        """

        pr: str = f"P(X<{x})"
        soln: float = self._dist.cdf(x-1)

        self._print_header(pr)
        print(
            f"{pr} = F({x-1})"
            "\n    = 1 - ",
            f"({StandardDiscrete._truncate(1 - self._p)})^{{{x-1}}}",
            f"\n    = {StandardDiscrete._truncate(soln)}"
        )

    def __str__(self) -> str:
        """
        """

        return (
            f"G({self._p})"
        )


class Poisson(StandardDiscrete):
    """
    Class to model a Poisson distribution.
    """

    def __init__(self, mu: float) -> None:
        """
        Constructor for an object of type Poisson.
        """

        self._mu = mu

        super().__init__(a_dist=stats.poisson(mu))

    def __str__(self) -> str:
        """
        """

        return (
            f"Poisson({self._mu})"
        )


class StandardNormal():
    """
    Class to model a normal probability distribution.
    """

    dist: stats.norm = stats.norm(0, 1)

    def get_cdf(z: float) -> float:
        """
        Returns the phi(z) of the standard normal distribuition rounded
        to 4dp.
        """
        pr: float = StandardNormal.dist.cdf(z)
        return round(pr, 4)

    def get_sf(z: float) -> float:
        """
        """
        pr: float = StandardNormal.dist.sf(z)
        return round(pr, 4)

    def get_z(x: float, mean, std) -> float:
        """
        Returns the z-value for a given x from Norm(mu, var)
        rounded to 2 dp.
        """
        z: float = (x-mean)/std
        return round(z, 2)

    def get_quantile(alpha: float) -> float:
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


class t():
    """
    Class to model t-distribution.
    """

    def get_quantile(alpha: float, df: int) -> float:
        """
        Returns the alpha-quantile of t(dof).
        """

        return round(stats.t.ppf(alpha, df), 3)


class Normal():
    """
    Class to model a normal probability distribution.
    """

    def __init__(self, mean: float, var: float) -> None:
        """
        """

        self._dist: stats.norm = stats.norm(mean, var ** 0.5)
        self._mean: float = mean
        self._var: float = var
        self._std: float = var ** 0.5

    # ========================================================================
    # @properties
    # ========================================================================

    @property
    def mean(self) -> float:
        """
        Returns the mean of the receiver, truncated to 6 decimal
        places.
        """

        return self._mean

    @property
    def var(self) -> float:
        """
        Returns the variance of the receiver, truncated to 6 decimal
        places.
        """

        return self._var

    @property
    def std(self) -> float:
        """
        Returns the standard deviation of the receiver, truncated to 6
        decimal places.
        """

        return self._std

    # ========================================================================
    # static helper methods
    # ========================================================================

    def _print_line_break() -> None:
        """
        Prints a standardised line break of 20x'='.
        """

        print("====================")

    def _truncate(x) -> float:
        """
        Returns argument x truncated to 4dp. There is no rounding.
        """

        stepper = 10.0 ** 4
        return trunc(stepper * x) / stepper

    # ========================================================================
    # helper methods
    # ========================================================================

    def _print_header(self, pr: str) -> None:
        """
        Prints the header of the calculation in the form
        "Outputting calculation for arg pr from arg dist".
        """

        print(f"Outputting calcuations for {pr} of {self}")
        StandardDiscrete._print_line_break()

    def _print_soln(self, soln: float) -> None:
        """
        Prints the footer of the calculation in the form
        "{pr} = {soln}". Argument soln is truncated to 6 dp.
        """

        print(f"    = {Normal._truncate(soln)}")

    # ========================================================================
    # instance methods
    # ========================================================================

    def __str__(self) -> str:
        return f"N({self.mean}, {self.var})"

    def cdf(self, x: float) -> None:
        """
        Prints the F(x) of the receiver's distribution, truncated to
        6dp.
        """

        pr: str = f"P(X<{x})"
        z: float = StandardNormal.get_z(x, self.mean, self.std)

        self._print_header(pr)

        # generate the calculation strings
        print(f"{pr} = P(Z<{z})")
        print(f"    = phi({z})")

        # work out if x < mu
        if (x < self.mean):
            # adjust z
            z = z*-1
            print(f"    = 1 - phi({z})")
            print(f"    = 1 - {StandardNormal.get_cdf(z)}")

        # calc solution
        soln: float = StandardNormal.get_cdf(z)

        print(f"    = {soln}")

    def gt(self, x: float) -> None:
        """
        Prints the F(x) of the receiver's distribution, truncated to
        6dp.
        """

        pr_header: str = f"P(X>{x})"
        pr_calc: str = f"P(X>{x}) = 1 - P(X<{x})"
        z: float = StandardNormal.get_z(x, self.mean, self.std)
        soln: float = StandardNormal.get_sf(z)

        self._print_header(pr_header)

        # generate the calculation strings
        print(f"{pr_calc}")
        print(f"    = 1 - P(Z<{z})"),
        print(f"    = 1 - phi({z})")

        if (x < self.mean):
            # adjust z
            z = z*-1
            print(f"    = 1 - {{1 - phi({z})}}")
            print(f"    = phi({z})")

        self._print_soln(soln)

    def pr(self, x1: float, x2: float) -> None:
        """
        """

        pr_header: str = f"Pr({x1}<X<{x2})"
        z1: float = StandardNormal.get_z(x1, self.mean, self.std)
        z2: float = StandardNormal.get_z(x2, self.mean, self.std)
        soln: float = StandardNormal.get_cdf(z2) - StandardNormal.get_cdf(z1)

        self._print_header(pr_header)
        print(f"{pr_header} = P(X<{x2}) - P(X<{x1})")
        print(f"    = P(Z<{z2}) - P(Z<{z1})")
        print(f"    = phi({z2}) - phi({z1})")

        # case 1: both x1, x2 >= mean
        if x1 >= self.mean and x2 >= self.mean:
            phi_z1: float = StandardNormal.get_cdf(z1)
            phi_z2: float = StandardNormal.get_cdf(z2)
            print(f"    = {phi_z2} - {phi_z1}")

        # case 2: x1 < mean, x2 > mean
        elif x1 < self.mean and x2 >= self.mean:
            # adjust z1
            z1 = z1*-1
            phi_z1: float = StandardNormal.get_cdf(z1)
            phi_z2: float = StandardNormal.get_cdf(z2)
            print(f"    = phi({z2}) - {{1 - phi({z1})}}")
            print(f"    = phi({z2}) + phi({z1}) - 1")
            print(f"    = {phi_z2} + {phi_z1} - 1")

        # case 3: both x1, x2 < mean
        elif x1 < self.mean and x2 < self.mean:
            # adjust z1, z2
            z1 = z1*-1
            z2 = z2*-1
            phi_z1: float = StandardNormal.get_cdf(z1)
            phi_z2: float = StandardNormal.get_cdf(z2)
            print(f"    = {{1 - phi({z2})}} - {{1 - phi({z1})}}")
            print(f"    = phi({z1}) + phi({z2})")
            print(f"    = {phi_z1} + {phi_z2}")

        self._print_soln(soln)

    def quantile(self, alpha: float) -> None:
        """

        """

        q: float = StandardNormal.get_quantile(alpha)
        soln: float = self._dist.ppf(alpha)

        print(f"Outputting calcuations for {alpha}-quantile of {self}")
        Normal._print_line_break()

        print("x = std * q_{{alpha}} + mean")
        print(f"    = {self.std} * q_{{{alpha}}} + {self.mean}")

        if (alpha < 0.5):
            print(f"    = {self.std} * -q_{{{1-alpha}}} + {self.mean}")
            # recalculate q to adjust accuracy
            q = StandardNormal.get_quantile(1-alpha)

        print(f"    = {self.std} * {q} + {self.mean}")
        self._print_soln(soln)

    def sample_mean(self, n: int) -> object:
        """
        """

        # local vars
        new_var = self.var/n
        sample_mean: Normal = Normal(self.mean, new_var)

        print("Outputting distribution of the sampling mean")
        Normal._print_line_break()
        print(f"E(Xn) = {self.mean}")
        print(f"V(Xn) = {self.var}/{n} = {Normal._truncate(self.var/n)}")
        Normal._print_line_break()
        print(f"Returned new distribution: {sample_mean}")

        return sample_mean

    def sample_total(self, n: int) -> object:
        """
        """

        # local vars
        new_mean = self.mean * n
        new_var = self.var * n
        sample_total: Normal = Normal(new_mean, new_var)

        print("Outputting distribution of the sampling total")
        Normal._print_line_break()
        print(f"E(Sn) = {self.mean} * {n} = {Normal._truncate(new_mean)}")
        print(f"V(Sn) = {self.var} * {n} = {Normal._truncate(new_var)}")
        Normal._print_line_break()
        print(f"Returned new distribution: {sample_total}")

        return sample_total

    def plot(
        self,
        fill_from: float = None,
        fill_to: float = None
    ) -> None:
        """
        Plots a normal distribution.
        If fill_between is declared, then shade between boundaries.
        """

        fig, ax = plt.subplots()

        x = np.linspace(
            self._dist.ppf(0.01),
            self._dist.ppf(0.99), 100
        )

        sns.lineplot(
            x=x,
            y=self._dist.pdf(x),
            lw=5,
            color="red"
        )

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

        plt.show()


class HypothesisTest():
    """
    """

    # ========================================================================
    # static helper methods
    # ========================================================================

    def _print_line_break() -> None:
        """
        Prints a standardised line break of 20x'='.
        """

        print("====================")

    def _truncate(x) -> float:
        """
        Returns argument x truncated to 6dp. There is no rounding.
        """

        stepper = 10.0 ** 6
        return trunc(stepper * x) / stepper

    # ========================================================================
    # static methods
    # ========================================================================

    def z_test_mean_two_tail(
        sig_level: int,
        n: int,
        mu0: float,
        mu: float,
        var: float
    ) -> None:
        """
        """

        # sort out parameters
        alpha: float = 1 - (sig_level/200)
        z: float = (mu - mu0)/(sqrt(var/n))

        c1: float = StandardNormal.get_quantile(alpha)
        c2: float = -1 * StandardNormal.get_quantile(alpha)

        # state parameters

        # step 1: state test
        print(
            "Testing hypotheses:",
            f"\n    null: mu = {mu0}, alt: mu != {mu0}"
        )

        # step 2: test statistic
        print(
            "\nTest statistic",
            f"\n    Z = {HypothesisTest._truncate(z)}"
        )

        # step 3: critical values
        print(
            f"\nCritical values for {sig_level}% test:",
            f"\n    c1 = {c1}",
            f"\n    c2 = {c2}",
            "\nRejection region:",
            f"\n    z<={c1} or z>={c2}",
        )

        # step 4: p-value
        print(
            "p-value:",
            f"    p = P(Z<=)"
        )

    def z_test_mean_one_tail_lt(
    ) -> None:
        """
        """

    def z_test_mean_one_tail_gt(
    ) -> None:
        """
        """
