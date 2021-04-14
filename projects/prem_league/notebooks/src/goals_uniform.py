
from __future__ import annotations
from .data import Data
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2


class UniformGoals():
    """
    A class of static methods to help with the chi-squared
    goodness-of-fit test to test the hypothesis that goals
    are scored evenly across a game.
    """

    SAMPLE = Data.load_uniform_goal_chi_sq()

    def plot_distribution() -> None:
        """
        Plots the number of goals in a ten mnute window as a seaborn
        barplot. Returns no value
        """

        ax = sns.barplot(
            x=UniformGoals.SAMPLE["banding"],
            y=UniformGoals.SAMPLE["observed"],
            color="cornflowerblue"
        )

        ax.set(xlabel="X")

        ax.set_title("Number of goals scored per ten minute banding")

        plt.show()

    def get_chi2() -> float:
        """
        Returns the sum of a column of data as a float.
        """

        return UniformGoals.SAMPLE["chi-sq contribution"].sum()

    def get_p_from_chi2(chi_sq, df) -> None:
        """
        Prints the p-value of arg chi-sq from the chi2(arg df)
        distribution. Returns no value.
        """

        print(f"{1 - chi2(df).cdf(chi_sq)}")
