---
title: "Further calculations involving lateral flow tests and Bayes theorem"
date: 2021-01-02
ref: 
---

This note was made in response to a follow-up post on the M248 forum:
[Covid19 tests and statistics](https://learn2.open.ac.uk/mod/forumng/discuss.php?d=3496734)

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

The question was stated as follows:

> *So, if I wanted to know the probability of a person being positive for covid given that they had a negative LFT test (...)*

This is $P(\text{Has C19} \> | \> \text{Negative result})$.
Mapping the terms to Bayes' Theorem states as stated above, let

- Has C19 $= C+ \to A$;
- Negative test $= -ve \to B$.

So therefore the probability $P(\text{Has C19} \> | \> \text{Neagtive result})$, is

$$
P(C+ \> | \> -ve) = \frac{P(-ve \> | \> C+) \> P(C+)}{P(-ve)}
$$

## Sourcing the data

The probability $P(-ve \> | \> \text{Not } C+)$ is the **specificity** of the LFT,[^1] which is approximately 99.6%,[^2] then[^5]

$$P(-ve \> | \> C+) = 100 - P(-ve \> | \> \text{Not } C+) \simeq 0.4\%.$$

It has been estimated[^3] that the percentage of the population in England with Covid-19, $P(C+)$, in the week 12 to 18 December 2020 was approximately 1.17%.
This means that the population in England without Covid-19, $P(\text{Not } C+)$, was approximately 98.83%

The probability[^4] $P(-ve)$ is given by

$$
\begin{aligned}
  P(-ve) &= P(-ve \> | \> C+) \> P(C+) + P(-ve \> | \> \text{Not } C+) \> P(\text{Not } C+) \\
  &\simeq 0.004(0.0117) + 0.996(0.983) \\
  &\simeq 0.979.
\end{aligned}
$$

## Calculating the probability

Now that we have the needed figures, let us calculate the probability that a person is positive for Covid-19, given they return a negative LFT,

$$
\begin{aligned}
    P(C+ \> | \> -ve)
      = \frac{P(-ve \> | \> C+) \> P(C+)}{P(-ve)}
      &\simeq \frac{0.004(0.017)}{0.979} \\
      &= 0.000069 \ldots.
\end{aligned}
$$

Hence, the probability of a person being positive for covid given that they had a negative LFT test is approximately 0.000069.

This is not a surprising result, given the LFT is highly specific.
It also points to a reason behind why much of the focus is on the sensitivity of the LFT, as opposed to specificity.

[^1]: This is the true negative rate.
[^2]: *"He said that, while 0.4% (400 in 100 000) was a very low rate, with a sensitivity of 58% and specificity of 99.6%"* [Covid-19: Lateral flow tests miss over half of cases, Liverpool pilot data show. BMJ](https://www.bmj.com/content/371/bmj.m4848)
[^3]: *"The number of people with the coronavirus (COVID-19) in England has increased, with 645,800 people estimated to have had COVID-19 in the most recent week (12 to 18 December 2020). This equates to 1 in 85 people."* [Coronavirus \(COVID-19\) roundup. ONS](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/articles/coronaviruscovid19roundup/2020-03-26)
[^4]: *"The* $P(\text{Positive}) = \ldots$ *is a direct application of the **Law of total probability.**"* [Bayes' theorem. Wikipedia](https://en.wikipedia.org/wiki/Bayes%27_theorem)
[^5]: This is because they are **mutually exlusive**: A person who returns a negative test can either have Covid-19 or not.
