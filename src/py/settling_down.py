
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class SettlingDown():
    """
    A class to visualise the settling down phemonenon.
    """

    SAMPLE_SIZES: list = [30, 100, 1000]
    OBS: int = 1130

    def __init__(
        self,
        a_dist: object,
        is_discrete: bool
    ) -> None:
        """
        Constructor for objects of type SettlingDown.
        Sets dist to arg a_dist, some distribution as created by
        scipy.stats.

        If a_dist is_discrete, then sets discrete to True, sets X
        to array of integers using np.arange(), and sets pr to the
        probability of each x in X using pmf method.

        Otherwise, sets discrete to False, sets X to array of floats
        using np.linspace(), and sets pr to the probability of each x
        in X using pdf method.
        """

        self.dist: object = a_dist

        if is_discrete:
            self.discrete = True
            x_range = np.arange(a_dist.ppf(0.01), a_dist.ppf(0.99))
            self.X = x_range
            self.pr = np.array(a_dist.pmf(x_range))
        else:
            self.discrete = False
            x = np.linspace(
                start=a_dist.ppf(0.01),
                stop=a_dist.ppf(0.99),
                num=100
            )
            self.X = x
            self.pr = a_dist.pdf(x)

    def plot_prob_function(self) -> None:
        """
        If the receiver's dist is discrete, then plot the probability
        mass function as a seaborn barplot.
        Otherwise, plot the probability density function as a seaborn
        histplot.
        """

        if self.discrete:
            self._plt_discrete_prob_function()
        else:
            self._plt_cts_prob_function()

    def plot_samples(self) -> None:
        """
        If the receiver's dist is discrete, then plot random samples
        as a seaborn barplot.
        Otherwise, plot the random samples as a seaborn histplot.
        """

        if self.discrete:
            self._plt_discrete_samples()
        else:
            self._plt_cts_samples()

    def _plt_discrete_prob_function(self) -> None:
        """
        Plots the probability function of the receiver's dist as a
        seaborn barplot. Returns no value.
        """

        sns.barplot(x=self.X, y=self.pr, color="cornflowerblue")
        plt.show()

    def _plt_discrete_samples(self) -> None:
        """
        Generates random samples with increasing sizes of receiver's
        dist as seaborn barplots, and outputs them on a seaborn
        FacetGrid.
        """

        samples: list = list()

        # build a list of sample name
        # will be used to segment the data
        for a_size in SettlingDown.SAMPLE_SIZES:
            i: int = 0
            while i < a_size:
                samples.append(a_size)
                i += 1

        # add the list to a new DataFrame
        df_samples = pd.DataFrame(data=samples, columns=["Sample size"])
        # generate the observations
        df_samples["obs"] = self.dist.rvs(size=SettlingDown.OBS)

        # plot the sample data
        g = sns.FacetGrid(
            df_samples,
            col="Sample size",
            height=4,
            sharey=False
        )

        g.map(sns.countplot, "obs", order=self.X, color="cornflowerblue")
        plt.show()

    def _plt_cts_prob_function(self) -> None:
        """
        Plots the probability function of the receiver's dist as a
        seaborn linplot. Returns no value.
        """

        sns.lineplot(
            x=self.X,
            y=self.pr,
            color="cornflowerblue",
            lw=2,
            label="f(x)"
        )
        plt.show()

    def _plt_cts_samples(self) -> None:
        """
        Generates random samples with increasing sizes of receiver's
        dist as seaborn barplots, and outputs them on a seaborn
        FacetGrid.
        """

        samples: list = list()

        # build a list of sample name
        # will be used to segment the data
        for a_size in SettlingDown.SAMPLE_SIZES:
            i: int = 0
            while i < a_size:
                samples.append(a_size)
                i += 1

        # add the list to a new DataFrame
        df_samples = pd.DataFrame(data=samples, columns=["Sample size"])
        # generate the observations
        df_samples["obs"] = self.dist.rvs(size=SettlingDown.OBS)

        # plot the sample data
        g = sns.FacetGrid(
            df_samples,
            col="Sample size",
            height=4,
            sharey=False,
        )

        g.map(
            sns.histplot,
            "obs",
            color="cornflowerblue"
        )
        plt.show()
