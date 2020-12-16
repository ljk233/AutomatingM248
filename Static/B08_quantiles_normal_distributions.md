# B8 Quantiles of normal variables

```python
from m248_support import Standard_Normal, Normal
from scipy import stats
```

## 1 Calculating quantiles

### Example 8.1.1

Let $X$ be a random variable distributed $X \sim N(100,15^{2})$.

Calculate the values of the following quantiles

**(a)** $q_{U}$

**(b)** $q_{0.2}$

**(c)** $q_{0.99}$

```python
# declare the distribution
x = Normal(a_mean=100, a_std=15)
```

#### (a)

The $0.75-$quantile, $x$, of the distribution $N(100, 15^{2}$) is

$$
x = \sigma q_{0.75} + \mu = 15 q_{0.75} + 100,
$$

where $q_{0.75}$ is the $0.75-$quantile of the standard normal distribution, $q_{0.75} = \cdots$

```python
Standard_Normal.has_quantile(a=0.75)
```

```
0.6745
```

Therefore, the $0.75-$quantile of the distribution is

$$
x = 15(0.6745) + 100 = \cdots
$$

```python
x.has_quantile(a=0.75)
```

```
110.1173
```

#### (b)

The $0.2-$quantile, $x$, of the distribution $N(100, 15^{2}$) is

$$
x = \sigma q_{0.2} + \mu = 15 q_{0.2} + 100,
$$

where $q_{0.2}$ is the $0.22-$quantile of the standard normal distribution, $-q_{0.8} = \cdots$

```python
Standard_Normal.has_quantile(a=0.2)
```

```
-0.8416
```

Therefore, the $0.2-$quantile of the distribution is

$$
x = 15(-0.8416) + 100 = \cdots
$$

```python
x.has_quantile(a=0.2)
```

```
87.3757
```

#### (c)

The $0.99-$quantile, $x$, of the distribution $N(100, 15^{2}$) is

$$
x = \sigma q_{0.99} + \mu = 15 q_{0.99} + 100,
$$

where $q_{0.99}$ is the $0.99-$quantile of the standard normal distribution, $q_{0.99} = \cdots$

```python
Standard_Normal.has_quantile(a=0.99)
```

```
2.3263
```

Therefore, the $0.99-$quantile of the distribution is

$$
x = 15(2.3263) + 100 = \cdots
$$

```python
x.has_quantile(a=0.99)
```

```
134.8952
```

### Example 8.1.2

Suppose that the size (in inches) of skipjack tuna may reasonably be modelled by a normal distribution with mean 22 and standard deviation 2.

According to the model, what is

**(a)** the interquartile range of the distribution of skipjack tuna in this population?

**(b)** the size $x$ such that only 5% of skipjack tuna in the population are bigger than this size?

```python
# declare the distribution
x = Normal(a_mean=22, a_std=2)
```

#### (a)

The iqr is defined as $q_{U} - q_{L} = q_{0.75} - q_{0.25}$.

The $0.75-$quantile, $x$, of the distribution $N(100, 15^{2}$) is

$$
x = \sigma q_{0.75} + \mu = 2 q_{0.75} + 22,
$$

where $q_{0.75}$ is the $0.75-$quantile of the standard normal distribution, $q_{0.75} = \cdots$

```python
Standard_Normal.has_quantile(a=0.75)
```

```
0.6745
```

Therefore, the $0.75-$quantile of the distribution is

$$
x = 2(0.6745) + 22 = \cdots
$$

```python
x.has_quantile(a=0.75)
```

```
23.349
```

And the $0.25-$quantile, $x$, of the distribution $N(100, 15^{2}$) is

$$
x = 2 q_{0.25} + 22,
$$

where $q_{0.25}$ is the $0.25-$quantile of the standard normal distribution, $q_{0.25} = -q_{0.75} = \cdots$

```python
Standard_Normal.has_quantile(a=0.25)
```

```
-0.6745
```

Therefore, the $0.25-$quantile of the distribution is

$$
x = 2 (0.6745) + 22 = \cdots
$$

```python
x.has_quantile(a=0.25)
```

```
20.651
```

Therefore, the distribution has iqr $\ldots$

```python
# calculate the iqr
round(x.has_quantile(a=0.75) - x.has_quantile(a=0.25), 4)
```

```
2.698
```

#### (b)

The size of skipjack tuna, $x$ such that only 5% of skipjack tunas exceed that is that is the $0.95$-quantile.
This is

$$
x = \sigma q_{0.95} + \mu = 2 q_{0.95} + 22,
$$

where $q_{0.95}$ is the $0.95-$quantile of the standard normal distribution, $q_{0.95} = \cdots$

```python
Standard_Normal.has_quantile(a=0.95)
```

```
1.6449
```

Therefore, the size $x$ is

$$
x = 2 (1.6449) + 22 = \cdots
$$

```python
x.has_quantile(a=0.95)
```

```
25.2897
```
