---
title: Lateral flow tests and Bayes theorem
date: 2020-12-28
ref: 
---

## Statement of Bayes' Theorem

> Bayes' theorem is stated mathematically as the following equation:
>
> $$
> P(A \>| \> B) = \frac{P(B \>| \> A)P(A)}{P(B)},
> $$
>
> where $A$ and $B$ are events and $P(B) \neq 0$.
>
> - $P(A \>| \> B)$ is a conditional probability: the likelihood of event $A$ occurring given that $B$ is true.
> - $P(B \>| \> A)$ is also a conditional probability: the likelihood of event $B$ occurring given that $A$ is true.
> - $P(A)$ and $P(B)$ are the probabilities of observing $A$ and $B$ respectively; they are known as the marginal probability.
>
> $A$ and $B$ must be different events.

Reference: *[Bayes' theorem (Wikipedia)](https://en.wikipedia.org/wiki/Bayes%27_theorem).*

## Stating the question and clarifying the terms

What is the probability that a person is positive for Covid-19, given they return a positive LFT?

This is $P(\text{Has C19} \> | \> \text{Positive result})$.
Mapping the terms to Bayes' Theorem states as stated above, let

- Has C19 $= C+ \to A$;
- Positive test $= +ve \to B$.

So therefore the probability $P(\text{Has C19} \> | \> \text{Positive result})$, otherwise known as the **Positive Predictive Power**,[^6] is

$$
P(C+ \> | \> +ve) = \frac{P(+ve \> | \> C+) \> P(C+)}{P(+ve)}
$$

## Sourcing the data

The $P(+ve \> | \> C+)$ is the **sensitivity** of the LFT,[^1] which is approximately 76.8%.[^2]

It has been estimated[^3] that the percentage of the population in England with Covid-19, $P(C+)$, in the week 12 to 18 December 2020 was approximately 1.17%.
This means that the population in England without Covid-19, $P(\text{Not } C+)$, was approximately 98.83%

The probability $P(+ve) = P(+ve \> | \> C+) \> P(C+) + P(+ve \> | \> \text{Not } C+) \> P(\text{Not } C+)$.[^4]
The probability $P(+ve \> | \> \text{Not } C+)$ is the **false positive rate** of the LFT, which was found to be approximately 0.38%.[^5]

## Calculating the probability

Now that we have the needed figures, let us calculate the probability that a person is positive for Covid-19, and returns a positive LFT,

$$
\begin{aligned}
    P(C+ \> | \> +ve)
      = \frac{P(+ve \> | \> C+) \> P(C+)}{P(+ve)}
      &= \frac{P(+ve \> | \> C+) \> P(C+)}{P(+ve \> | \> C+) \> P(C+) + P(+ve \> | \> \text{Not } C+) \> P(\text{Not } C+)} \\
      &= \frac{0.768(0.0117)}{0.768(0.0117) + 0.0038(0.9883)} \\
      &= 0.70524\ldots \simeq 0.705.
\end{aligned}
$$

Hence, the positive predictive power of the LFT in the week 12-18 December 2020 was approximately 70.5%.

## Caveat on the sensitivity

The sensitivity of the test was stated as 76.8%.
This is the *overall* sensitivity of the test.
However, the sensitivity dropped to 58% when used by *"self-trained staff at a Boots track-and-trace centre".*[^5]

Using this other figure for the sensitivity would mean the PPV of the LFT would fall to approximately 64.4% in the week quoted!

[^1]: This is the true positive rate
[^2]: *"The findings contrast with an earlier assessment of the Innova test by Public Health England’s Porton Down laboratory and the University of Oxford, which found an overall sensitivity of 76.8%."* [Covid-19: Lateral flow tests miss over half of cases, Liverpool pilot data show. BMJ](https://www.bmj.com/content/371/bmj.m4848)
[^3]: *"The number of people with the coronavirus (COVID-19) in England has increased, with 645,800 people estimated to have had COVID-19 in the most recent week (12 to 18 December 2020). This equates to 1 in 85 people."* [Coronavirus \(COVID-19\) roundup. ONS](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/articles/coronaviruscovid19roundup/2020-03-26)
[^4]: *"The* $P(\text{Positive}) = \ldots$ *is a direct application of the **Law of total probability.**"* [Bayes' theorem. Wikipedia](https://en.wikipedia.org/wiki/Bayes%27_theorem)
[^5]: *"The report said that the test’s sensitivity was 58% when used by the public and that the false positive rate was 0.38%"* [Covid-19: Innova lateral flow test is not fit for “test and release” strategy, say experts. BMJ](https://www.bmj.com/content/371/bmj.m4469#:~:text=The%20overall%20specificity%20of%20the,interval%2072.8%25%20to%2084.6%25)
[^6]: *The Positive predictive value (PPV) of a test is the proportion of persons who are actually positive out of all those testing positive.* [Bayes' theorem. Wikipedia](https://en.wikipedia.org/wiki/Bayes%27_theorem).
