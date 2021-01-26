---
title: Attaining the cumulative distribution function of an exponential distribution
date: 2020-12-28
ref: 
---

This note was made in response to a post on the M248 forum:
[Unit 5 Section 3.1](https://learn2.open.ac.uk/mod/forumng/discuss.php?d=3495996)

## Method 1

The definition of the c.d.f. of a continuous distribution[^1] is

$$
F(t) = \int_{L}^{t} f(x) \> dx, \hspace{2mm} t \in (L, U).
$$

Now, an exponential distribution has range $x>0$[^2] and p.d.f.[^3] $f(x) = \lambda e^{-\lambda x}$.
Therefore the c.d.f. of an exponential distribiution will be

$$
\begin{aligned}
    F(t) = \int_{L}^{t} f(x) \> dx &= \int_{0}^{t} \lambda e^{-\lambda x} \> dx \\
      &= \bigg[ \frac{\lambda}{-\lambda} e^{-\lambda x} \bigg]^{t}_{0} \\
      &= -(e^{-\lambda t} - e^{0}) \\
      &= -(e^{-\lambda t} - 1) \\
      &= 1 - e^{-\lambda t}.
\end{aligned}
$$

## Method 2

We can also reach this result using the **Poisson distribution**.
The probability that the time $T$ between two events $X$ is less than $t$ is equivalent to the probability that at least one event happens in time $t$.
Given that $X$ is a Poisson random variable with distrubtion $X \sim \text{Poisson}(\lambda t)$[^3] then

$$
P(T>t) \equiv P(X>0).
$$

The probability $P(X>0) = 1 - P(X \leq 0) = P(X=0)$, given that the range of $X$ is $\{0, 1, 2, \ldots\}$,[^2] so

$$
1 - P(X \leq 0) = 1 - P(X=0),
$$

where

$$
P(X=0) = e^{-\lambda t} \bigg( \frac{(\lambda t)^{0}}{0!} \bigg) = e^{-\lambda t}.
$$

And so finally

$$
P(T>t) \equiv 1 - P(X=0) = 1 - e^{-\lambda t}.
$$

[^1]: HB pp 7
[^2]: HB pp 26-27
[^3]: HB pp 10
