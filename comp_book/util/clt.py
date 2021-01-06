import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import seaborn as sns


def clt(a_dist: object,
        n: int,
        N: int,
        plot_normal: bool = False,
        bins: int = 50) -> None:
    '''
    Generates N random samples of size n from the distribution a_dist.
    Calulate's each samples mean, and plots the sampling
    distribution of the mean on a histogram as a relative freq
    histogram.

    The parameter `bins` controls the number of bins used in the
    histogram.
    Changing this parameter will make the histogram less accurate,
    but improves the plot's fidelity for discrete distributions.

    If parameter plot_normal=true, also outputs the CLT approximation
    of the sampling distribution of the mean.
    '''

    fig, ax = plt.subplots(1, 1)

    if plot_normal:
        mu = a_dist.mean()
        ste = a_dist.std()/(n**0.5)

        x = np.linspace(norm.ppf(q=0.01, loc=mu, scale=ste),
                        norm.ppf(q=0.99, loc=mu, scale=ste), 100)
        ax.plot(x, norm.pdf(x, loc=mu, scale=ste),
                'r-', lw=5, alpha=0.6, label='CLT')

    sample_means: list = list()

    i: int = 1  # counter variable
    while i <= N:
        sample_means.append(a_dist.rvs(size=n).mean())
        i += 1

    sns.histplot(sample_means,
                 stat="density",
                 bins=bins,
                 alpha=0.3)
    ax.legend(loc='best', frameon=False)
    # ax.axes.yaxis.set_visible(False)

    plt.show()

    return None
