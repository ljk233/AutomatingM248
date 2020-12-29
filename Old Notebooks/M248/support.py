from scipy.stats import poisson, expon
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def samplePoisson(N: int) -> None:
    '''Generates a random sample from the Poisson(10) distribution, and
    plots the distribution'''

    fig, ax = plt.subplots(1, 1)

    mu = 10
    x = np.arange(poisson.ppf(0.01, mu),
                  poisson.ppf(0.99, mu))
    ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
    ax.vlines(x, 0, poisson.pmf(x, mu), colors='r', lw=5, alpha=0.5)

    r = poisson.rvs(10, size=N)
    df = pd.DataFrame(data=x, columns={'x'})

    a_list = list()

    for i in x:
        count = 0
        for j in r:
            if i == j:
                count = count+1
        a_list.append(count/N)

    df = pd.DataFrame(data=x, columns={'x'})
    df['rel freq'] = a_list
    ax.bar(x=df['x'], height=df['rel freq'], alpha=0.3)
    ax.legend(loc='best', frameon=False)
    plt.show()


def sampleExponential(N: int) -> None:
    '''Generates a random sample from the M(2) distribution, and
    plots the distribution.'''

    fig, ax = plt.subplots(1, 1)

    x = np.linspace(expon.ppf(q=0.01, scale=0.5),
                    expon.ppf(q=0.99, scale=0.5), 100)
    ax.plot(x, expon.pdf(x, scale=0.5),
            'r-', lw=5, alpha=0.6, label='exponential pdf')

    r = expon.rvs(scale=0.5, size=N)
    ax.hist(r, bins=50, density=True, histtype='stepfilled', alpha=0.3)
    ax.legend(loc='best', frameon=False)
    plt.show()


def generateSampleMean(dist: object, sample_size: int) -> list:
    '''Generates a sample of size 'sample_size' from the distribution.
    Calculates the sample total and the sample mean.

    Return: Sample mean
    '''

    a_sample: list = dist.rvs(size=sample_size)

    # calculate the sample total
    sample_total: float = 0

    for an_obs in a_sample:
        sample_total = sample_total + an_obs

    # calculate the sample mean
    sample_mean: float = sample_total/sample_size

    return sample_mean


def generateSampleDist(dist: object,
                       sample_size: int,
                       total_samples: int) -> list:
    '''Generates a sample distribution of means of size number from giving
    distribution.

    return: a list of sample means
    '''

    a_list: list = list()

    i: int = 1

    while i <= total_samples:
        a_mean: float = generateSampleMean(dist=dist, sample_size=sample_size)
        a_list.append(a_mean)
        i = i + 1

    return a_list


def generatePlotSampleDist(dist: object,
                           k: int,
                           N: int) -> None:
    '''
    Returns: None.
    Arg k is the number of observations within the sample.
    Arg N is the number of samples of size k to generate.
    '''

    # declare the list of sample means
    sample_means: list = list()

    i: int = 1  # counter variable

    # while the counter is less than or equal to the total samples
    while i <= N:
        # generate a sample
        a_sample: list = dist.rvs(size=k)

        a_total: int = 0

        # calculate the sample total
        for an_obs in a_sample:
            a_total = a_total + an_obs

        # calculate the sample mean
        a_mean: float = a_total/k

        # append the sample mean to the sample mean list
        sample_means.append(a_mean)

        # increment the counter
        i = i + 1

    # plot the histogram
    sns.histplot(x=sample_means, binwidth=1)

    return None
