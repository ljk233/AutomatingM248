from scipy.stats import poisson, expon, randint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def sample_poisson(sample_size: int) -> None:
    '''
    Generates a random sample from the Poisson(10) distribution, and
    plots the distribution.
    '''

    fig, ax = plt.subplots(1, 1)

    mu = 10
    x = np.arange(poisson.ppf(0.01, mu),
                  poisson.ppf(0.99, mu))
    ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
    ax.vlines(x, 0, poisson.pmf(x, mu), colors='r', lw=5, alpha=0.5)

    r = poisson.rvs(10, size=sample_size)
    df = pd.DataFrame(data=x, columns={'x'})

    a_list = list()

    for i in x:
        count = 0
        for j in r:
            if i == j:
                count = count+1
        a_list.append(count/sample_size)

    df = pd.DataFrame(data=x, columns={'x'})
    df['rel freq'] = a_list
    ax.bar(x=df['x'], height=df['rel freq'], alpha=0.3)
    ax.legend(loc='best', frameon=False)
    plt.title(("Plot of Poisson(10), " +
               "n=" + str(sample_size)))
    plt.show()


def sample_exponential(sample_size: int) -> None:
    '''
    Generates a random sample from the M(2) distribution, and
    plots the distribution.
    '''

    fig, ax = plt.subplots(1, 1)

    x = np.linspace(expon.ppf(q=0.01, scale=0.5),
                    expon.ppf(q=0.99, scale=0.5), 100)
    ax.plot(x, expon.pdf(x, scale=0.5),
            'r-', lw=5, alpha=0.6, label='exponential pdf')

    r = expon.rvs(scale=0.5, size=sample_size)
    ax.hist(r, bins=50, density=True, histtype='stepfilled', alpha=0.3)
    ax.legend(loc='best', frameon=False)
    plt.title(("Plot of M(2), " +
               "n=" + str(sample_size)))
    plt.show()


def sample_discrete_uniform(sample_size: int) -> None:
    '''
    Generates a random sample from the discrete uniform distribution,
    with parameters lower=1, upper=12, and plots the distribution.

    We set local variable high to 14 because np.arange output 1 to 13,
    and randint requires upper to be upper+1.
    '''

    fig, ax = plt.subplots(1, 1)
    low, high = 1, 14
    x = np.arange(randint.ppf(0.01, low, high),
                  randint.ppf(0.99, low, high))
    ax.plot(x, randint.pmf(x, low, high), 'bo', ms=8, label='randint pmf')
    ax.vlines(x, 0, randint.pmf(x, low, high), colors='b', lw=5, alpha=0.5)

    r = randint.rvs(low, high, size=sample_size)
    df = pd.DataFrame(data=x, columns={'x'})

    a_list = list()

    for i in x:
        count = 0
        for j in r:
            if i == j:
                count = count+1
        a_list.append(count/sample_size)

    df = pd.DataFrame(data=x, columns={'x'})
    df['rel freq'] = a_list
    ax.bar(x=df['x'], height=df['rel freq'], alpha=0.5)
    ax.legend(loc='best', frameon=False)
    plt.title(("Plot of discrete uniform distribution (1, 12)," +
               " n=" + str(sample_size)))
    plt.show()
