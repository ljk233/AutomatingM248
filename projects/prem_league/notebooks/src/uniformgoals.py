
from __future__ import annotations
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2


class UniformGoals():
    """
    A class of static methods to help with the chi-squared
    goodness-of-fit test to test the hypothesis that goals
    are scored evenly across a game.
    """

    def get_banding(x: int) -> str:
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

    def plot_distribution(x, y) -> None:
        """
        Plots the number of goals in a ten mnute window as a seaborn
        barplot. Returns no value
        """

        ax = sns.barplot(
            x=x,
            y=y,
            color="cornflowerblue"
        )

        ax.set(xlabel="X")

        ax.set_title("Number of goals scored per ten minute banding")

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

        print(f"p = {chi2(df).cdf(chi_sq)}")
