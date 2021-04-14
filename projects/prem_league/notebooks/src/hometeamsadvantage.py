
from .data import Data
import pandas as pd
from scipy.stats import norm
from math import sqrt
import seaborn as sns
import matplotlib.pyplot as plt


class HomeAdvantage():
    """
    A class of static methods to help with the analysis of whether
    Home teams score more goals.
    """

    SAMPLE = Data.load_home_advantage()

    def get_sample_size() -> int:
        """
        Returns the sample size.
        """
        return HomeAdvantage.SAMPLE["home"].size

    def get_home_mean() -> float:

        return HomeAdvantage.SAMPLE["home"].mean()

    def get_away_mean() -> float:

        return HomeAdvantage.SAMPLE["away"].mean()

    def get_home_std() -> float:

        return HomeAdvantage.SAMPLE["home"].std()

    def get_away_std() -> float:

        return HomeAdvantage.SAMPLE["away"].std()

    def get_ese() -> float:

        frac1: float = (
            HomeAdvantage.get_home_std()**2 /
            HomeAdvantage.get_sample_size()
        )

        frac2: float = (
            HomeAdvantage.get_away_std()**2 /
            HomeAdvantage.get_sample_size()
        )

        return sqrt(frac1 + frac2)

    def get_z() -> float:

        return (
            (HomeAdvantage.get_home_mean() - HomeAdvantage.get_away_mean()) /
            HomeAdvantage.get_ese())

    def get_p() -> None:

        return round(1 - norm().cdf(HomeAdvantage.get_z()), 10)

    def plot_sample() -> None:
        """
        Plots the same in home, away as a side-by-side bar chart.
        """

        plot_data = pd.melt(
            HomeAdvantage.SAMPLE,
            value_vars=['home', 'away']
        )

        ax = sns.countplot(
            data=plot_data,
            x="value",
            hue="variable"
        )

        ax.set(xlabel="Number of goals", ylabel="Frequency")

        ax.set_title("Number of goals scored by home and away teams")

        plt.show()
