## About

This note was made in response to a post by **@Iank**

> Hi Liam
>
> I got this where it was talking about estimators of the mean. Not easy, but i think i got there in the end....
>
> What did you make of the estimator of variance and the whole 1/n vs 1/n-1 section?
>
> I confess i found that the most difficult thing i've come across in the unit so far. Do you have any insights on that?
>
> I think in this instance i'm struggling with the proliferation of symbols - I'd love to see it explained in words!
>
> Cheers
>
> Ian

In this note, we first run through Example 7, Unit 7 to see why the two estimators for the variance are what they are.
We finish up with an example of both estimators in action.

## Unbiased estimators

Recall that an estimator $\widehat \theta$ is an unbiased estimator of $\theta$, if and only if

$$
E(\widehat \theta) = \theta.
$$

## Scenario

We want to estimate $\sigma^{2}$ of a distribution from a random sample of size $n$ observations $X_{i} = X_{1}, X_{2}, \ldots, X_{n}$.

Remember that, by definition, if $\mu$ and $\sigma^{2}$ are the population mean and the population variance, then

$$
\sigma^{2} = E\{(x-\overline{x})^{2}\}.
$$

## A biased estimate of the variance

One way to estimate $\sigma^{2}$ would be to use the classic definition[^1] of what an average is, such that

$$
\widehat \theta_{V} = \frac{1}{n} \sum_{i=1}^{n}\{ (X_{i} - \overline X)^{2} \}.
$$

And so, if $\widehat \theta_{V}$ is an unbiased estimator of $\sigma^{2}$, then it must be that

$$
E(\widehat \theta_{V}) = \sigma^{2},
$$

by the definition of what an unbiased estimator is: Is this the case?

Let us expand the summation:

$$
\begin{aligned}
  E(\widehat \theta_{V}) &= E\bigg\{\frac{1}{n} \sum_{i=1}^{n} (X_{i} - \overline X)^{2}\bigg\} \\
    &= \frac{1}{n} E\bigg\{ \sum_{i=1}^{n} (X_{i} - \overline X)^{2}\bigg\} \\
    &= \frac{n-1}{n}  \sigma^{2} \neq \sigma^{2}.
\end{aligned}
$$

Therefore, we can conclude that $\widehat \theta_{V}$ is biased.

Note, there is nothing special about this result. It will always be biased, because of how we calculated the variance in the first place.

## An unbiased estimate of the variance

We can estimate $\sigma^{2}$ using the sample variance, $\theta_{S}$, where

$$
\widehat \theta_{S} = \frac{1}{n-1} \sum_{i=1}^{n}\{ (X_{i} - \overline X)^{2} \}.
$$

And so, if $\widehat \theta_{S}$ is an unbiased estimator of $\sigma^{2}$, then it must be that

$$
E(\widehat \theta_{S}) = \sigma^{2},
$$

by the definition of what an unbiased estimator is: Is this the case?

Let us expand the summation:

$$
\begin{aligned}
  E(\widehat \theta_{S}) &= E\bigg\{\frac{1}{n-1} \sum_{i=1}^{n} (X_{i} - \overline X)^{2}\bigg\} \\
    &= \frac{1}{n-1} E\bigg\{ \sum_{i=1}^{n} (X_{i} - \overline X)^{2}\bigg\} \\
    &= \frac{n-1}{n-1}  \sigma^{2} = \sigma^{2}.
\end{aligned}
$$

Therefore, we can conclude that $\widehat \theta_{S}$ is unbiased.

## Comparing the two estimators in action

In this example, we will:

- Generate 1000 samples of size $n=10$ from the $B(10,0.5)$
- For each sample, calculate $\overline X, \widehat \theta_{S}, \widehat \theta_{V}.$
- Calculate $E(\overline X), E(\widehat \theta_{S}), E(\widehat \theta_{V}).$

After the conclulsion of the workflow, we should see that:

- $E(\overline X) \simeq \mu = 10(0.5) = 5$
- $E(\widehat \theta_{S}) \simeq \sigma^{2} = 10(0.5)(0.5) = 2.5$.
- $E(\widehat \theta_{V}) \simeq \frac{n-1}{n}\sigma^{2} = \frac{9}{10}10(0.5)(0.5) = 2.25$.

```python
from scipy.stats import binom
import pandas as pd
import numpy as np
from util.pointestimation import (get_sample, get_samples,
                                  get_description, get_table1)

a_dist = binom(n=10, p=0.5)  # the distribution B(10,0.5)
```

Let us first generate a random sample $X$ from $B(10,0.5)$ to illustrate the first step.

```python
get_sample(a_dist, n=10)  # a sample of size 10 from B(10,0.5)
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }


    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }

</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X</th>
      <th>obs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>5</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>6</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>5</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>7</td>
    </tr>
  </tbody>
</table>

</div>

There is nothing particularly surprising here, so let us move on.

Let us now generate $N=1000$ samples of size $n=10$ from $B(10,0.5)$.
We will calculate $\overline X$, $\widehat \theta_{S}$ and $\widehat \theta_{V}$ for each sample.
The returned table will contain these three measures for each sample $X_{i}$.

```python
samples: dict = get_samples(a_dist,
                            n=10,
                            N=1000)

samples.head()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }


    .dataframe tbody tr th {
        vertical-align: top;
    }
    
    .dataframe thead th {
        text-align: right;
    }

</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>E(X)</th>
      <th>Theta(S)</th>
      <th>Theta(V)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4.1</td>
      <td>0.766667</td>
      <td>0.69</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.1</td>
      <td>2.766667</td>
      <td>2.49</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.5</td>
      <td>1.388889</td>
      <td>1.25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.7</td>
      <td>1.566667</td>
      <td>1.41</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>2.000000</td>
      <td>1.80</td>
    </tr>
  </tbody>
</table>

</div>

We now have 3000 estimates, 1000 for each estimator.
So let us check the expected values of each of our estimators to see how close they are to $\mu=5$ and $\sigma^{2} = 2.5$.

As a sanity check, we know that the sample mean is an unbiased estimator of the population mean.
Does $E(\overline X) \simeq 5$?

```python
samples["E(X)"].mean()
```

    5.0198

That is reassuring!
Next, does $E(\widehat \theta_{S}) \simeq 2.5$?

```python
samples["Theta(S)"].mean()
```

    2.525911111111111

Again, we can conclude that they are approximately equal.
And finally, does $E(\widehat \theta_{V}) \simeq 2.25$?

```python
samples["Theta(V)"].mean()
```

    2.27332

Yes, it does seem so.

Finally, we can display that this phenomenom is just an expression of the formulas we used to generate the estimates of $\sigma^{2}$.

If, as we have seen,

$$
\begin{aligned}
  E(\widehat \theta_{V}) = \frac{n-1}{n}\sigma^{2},
\end{aligned}
$$

then

$$
\begin{aligned}
  \sigma^{2} =\frac{n}{n-1} E(\widehat \theta_{V}).
\end{aligned}
$$

But we also know that 

$$
E(\widehat \theta_{S}) = \sigma^{2},
$$

Therefore it must be that

$$
E(\widehat \theta_{S}) = \frac{n}{n-1} E(\widehat \theta_{V}).
$$

Can we confirm this from our sample?

We know that $n=10, \sigma^{2} = 2.5$ so ...

```python
samples["Theta(S)"].mean() == (10/9) * samples["Theta(V)"].mean()
```

    True

**END**.

[^1]: This is $\overline{X} = \frac{\sum X}{N}$.