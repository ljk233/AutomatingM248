# B9 Sampling distributions of the sample mean and totals

```python
from m248_support import Normal
from scipy import stats
```

## 1 Sampling distribution of the sample mean

### Example 9.1.1

Suppose that a random sample of 50 packets of sweets of a certain variety is taken from a production line.
The number of sweets in each packet $X$ may be modelled by a Poisson distribution with mean 45.

**(a)** What is the approximate distribution of the sample mean, $\overline{X}_{50}$?

**(b)** What is the probability that the sample mean will be less than 43 sweets?

```python
# declare the original distribution
p = stats.poisson(mu=45)
```

```python
# declare the normal distribution
# use the original distribution as parameters
x = Normal(a_mean=p.mean(), a_std=p.std())
```

```python
# model the sampling distribution of the mean
sample_mean = x.model_sample_distribution_of_mean(n=50)
```

#### (a)

Let $X_{i}$ represent the number of sweets in packet $i$. Then $X_{i} \sim \text{Poisson}(45)$.

For a Poisson distribution with parameter $\lambda$, both the mean and the variance are equal to $\lambda$, and so when $X_{i} \sim \text{Poisson}(45)$, then $\mu$ is

```python
p.mean()
```

```
45.0
```

and $\sigma$ is approximately

```python
round(p.std(), 4)
```

```
6.7082
```

By the Central Limit Theorem, the mean $\overline{X}_n$ of large $n$ independent random variables each with mean $\mu$ and standard deviation $\sigma$ has distribution

$$
\overline{X}_n \sim N \bigg( \mu, \frac{\sigma}{\sqrt{n}} \bigg).
$$

Therefore, $E(\overline{X}_n)$ is

```python
sample_mean.get_mu()
```

```
45.0
```

and $S(\overline{X}_n)$ is approximately

```python
round(sample_mean.get_sigma(), 4)
```

```
0.9487
```

so that $\overline{X}_n \sim \ldots$

```python
sample_mean.is_distributed()
```

```
Current model: N(45.0, 0.95^2)
```

#### (b)

The probability $P(\overline{X}_{50} \leq 43) = P(Z \leq z)$, where $z =$

```python
sample_mean.has_z(x=43)
```

```
-2.11
```

Therefore, the probability $P(Z \leq -2.11) = \Phi (-2.11) = 1 - \Phi (2.11) = \cdots$

```python
sample_mean.has_F(x=43)
```

```
0.0175
```

### Example 7.1.2 (June 2020)

Suppose that the weights of the contents of a certain brand of cereal packets, each of which is labelled as containing 500 g, are normally distributed with a mean weight of 502 g and standard deviation of 5 g.

A random sample of 40 packets is taken.

**(a)** What is the approximate distribution of the sample mean, $\overline{X}_{40}$?

**(b)** Calculate the probability that the sample mean that the sample mean contents is less than 500 g.

```python
# declare the original distribution
x = Normal(a_mean=502, a_std=5)
```

```python
# model the sampling distribution of the mean
sample_mean = x.model_sample_distribution_of_mean(n=40)
```

#### (a)

The $E(\overline{X}_{40}) = \mu = \cdots$

```python
sample_mean.get_mu()
```

```
502
```

and $S(\overline{X}_{40}) = \sigma / \sqrt{n} = 5 / \sqrt{40} = \cdots$

```python
round(sample_mean.get_sigma(), 4)
```

```
0.7906
```

So $\overline{X}_{40} \sim \cdots$

```python
sample_mean.is_distributed()
```

```
Current model: N(502, 0.79^2)
```

#### (b)

The probability $P(\overline{X}_{40} \leq 500) = P(Z \leq z)$, where $z =$

```python
sample_mean.has_z(x=500)
```

```
-2.53
```

Therefore, the probability $P(Z \leq -2.53) = \Phi (-2.53) = 1 - \Phi (2.53) = \cdots$

```python
sample_mean.has_F(x=500)
```

