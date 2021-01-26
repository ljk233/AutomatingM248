import numpy as np
import pandas as pd


def get_sample(a_dist, n: int) -> None:
    """
    Generates an example random sample of size n from a_dist.
    """

    a_sample = pd.DataFrame()
    a_sample["X"] = np.arange(start=1, stop=n+1)
    a_sample["obs"] = a_dist.rvs(size=n)

    return a_sample


def get_description(a_dist, a_sample):
    """
    Generates a pd.DataFrame, showing the
    - sample mean,
    - variance,
    - sample variance,
    - population variance.

    Returns the DataFrame
    """

    np_sample = np.array(a_sample)
    a_table = pd.DataFrame()
    a_table["E(X)"] = [np_sample.mean()]
    a_table["SV(X)"] = [np_sample.var(ddof=1)]
    a_table["PV(X)"] = [np_sample.var()]

    return a_table


def get_samples(a_dist, n: int, N: int) -> dict:
    """
    Generates N samples of size n from a_dist.
    Calculates the mean and variance of each sample, and returns
    as a dict.
    """

    a_df = pd.DataFrame()
    means: list = list()  # holding list for the sample means
    sample_vars: list = list()  # holding list for the sample variances
    pop_vars: list = list()  # holding list for the population variances

    for i in range(N):
        a_sample = a_dist.rvs(size=n)
        means.append(a_sample.mean())
        sample_vars.append(a_sample.var(ddof=1))
        pop_vars.append(a_sample.var())

    # append to dataframe
    a_df["E(X)"] = np.array(means)
    a_df["Theta(S)"] = np.array(sample_vars)
    a_df["Theta(V)"] = np.array(pop_vars)

    return a_df


def get_table1(a_dist, n: int, N: int):
    """
    Generates five collections of N samples of size n from
    a_dist, and calculates the sample mean, samples variance, and
    population variance.

    Return the result is a pd.DataFrame.
    """

    """-----------------------------------------------------------------------
    We have already written a function that will generate one sample
    Let us loop five times, each time invoking the function.
    -----------------------------------------------------------------------"""

    collection: list = list()

    for i in range(0, 5):
        collection.append(get_samples(a_dist=a_dist,
                                      n=n,
                                      N=N))

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
