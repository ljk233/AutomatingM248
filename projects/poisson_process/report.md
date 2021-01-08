---
Title: A worked example of the Poisson process
Created: 2020-12-29
---

Outline

1. Scenario
2. Describing the data
3. Confirming the Poisson process
   1. Number of emails per hour
   2. Waiting time between emails
4. Estimating the rate, $\lambda$
   1. Point estimate
   2. Interval estimate
5. Using the model

-----

## 1. Scenario

## 2. Defining the terms

Let $X$ be a random variable that models the number of emails received, with range $0, 1, 2, \ldots$.
We would expect this to be similar to the Poisson p.m.f.

Let $T$ be a random variable that represents the time (in hours) between successive emails.
We would expect this to be similar to the exponential p.d.f.

## 3. Describing the data

## 4. Does the data fit the Poisson process

### 4.1 Rate of occurrence remains constant over time

Data can be modelled by the **Poisson process** if it meets the following criteria:[^1]

- Events occur singly;
- The rate of occurrence of events remains constant;
- The incidence of future events is independent of the past.

Let us assume that the data meets the first criteria. The second and third criteria can be checked by a single graph: *Is the average rate of emails received constant over the time period*?[^2]

![](assets/fig1.svg)

**Figure 1**. Rate of emails over time

The $x-$axis shows the time, in hours, that has passed; the $y-$axis shows the event number.[^3]

We can see that the points lie approximately along a straight line, indicating that the rate of events remained constant over time.
This suggests that the Poisson process is indeed a suitable model for the scenario.

### 4.2 Frequency of $X$

Another property that we must confirm is that the **X** is approximately a Poisson distribution.[^1][^2]

We can confirm this by comparing the frequency of $x_{i} \in X$ with that of the Poisson probability mass function of $\text{Poisson}(\lambda_{X})$, where $\lambda_{X}$ is the mean of the frequency of each distinct number of emails per hour.

The data was aggregated, producing a new view that showed the number of emails received per hour per day. From this, we then calculated $f_{X}$.[^4]

![](assets/fig2.svg)

**Figure 2**. Frequency of $X$.

The plot in **Figure 2** is unimodal and is approximately symmetrical.
This indicates that the distribution could be modelled by a **Poisson distribution**, with a parameter $\lambda \simeq $.

The Poisson distribution has the property that its mean is equal to its variance.[^ref]
The sample mean of the number of emails per hour is approximately $13.6$, and the variance is $13.96$.

These two figures are close enough that we can say they are approximately equal, so we can conclude that the distribution of the *number of emails per hour* is approximately Poisson.

### 4.3 Waiting times between emails

The final property of the Poisson process that we must confirm is that the **waiting times between emails**, $T$, is approximately an exponential distribution.[^1][^2][^5]

![](assets/fig3.svg)

**Figure 3**. Waiting time between sucessive emails.

The histogram is highly right-skewed with a high density of low values, as is expected by an exponential distribution.

This can be further supported by checked if the mean waiting time is approximately equal to the standard deviation.
The sample mean waiting time is $\overline t \simeq 0.073$ with standard deviation $\sigma_{T} \simeq 0.072$.
These two figures are close enough that we can say they are approximately equal, so we can conclude that the distribution of the waiting time between emails is indeed approximately exponential.

## 5. Estimating the rate of emails of hours $\widehat \lambda$

### 5.1 Number of emails per hour

We confirmed it is possible the number of emails per hours could be modelled by the **Poisson distribution**, with parameter $\lambda_{X}$ being the expected number of emails per hour.

The maximum likelihood estimator of the Poisson distribution is given by $\widehat \lambda_{X} = \overline X$.[^6]
We calculated $\overline X \simeq 13.6$, so we propose that the number of emails per hour, $X$, can be modelled by a Poisson distribution, $X \sim \text{Poisson}(\widehat \lambda_{X})$, where $\widehat \lambda_{X} = \overline X \simeq 13.6$.

### 5.2 Waiting time between emails

We confirmed it is possible the waiting time between emails in unit hours could be modelled by the **exponential distribution**, with parameter $\lambda_{T}$.

The maximum likelihood estimator of the exponential distribution is given by $\widehat \lambda_{T} = 1 / \overline T$, where $\overline T$ is the average waiting time between emails in unit hours.[^6]
We calculated $\overline T \simeq 0.073$, so we propose that the waiting time between emails in unit hours, $T$, can be modelled by an exponential distribution distribution, $T \sim M(\widehat \lambda_{T})$, where $\widehat \lambda_{T}  \overline T \simeq 13.6$.

### 5.3 Estimating $\widehat \lambda$ with 95% confidence

We can produce a more useful estimate by calculating the 95% confidence interval for $\widehat \lambda$.[^7]
An approximate large sample $100(1 − \alpha)\%$ confidence interval for the Poisson parameter $\lambda$ is

$$
(\lambda^{-}, \lambda^{+}) = \bigg(\overline x - z \sqrt{\frac{\overline x}{n}}, \overline x + z \sqrt{\frac{\overline x}{n}}\bigg)
$$

where $\overline x$ is the **sample mean**, and $z$ is the $(1 − (\alpha/2))-$quantile of the standard normal distribution.[^ref]

We know that $\overline x \simeq 13.6$ and $n=731$ (the number of hours in the sample), so[^8]

$$
\begin{aligned}
   \lambda^{-} &\simeq 13.6 - 1.96 \sqrt{\frac{13.6}{731}} = 13.3657 \ldots \\
   \lambda^{+} &\simeq 13.6 + 1.96 \sqrt{\frac{13.6}{731}} = 13.9010 \ldots \\
\end{aligned}
$$

Therefore the 95% confidence interval for this data is approximately $(13.4, 13.9)$.

## 6. Conclusion

In this report, we took a large dataset containing approximately 10,000 observations of the date and time of the receipt of an email by a company.
The company was interested in modelling the number of emails they received per hour, and the waiting time between successive emails.
It was confirmed that the sample could be modelled by a **Poisson process**. This confirmation was used to calculate the maximum likelihood estimators of the Poisson and exponential parameters to ascertain $\widehat \theta$.
We also calculated the 95% confidence interval for estimate.

[^1]: M248 Book A5.3.
[^2]: M248 Computer book A10.1
[^3]: See **(3)** in support notebook.
[^4]: See **(2)** in support notebook.
[^5]: See **(4)** in support notebook.
[^6]: M248 Book B.7.4
[^7]: M248 Book B8.3
[^8]: See **(6)** in support notebook.
