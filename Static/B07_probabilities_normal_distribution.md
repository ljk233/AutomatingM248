# B7 Probabilities of normal variables

```python
from m248_support import Standard_Normal, Normal
from scipy import stats
```

## 1 Standard normal distribution

### Example 7.1.1

> Let $Z$ be a random variable distributed $Z \sim N(0,1)$.
>
> Calculate
>
> **(a)** $P(Z \leq 1)$
>
> **(b)** $P(Z \leq -0.7)$

**(a)** The probability $P(Z \leq 1) = \Phi (1) = \cdots$

```python
Standard_Normal.has_phi(z=1)
```

```
0.8413
```

**(b)** The probability $P(Z \leq -0.7) = 1 - \Phi (0.7) = \cdots$

```python
Standard_Normal.has_phi(z=-0.7)
```

```
0.242
```

### Example 7.1.2

> Let $Z$ be a random variable distributed $Z \sim N(0,1)$.
>
> Calculate
>
> **(a)** $P(Z \geq 1.3)$
>
> **(b)** $P(Z \geq -1.6)$

**(a)** The probability $P(Z \geq 1.3) = 1 - \Phi (1.3) = \cdots$

```python
Standard_Normal.has_phi(z=1.3, greater_than=True)
```

```
0.0968
```

**(b)** The probability $P(Z \geq -1.6)$ is given by

$$
\begin{aligned}
P(Z \geq -1.6) &= 1 - \Phi (-1.6) \\
  &= 1 - (1 - \Phi (1.6)) \\
  &= \Phi (1.6) \\
  &= \cdots
\end{aligned}
$$

```python
Standard_Normal.has_phi(z=-1.6, greater_than=True)
```

```
0.9452
```

### Example 7.1.3

> Let $Z$ be a random variable distributed $Z \sim N(0,1)$.
>
> Calculate
>
> **(a)** $P(-1.25 \leq Z \leq 2)$
>
> **(b)** $P(-1.5 \leq Z \leq 0.5)$

**(a)** The probability $P(-1.25 \leq Z \leq 2)$ is

$$
\begin{aligned}
P(-1.25 \leq Z \leq 2) &= \Phi(2) - \Phi(-1.25) \\
  &= \Phi(2) - (1 - \Phi(1.25)) = \cdots
\end{aligned}
$$

```python
Standard_Normal.has_prob_range_phi(z1=-1.25, z2=2)
```

```
0.8716
```

**(b)** The probability $P(-1.5 \leq Z \leq 0.5)$ is

$$
\begin{aligned}
P(-1.5 \leq Z \leq 0.5) &= \Phi(0.5) - \Phi(-1.5) \\
  &= \Phi(0.5) - (1 - \Phi(-1.5)) = \cdots
\end{aligned}
$$

```python
Standard_Normal.has_prob_range_phi(z1=-1.5, z2=0.5)
```

```
0.6247
```

## 2 Other normal distributions

### Example 7.2.1

> Let $X$ be a random variable distributed $X \sim N(8,2^{2})$.
>
> Calculate
>
> **(a)** $P(X \leq 10)$
>
> **(b)** $P(X \geq 7)$
>
> **(c)** $P(X \leq Z \leq 9.5)$

```python
# declare the distribution
x = Normal(a_mean=8, a_std=2)
```

**(a)** The probability $P(X \leq 10) = P(Z \leq z)$, where $z$ is

$$
z = \frac{10 - \mu}{\sigma} = \cdots
$$

```python
x.has_z(x=10)
```

```
1.0
```

Therefore, the probability $P(X \leq 10) = P(Z \leq 1) = \Phi (1) = \cdots$

```python
x.has_F(x=10)
```

```
0.8413
```

**(b)** The probability $P(X \geq 7) = P(Z \geq z)$, where $z$ is

$$
z = \frac{7 - \mu}{\sigma} = \cdots
$$

```python
x.has_z(x=7)
```

```
-0.5
```

Therefore, the probability $P(X \geq 7)$ is given by

$$
\begin{aligned}
P(Z \geq -0.5) &= 1 - \Phi (-0.5) \\
  &= 1 - (1 - \Phi (0.5)) \\
  &= \Phi (0.5) \\
  &= \cdots
\end{aligned}
$$

```python
x.has_F(x=7, greater_than=True)
```

```
0.6915
```

**(c)** The probability $P(6 \leq X \leq 9.5) = P(z_{1} \leq Z \leq z_{2})$, where

$$
z_{1} = \dfrac{6 - \mu}{\sigma} = \cdots
$$

```python
x.has_z(x=6)
```

```
-1.0
```

and

$$
z_{2} = \dfrac{9.5 - \mu}{\sigma} = \cdots
$$

```python
x.has_z(x=9.5)
```

```
0.75
```

Therefore, the probability $P(6 \leq X \leq 9.5)$ is given by

$$
\begin{aligned}
P(z_{1} \leq Z \leq z_{2}) &= P(-1 \leq Z \leq 0.75) \\
  &= \Phi (0.75) - \Phi (-1) \\
  &= \Phi (0.75) - (1 - \Phi (1)) \\
  &= \Phi (0.75) + \Phi (1) - 1 \\
  &= \ldots
\end{aligned}
$$

```python
x.has_prob_range_F(x1=6, x2=9.5)
```

```
0.6147
```

### Example 7.2.2

> Suppose that the birth weight (in kilograms) of new born babies in a population may be reasonably modelled by a normal distribution with mean 3.4 and standard deviation 0.5.
>
> According to the model, what is the proportion of birth weights that are
>
> **(a)** between 2.9 and 3.9 kilograms?
>
> **(b)** less than 4 kilograms?
>
> **(c)** greater that 3 kilograms?

```python
# declare the distribution
x = Normal(a_mean=3.4, a_std=0.5)
```

**(a)** The probability $P(2.9 \leq X \leq 3.9) = P(z_{1} \leq Z \leq z_{2})$, where $z_{1}$ is

```python
x.has_z(x=2.9)
```

```
-1.0
```

and $z_{2}$ is

```python
x.has_z(x=3.9)
```

```
1.0
```

Therefore, the probability $P(2.9 \leq X \leq 3.9)$ is given by

$$
\begin{aligned}
P(-1 \leq Z \leq 1) &= \Phi (1) - \Phi (-1) \\
  &= \Phi (1) - (1 - \Phi (1)) \\
  &= 2 \Phi (1) - 1 \\
  &= \cdots
\end{aligned}
$$

```python
x.has_prob_range_F(x1=2.9, x2=3.9)
```

```
0.6826
```

**(b)** The probability $P(X \leq 4) = P(Z \leq z)$, where $z$ is

```python
x.has_z(x=4)
```

```
1.2
```

Therefore, the probability $P(X \leq 4) = \Phi (1.2) = \cdots$

```python
x.has_F(x=4)
```

```
0.8849
```

**(c)** The probability $P(X \geq 3) = P(Z \geq z)$, where $z$ is

```python
x.has_z(x=3)
```

```
-0.8
```

Therefore, the probability $P(X \geq 3) = 1 - \Phi (-0.8) = 1 - (1 - \Phi (0.8)) = \Phi (0.8) = \cdots$

```python
x.has_F(x=3, greater_than=True)
```

```
0.7881
```
