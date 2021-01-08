import numpy as np
from scipy.stats import poisson
import pandas as pd


def get_samples(a_dist, n: int, N: int) -> dict:
    """
    Generates N samples of size n from a_dist.
    Calculates the mean and variance of each sample, and returns
    as a dict.
    """

    samples: dict = dict()
    means: list = list()  # holding list for the sample means
    sample_vars: list = list()  # holding list for the sample variances
    pop_vars: list = list()  # holding list for the population variances

    for i in range(N):
        a_sample = a_dist.rvs(size=n)
        means.append(a_sample.mean())
        sample_vars.append(a_sample.var(ddof=1))
        pop_vars.append(a_sample.var())

    # append to dictionary
    samples["means"] = np.array(means)
    samples["sample vars"] = np.array(sample_vars)
    samples["population vars"] = np.array(pop_vars)

    return samples


def get_table1():
    """
    """

    """-----------------------------------------------------------------------
    We have already written a function that will generate one sample
    Let us loop five times, each time invoking the function.
    -----------------------------------------------------------------------"""

    collection: list = list()

    for i in range(0, 5):
        collection.append(get_samples(a_dist=poisson(mu=1),
                                      n=10,
                                      N=1000))

    """-----------------------------------------------------------------------
    Let us further aggregate the data by finding the mean of each sample's
    means and variances.

    We append them to a list so we send them to a DataFrame.
    -----------------------------------------------------------------------"""

    means: list = list()

    for i in range(0, 5):
        means.append(collection[i]["means"].mean())

    sample_vars: list = list()

    for i in range(0, 5):
        sample_vars.append(collection[i]["sample vars"].mean())

    pop_vars: list = list()

    for i in range(0, 5):
        pop_vars.append(collection[i]["population vars"].mean())

    """-----------------------------------------------------------------------
    And finally, let us append these to a `DataFrame` for display purposes.
    -----------------------------------------------------------------------"""

    tbl1 = pd.DataFrame()
    tbl1["Sample"] = ["One"] + ["Two"] + ["Three"] + ["Four"] + ["Five"]
    tbl1["Mean"] = means
    tbl1["Sample Variance"] = sample_vars
    tbl1["Population Variance"] = pop_vars
    tbl1

    return tbl1
