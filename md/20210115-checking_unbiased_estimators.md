## Proposition

Let $X_{i}$ be a collection of size $n$ of random variables with means $\gamma_{i} \mu$, where $\gamma_{i}$ are some arbitrary known constants, and $i \in 1,2,\ldots,n$.
Also let $\widehat \mu$ be some other estimator for the mean, such that

$$
\widehat \mu = \frac{1}{k}\sum_{i}^{n} c_{i} X_{i},
$$

where $c_{i}$, $k$ are some other arbitrary constants. Then $\widehat \mu$ is an **unbiased estimator** of $\mu$ if and only if

$$
k = \sum_{i}^{n}c_{i} \gamma_{i}.
$$

## Proof

Let $X_{i}$ be a collection of size $n$ of random variables with means $\gamma_{i} \mu$, where $\gamma_{i}$ are some arbitrary known constants, and $i \in 1,2,\ldots,n$.
Also let $\widehat \mu$ be some other estimator for the mean, such that

$$
\widehat \mu = \frac{1}{k}\sum_{i}^{n} c_{i} X_{i},
$$

where $c_{i}$, $k$ are some other arbitrary constants.

It is known that if $\widehat \mu$ is an unbiased estimator of $\mu$, then

$$
E(\widehat \mu) =  \mu.
$$

Therefore it must be that

$$
\begin{aligned}
\mu &= E\bigg\{ \frac{1}{k} \sum_{i}^{n} c_{i} X_{i} \bigg\} \\
  &= \frac{1}{k} E\bigg\{ \sum_{i}^{n} c_{i} X_{i} \bigg\} \\
  k \mu &= E\{c_{1}X_{1} + \cdots + c_{n}X_{n}\} \\
  &= E(c_{1}X_{1}) + \cdots + E(c_{n}X_{n}) \\
  &= c_{1} E(X_{1}) + \cdots + c_{n} E(X_{n}) \\
  &= c_{1} \gamma_{1} \mu + \cdots + c_{n} \gamma_{n} \mu \\
  k\mu &= \mu (c_{1} \gamma_{1} + \cdots c_{n} \gamma_{n}) \\
  k &= \sum_{i}^{n}c_{i} \gamma_{i}.
\end{aligned}
$$

## Examples

### (1)

> Each of the independent random variables $X_{1}$, $X_{2}$ and $X_{3}$ has mean $\mu$.
>
> Consider the estimator
>
> $$
> \widehat \mu = \frac{1}{8}(2X_{1} + 3X_{2} + 4X_{3}),
> $$
>
> Is $\widehat \mu$ an unbiased estimator of $\mu$?
>
> (Practice quiz 7, q2)

For $\widehat \mu = \frac{1}{k}\sum_{i}^{n} c_{i} X_{i}$ to be an unbiased estimator of $\mu$, it must be that

$$
k = \sum_{i}^{n}c_{i} \gamma_{i}.
$$

Here, let $c_{i} = 2, 3, 4$, $\gamma_{i} = 1$, and $k=8$. Then

$$
2(1) + 3(1) + 4(1) = 9\neq 8.
$$

Therefore $\widehat \mu$ is not an unbiased estimator, as $k \neq \sum c_{i} \gamma_{i}$.

### (2)

> Suppose that $X_{1}$, $X_{2}$ and $X_{3}$ independent random variables such that $X_{1} \sim N(\theta, \sigma^{2})$, $X_{2} \sim N(2\theta, \sigma^{2})$ and $X_{3} \sim N(3\theta, \sigma^{2})$.
>
> Consider the estimator
>
> $$
> \widehat \theta = \frac{1}{3}(X_{1} + X_{2} + X_{3}),
> $$
>
> Is $\widehat \theta$ an unbiased estimator of $\theta$?
>
> (Practice quiz 7, q6)

For $\widehat \theta = \frac{1}{k}\sum_{i}^{n} c_{i} X_{i}$ to be an unbiased estimator of $\theta$, it must be that

$$
k = \sum_{i}^{n}c_{i} \gamma_{i}.
$$

Here, let $c_{i} = 1$, $\gamma_{i} = 1, 2, 3$, and $k=3$. Then

$$
1(1) + 1(2) + 1(3) = 6 \neq 3.
$$

Therefore $\widehat \theta$ is not an unbiased estimator, as $k \neq \sum c_{i} \gamma_{i}$.

### (3)

> Three independent random variables, $X$, $Y$ and $Z$, are such that the mean of $X$ is $4\theta$, the mean of $Y$ is $2\theta$, and the mean of $Z$ is $\theta$.
>
> Consider the estimator
>
> $$
> \widehat \theta = \frac{1}{8}(X + Y + 2Z),
> $$
>
> Is $\widehat \theta$ an unbiased estimator of $\theta$?
>
> (Practice quiz 7, q7)

For $\widehat \theta = \frac{1}{k}\sum_{i}^{n} c_{i} X_{i}$ to be an unbiased estimator of $\theta$, it must be that

$$
k = \sum_{i}^{n}c_{i} \gamma_{i}.
$$

Here, let $c_{i} = 1,1,2$, $\gamma_{i} = 4,2,1$, and $k=8$. Then

$$
1(4) + 1(2) + 2(1) = 8 = 8.
$$

Therefore $\widehat \theta$ is an unbiased estimator, as $k = \sum c_{i} \gamma_{i}$.
