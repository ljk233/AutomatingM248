# Common Workflows

Add some introductory blurb here.

## Checking the validity of a probability function

Confirm the two properties of a valid probability mass or density function hold true.

### Discrete random variables

1. $\sum_x p(x) = 1$
2. $p(x) \in (0,1]$

### Continuous random variables

1. $\int f(x) = 1$, over the range of $x$
2. $f(x) \in (0,1)$

## Standard probability models

**Use case**: We are given a scenario, and asked to calculate the probability of some event.

**Workflow**:

1. Identify the distribution
2. Map the parameters
3. Parse the probabilities
4. Solve the equation(s)
5. State the solution, and the level of any approximation

**Example**. EasyAir charters 15 flights each day from Cardiff to Narnia. It has been reported by cabin crew that sky mermaids are spotted during 40% of flights.

For a particular day,

1. calculate the probability that 9 flights will spot sky mermaids.
2. calculate the probability that less than 3 flights will spot sky mermaids.

**Identify the distribution.**
This scenario is described a binomial distribution, $B(n,p)$.

**Map the parameters.**
There are 15 flights, so $n=15$; and 40% of flights spot sky mermaids, so $p=0.4$; thus $B(15, 0.4)$.

**Parse the probabilities.**
For (1) "*Exactly 9*" is $P(X=9) = p(9)$; and for (2) "*Less than 3*" is $P(X<3) = P(X \leq 2) = F(2)$

**Solve the equations** (See HB pp.26 for the need formulae).

For (1) $p(9) \backsimeq 0.06121$.

And for (2) $F(2) = p(0) + p(1) + p(2) \backsimeq 0.02711$.

**State the solutions, and the level of approximation.**

## Calculating population quantiles in the continuous case

**Use case**: We are given a p.d.f. $f(x)$ or c.d.f. $F(x)$, and asked to calculate some $\alpha-$quantile of the distribution.

**Workflow**:

1. If needed, find the c.d.f. by integrating $F(x) = \int_{a}^{x} f(y) dy$.
2. Identify the needed quantile in terms of a $\alpha \in (0,1)$.
3. Solve $q_{\alpha} = F^{-1}(\alpha)$.

**Example**: The c.d.f. of a random variable $X$ is given by

$$
F(x) = \frac{1}{8} (x^{2} - 1), \hspace{3mm} x \in  1,3).
$$

Calculate lower quartile of $X$.

**Find the c.d.f.**
This is given in the question, so $F(x) = \frac{1}{8} (x^{2} - 1)$.

**Identify the needed quantile.** The lower quartile is $q_{0.25}$, so $\alpha = 0.25$.

**Solve** $q_{\alpha} = F^{-1}(\alpha)$.
If $F(q_{\alpha}) = \frac{1}{8} (q_{\alpha}^{2} - 1)$, then

$$
\begin{aligned}
\frac{1}{8} (q_{\alpha}^{2} - 1) &= \alpha \\
q_\alpha &= \sqrt{8 \alpha + 1}.
\end{aligned}
$$

We know that $\alpha = 0.25$, so

$$
q_{0.25} = \sqrt{8(0.25) + 1} = \sqrt{3}.
$$

## Poisson process

**Use case**: We are given some process that occurs in real time with a rate $\lambda$, and asked to identify the probability of some event occuring within some time interval.

**Workflow**:

1. **Formalise the rate $\lambda$**. Pay attention to the unit of time.
2. **Determine the rate $\lambda t$ of the scenario.** It will be $\lambda$ if the events are being modelled *over the same time interval*, and it will $\lambda t$ if it is a different time interval.
3. **Parse the probability**.
4. **Number of events $X$**. Use $X \sim \text{Poisson}(\lambda t)$
5. **Waiting time $T$ between events**. Use $T \sim M(\lambda)$.

**Example.** Suppose that alpha particles are emitted from a radioactive source at random at an average rate of 0.5 every second.
Assume that the emissions of alpha particles may be modelled by a Poisson process.

1. Calculate the probability that more than 3 alpha particles will be emitted within a 5 second window.
2. Calculate the probability that the waiting time between emissions of alpha particles exceeds ten seconds.

**Formalise the rate $\lambda$.**
The rate $\lambda$ is 0.5 per second.

**Determine the rate for the timeframe.**
Alpha particle emissions may be modelled by a Poisson process with rate $\lambda = 0.5$ per second.
So $X$, the number of emissions in a five-second interval, will have a Poisson distribution with parameter $\lambda t = 0.5(5) = 2.5$.

**Parse the probability.**
For (1) *"More than 3"* is $P(X>3) = 1 - P(X \leq 3)$.
And for (2) *"Exceeds 10"* is $P(T>10) = 1 - P(T \leq 10) = 1 - F(10)$.

**Solve the equations**.

For (1), we use $X \sim \text{Poisson}(2.5)$, so

$$
\begin{aligned}
P(X > 3) = 1 - P(X \leq 3) =  e^{-2.5} \sum_{k=0}^{3} \frac{2.5^{k}}{k!} \backsimeq 0.00175,
\end{aligned}
$$

and for (2), we use $T \sim M(0.5)$, so

$$
\begin{aligned}
P(T > 10) = 1 - F(10) = 1 - (1 - e^{-0.5(10)}) = e^{-5} \backsimeq 0.0067.
\end{aligned}
$$
