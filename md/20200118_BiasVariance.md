---
title: "Why is te population variance biased?"
date: 2021-01-18
---

This is an annotated version of the proof in Example 7, Unit 7.
It uses Screencast 1 of Unit 7 as a template.

## Proposition

The estimator $E(W)$, where $W$ is

$$
E(W) = E\bigg\{\frac{1}{n} \bigg(\sum_{i=1}^{n} (X_{i} - \overline{X})^{2}\bigg)\bigg\}.
$$

is a biased estimator of the variance.

## Proof

Let us being by focusing on the sum of the squared deviations, $\sum_{i=1}^{n} (X_{i} - \overline{X})^{2}$.

We start with introducing $-\mu,- \mu = 0$.
We can do this as $\mu - \mu = 0$, so it doesn't change the results.
So

$$
\begin{aligned}
\sum_{i=1}^{n} (X_{i} - \overline{X})^{2} &= \sum_{i=1}^{n} (X_{i} - \mu - \overline{X} + \mu)^{2} \\
  &= \sum_{i=1}^{n} \{ (X_{i} - \mu) - (\overline{X} - \mu) \}^{2}.
\end{aligned}
$$

Now, recall that $(a+b)^{2} = a^{2} + 2ab + b^{2}$, so if we set $a =(X_{i} -\mu)$ and $b = (\overline{X} - \mu)$, then this becomes

$$
\begin{aligned}
\sum_{i=1}^{n} (X_{i} - \overline{X})^{2} &= \sum_{i=1}^{n} \{ (X_{i} -\mu)^{2} - 2(X_{i} -\mu)(\overline{X} - \mu) + (\overline{X} - \mu)^{2} \}.
\end{aligned}
$$

We can split the sum into three different sums, thus

$$
\begin{aligned}
\sum_{i=1}^{n} (X_{i} - \overline{X})^{2} &= \sum_{i=1}^{n} (X_{i} -\mu)^{2} - \sum_{i=1}^{n} 2(X_{i} -\mu)(\overline{X} - \mu) + \sum_{i=1}^{n}(\overline{X} - \mu)^{2}.
\end{aligned}
$$

We can simplify this further, by noting that the terms $2, \overline{X}, \mu$ are constants that do not rely on $i$, so can be moved outside of the sums.

$$
\begin{aligned}
\sum_{i=1}^{n} (X_{i} - \overline{X})^{2} &= \sum_{i=1}^{n} (X_{i} -\mu)^{2} - 2(\overline{X} - \mu) \sum_{i=1}^{n} (X_{i} -\mu) + n(\overline{X} - \mu)^{2}.
\end{aligned}
$$

Let us now focus in on the term $\sum_{i=1}^{n} (X_{i} -\mu)$.
We can again split the sum, so $\sum_{i=1}^{n} (X_{i} -\mu) = \sum_{i=1}^{n} X_{i} + \sum_{i=1}^{n} \mu$.
Using the fact that $\sum_{i=1}^{n} \mu = \mu \sum_{i=1}^{n} 1 = n\mu$, and also that

$$
\begin{aligned}
\sum_{i=1}^{n} X_{i} = \frac{n}{n} \sum_{i=1}^{n} X_{i} = n \frac{\sum_{i=1}^{n} X_{i}}{n} = n\overline{X},
\end{aligned}
$$

We can further simplify $\sum_{i=1}^{n} (X_{i} -\mu)$ to become $\sum_{i=1}^{n} (X_{i} -\mu) = n\overline{X} - n\mu = n(\overline{X} - \mu)$.

Let us substitute this in, and simplify as far as we can go

$$
\begin{aligned}
\sum_{i=1}^{n} (X_{i} - \overline{X})^{2} &= \sum_{i=1}^{n} (X_{i} -\mu)^{2} - 2(\overline{X} - \mu) \sum_{i=1}^{n} (X_{i} -\mu) + n(\overline{X} - \mu)^{2} \\
&= \sum_{i=1}^{n} (X_{i} -\mu)^{2} - 2(\overline{X} - \mu)n(\overline{X} - \mu) + n(\overline{X} - \mu)^{2} \\
&= \sum_{i=1}^{n} (X_{i} -\mu)^{2} - 2n(\overline{X} - \mu)(\overline{X} - \mu) + n(\overline{X} - \mu)^{2} \\
&= \sum_{i=1}^{n} (X_{i} -\mu)^{2} - 2n(\overline{X} - \mu)^{2} + n(\overline{X} - \mu)^{2} \\
&= \sum_{i=1}^{n} (X_{i} -\mu)^{2} - n(\overline{X} - \mu)^{2}
\end{aligned}
$$
