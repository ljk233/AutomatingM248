---
title: "Sampling Distribution of an Estimator"
date: 2021-11-18
---

An estimator $\widehat \theta$ is a random variable, so it has a probability distribution.
This distribution is called the **sampling distribution of the estimator**,[^1][^7] and it will be:

[^1]: According to the CLT.
[^7]: Quoted from Unit 7, S1.2.

$$
\widehat \theta_{n} \approx N\bigg(\mu_{\widehat \theta}, \frac{\sigma^{2}_{\widehat \theta}}{n}\bigg).
$$

Now we know that the sample mean of $\widehat \theta$ is an unbiased estimator of $\mu_{\widehat \theta}$, but what do we know about the variance of $\widehat \theta$?
Looking closer at the distribution's variance, we can see that

$$
\frac{\sigma^{2}_{\widehat \theta}}{n}
  = \frac{1}{n} \sigma^{2}_{\widehat \theta} = E(\sigma^{2}_{\widehat \theta}).
$$

This is just the *expected value* of the variance of $\widehat \theta$.[^2]
So what value should we use for the variance of $\widehat \theta$?

[^2]: Compare this to $\sum X/n = E(X)$. It actually makes an interesting point about the CLT!

We are presented with two possible formulas[^6] for ascertaining the variance.[^3]
The first[^4] is a simple interpretation[^5] of what the variance is

$$
V^{2}_{\widehat \theta} = \frac{1}{n} \sum_{i=1}^{n}\{ (X_{i} - \overline X)^{2} \},
$$

and the second is the *sample variance*

$$
S^{2}_{\widehat \theta} = \frac{1}{n-1} \sum_{i=1}^{n}\{ (X_{i} - \overline X)^{2} \}.
$$

[^3]: Example 7, Unit 7.
[^4]: The example uses $W$ instead of $V^{2}$.
[^5]: The average squared deviation, known as the *population variance*.
[^6]: I have not specified $X$ in this note. It will just be a sample of data $X_{i} = \{X_{1}, X_{2}, \ldots , X_{n}\}$.

The example goes on to prove that $V^{2}_{\widehat \theta}$ is a **biased estimator** of the variance of a sample of data, and $S^{2}_{\widehat \theta}$ is an **unbiased estimator**.

All this means is, if we require the variance of some data, then we should use the **sample variance** $S^{2}$ rather than the population variance $V^{2}$.
