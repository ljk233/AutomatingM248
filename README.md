# AutomatingM248

Python Calculators for OU M248: Analysing Data.
Built with Python 3.8.3. Uses variable typing.
Built and tested in VSCode.

-----

## Prbability calculator for standard discrete distribution

Generates a distribution with the given parameters.
Distributions currently supported:

- Binomial (`Binomial(n, p)`)
- Geometric (`Geometric(p)`)
- Poisson (`Poisson(mu)`)
- Discrete Uniform (`DiscreteUniform(m, n)`)

### Guide

1. Declare the distribution: `distribution = Distribution(args)`
2. Calculate probabilities: `distribution.calculateProbabilty()`
3. Display summary statistic: `distribution.displaySummary()`
