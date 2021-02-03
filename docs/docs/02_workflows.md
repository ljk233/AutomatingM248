# Common Workflows

Add some introductory blurb here.

## Checking the validity of a probability function

**Use case:** We are given some probability distribution (either a p.m.f. or a p.d.f.), and we are asked to confirm it is valid.

**Workflow:**
Check if the properties hold true.

For a p.m.f. of a discrete rv

1. $\sum_x p(x) = 1$
2. $p(x) \in (0,1],$

and for a p.d.f. of a continuous rv

1. $\int f(x) = 1$, over the range of $x$
2. $f(x) \in (0,1)$

## Using standard probability models

**Use case**: We are given a scenario, and asked to calculate the probability of some event.

**Workflow:**

1. Identify the distribution
2. Map the parameters
3. Parse the probabilities
4. Solve the equation(s)
5. State the solution, and the level of any approximation

## Calculating population quantiles in the continuous case

**Use case**: We are given a p.d.f. $f(x)$ or c.d.f. $F(x)$, and asked to calculate some $\alpha-$quantile of the distribution.

**Workflow**:

1. Find the c.d.f. by integrating $F(x) = \int_{a}^{x} f(y) dy$, if it is not gien in the question.
2. Identify the needed quantile in terms of a $\alpha \in (0,1)$.
3. Solve $q_{\alpha} = F^{-1}(\alpha)$.

## Poisson process

**Use case**: We are given some process that occurs in real time with a rate $\lambda$, and asked to identify the probability of some event occuring within some time interval.

**Workflow**:

1. **Formalise the rate $\lambda$.** Pay attention to the unit of time.
2. **Determine the rate $\lambda t$ of the scenario.** It will be $\lambda$ if the events are being modelled over the *same* time interval to the given rate in the question, and $\lambda t$ if it is a *different* time interval to that given in the scenario.
3. **Parse the probability.**
4. **Number of events $X$.** Use $X \sim \text{Poisson}(\lambda t)$
5. **Waiting time $T$ between events.** Use $T \sim M(\lambda)$., do not use the scaled $\lambda t$.
