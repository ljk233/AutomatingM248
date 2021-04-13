
from __future__ import annotations
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import poisson, chi2, expon


class PoissonProcess():
    """
    A class of static methods to help with the Poisson process.
    """

    def get_banding(x: int) -> str:
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

    def plot_x(x) -> None:
        """
        Plots the number of goals per game as a seaborn countplot.
        Returns no value
        """

        ax = sns.countplot(x=x, color="cornflowerblue")
        ax.set(xlabel="X")
        ax.set_title("Number of goals per game")
        plt.show()

    def plot_w(w) -> None:
        """
        Plots the waiting time between goals as a seaborn histplot.
        Returns no value
        """

        ax = sns.histplot(
            x=w,
            color="cornflowerblue",
            binwidth=10
        )
        ax.set(xlabel="W")
        ax.set_title("Waiting time between goals (mins)")
        plt.show()

    def plot_Poisson(mu: float) -> None:
        """
        Plots the PMF of Poisson(mu) as a seaborn barplot.
        """

        poiss = poisson(mu)

        # get the range and Pr
        r = np.arange(start=0, stop=9)
        rv = poiss.pmf(r)

        ax = sns.barplot(x=r, y=rv, color="cornflowerblue")
        ax.set(xlabel="X", ylabel="p(x)")
        ax.set_title(f"Poisson({mu})")
        plt.show()

    def plot_expon(mu: float) -> None:
        """
        Plots the PMF of M(mu) as a seaborn barplot.
        """

        m = expon(scale=mu)
        r = np.linspace(start=m.ppf(0.01), stop=m.ppf(0.99), num=100)
        rv = m.pdf(r)
        ax = sns.histplot(
            x=rv,
            color="cornflowerblue",
            bins=15
        )
        ax.set(xlabel="W", ylabel="f(W)")
        ax.set_title(f"M({mu})")
        plt.show()

    def plot_rate(x, y) -> None:
        """
        Plots the rate of goals scored over the observation period as a
        seaborn scatterplot.
        """

        ax = sns.scatterplot(
            x=x,
            y=y
        )

        ax.set(xlabel="Goal time (mins)", ylabel="Goal ID")
        ax.set_title("Rate of goals scored over the observation period")
        plt.show()

    def get_chi2(contributions) -> float:
        """
        Returns the sum of a column of data as a float.
        """

        return contributions.sum()

    def get_p_from_chi2(chi_sq, df) -> None:
        """
        Prints the p-value of arg chi-sq from the chi2(arg df)
        distribution. Returns no value.
        """

        print(f"{1 - chi2(df).cdf(chi_sq)}")