```
0.0057
```

## 2 Sampling distribution of the sample total

### Example 9.2.1 (U6.Ex24)

Vehicles pass an observer in such a way that the waiting time between successive vehicles may be adequately modelled by an exponential distribution with mean 15 seconds.
Particular details of each vehicle that passes are recorded on a sheet.
There is room to record the details of twenty vehicles on each sheet.

**(a)** What is the distribution that models the time taken to complete a sheet, $T_{20}$?

**(b)** What, approximately, is the probability that it takes less than 6 minutes to fill one of the sheets?

#### (a)

If $W$ is the waiting time in seconds between successive vehicles, then $W$ has mean 15.
Since the mean and standard deviation of an exponential distribution are equal, the standard deviation of $W$ is 15.
The time $T_{20}$ that it takes to fill a sheet is the sum of the first twenty such waiting times is

$$
T_{20} = W_{1} + W_{2} + \cdots + W_{20}.
$$

```python
# declare the distribution
w = Normal(a_mean=15, a_std=15)
```

```python
# model sample mean of size 20
t = w.model_sampling_distribution_of_total(n=20)
```

So $E(T_{20}) = 20 E(X) \cdots$

```python
t.get_mu()
```

```
300
```

and $S(T_{20}) = S(X) \sqrt{20} \simeq \cdots$

```python
round(t.get_sigma(), 4)
```

```
67.082
```

Also, by the corollary to the Central Limit Theorem, Distributional Result, the distribution of $T_{20}$ is approximately normal, so $T_{20} \sim \cdots$

```python
t.is_distributed()
```

```
Current model: N(300, 67.08^2)
```

#### (b)

The approximate probability that the total time taken to fill a sheet is less than 6 minutes (or 360 seconds) is given by

$$
P(T_{20} \leq 360) = P(Z \leq z)
$$

where $z$ is

```python
t.has_z(x=360)
```

```
0.89
```

And so $P(T_{20} \leq 360) = \Phi (0.89) = \cdots$

```python
t.has_F(x=360)
```

```
0.8145
```

*Note, there's a slight discrepency compared to the text due to rounding.*

### Example 9.2.2 (June 2017)

The mean weight of chocolate bars produced by a particular factory is 39 g with a variance of 16 g$^{2}$. Those chocolate bars were packed in boxes with 30 bars.

**(a)** What is the distribution that models the boxes of 30 bars, $T_{30}$?

**(b)** Calculate the approximate probability that the total weight of chocolate bars in a box will exceed 1130 g.

```python
# declare the distribution
w = Normal(a_mean=39, a_std=4)
```

```python
# model sample mean of size 30
t = w.model_sampling_distribution_of_total(n=30)
```

#### (a)

Let $W_{i}$ be represent the weight of of chocolate bar $i$ in a box, where $W_{i} \sim N(39, 4^{2})$.

Let $T_{30}$ be

$$
T_{30} = \sum_{i=1}^{30} W_{i}, \hspace{3mm} i = 1, 2, \ldots 30,
$$

where $E(T_{30}) = 30 E(W_{i}) = \cdots$

```python
t.get_mu()
```

```
1170
```

and $S(T_{30}) = S(W_{i}) \sqrt{30} = \cdots$

```python
round(t.get_sigma(), 4)
```

```
21.9089
```

So therefore, $T_{30} \sim \cdots$

```python
t.is_distributed()
```

```
Current model: N(1170, 21.91^2)
```

#### (b)

The approximate probability that the total weight of a box of thirty chocolate bars is greater than 1130 g is given by $P(T_{30} \geq 1130) = P(Z \geq z)$, where $z$ is

```python
t.has_z(x=1130)
```

```
-1.83
```

Therefore, $P(T_{30} \geq 1130) = 1 - \Phi (-1130) = \Phi (1130) = \cdots$

```python
t.has_F(x=1130, greater_than=True)
```

```
0.9661
```
