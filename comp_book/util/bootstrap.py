from scipy.stats import randint, norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def bootstrap(a_dist, n) -> None:
    '''
    A quick and dirty function to run a bootstrap method
    for the sampling distribution of the mean.

    The algorithm is
    BEGIN
      generate a_sample of size n from a_dist
      repeating n*n times
        repeating n times
          randomly select an observation
          append observation to a_resample
        calculate a_mean of a_resample
        append a_mean to means
      plot means as a histogram
    END
    '''

    fig, ax = plt.subplots(1, 1)

    mu = a_dist.mean()
    std = a_dist.std()

    x = np.linspace(norm.ppf(q=0.01, loc=mu, scale=std),
                    norm.ppf(q=0.99, loc=mu, scale=std), 100)
    ax.plot(x, norm.pdf(x, loc=mu, scale=std),
            'r-', lw=5, alpha=0.6, label='normal pdf')

    # generate a sample of the distribution
    a_sample = a_dist.rvs(size=n)
    means: list = list()

    for i in range(n*n):
        a_resample: list = list()
        for j in range(n):
            a_resample.append(a_sample[randint.rvs(low=0, high=n, size=1)])
        means.append(np.array(a_resample).mean())

    sns.histplot(means,
                 stat="probability",
                 bins=10,
                 alpha=0.3)
    ax.legend(loc='best', frameon=False)
    ax.axes.yaxis.set_visible(False)

    plt.show()

    return None
