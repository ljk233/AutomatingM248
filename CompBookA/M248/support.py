
import seaborn as sns
import numpy as np


def plotProbDist(x: object, title: str) -> None:
    '''
    Plots the probability distribution
    '''

    # generated array of x 0:30
    X = np.arange(30)

    p = list()
    # for each x in X
    for i in X:
        # calculate p(x), append to list
        p.append(x.pmf(i))

    # plot p(x)
    ax1 = sns.barplot(x=X, y=p, palette="Blues_d")
    ax1.set(xlabel='x', ylabel='p(x)', title=title)
