# Automating M248

The purpose of this note is to provide a list of references for my study of **M248: Analysing data**.
There would be little utility is reproducing the notes, given that the Open University already provides a fantastic source of notes in the Handbook and the study text.

The example links direct to a computer activity completed in `Python`.
They provide little use to the study of **M248** (given that the module uses **Minitab**), and is so mainly for interest and colour.
They were written using **Atom + Hydrogen**, as I found Jupyter notebook irritating to version control in GitHub.
They could also be used with some other IDE, such as Spyder.

## Data

### Summarising data

?> This section is served by two examples.
See
[Computer activity A14]([href](https://github.com/ljk233/AutomatingM248/blob/master/Python/a_14_summarising_data.py))
and
[Computer activity A15]([href](https://github.com/ljk233/AutomatingM248/blob/master/Python/a_15_summarising_data.py))

**Sample mean** (HB.p6. U1.4.1. CA3.)

**Sample median** (HB.p6. U1.4.1. CA3.)

**Sample quartiles** (H.pp6. U1.4.2. CA3.)

**Sample IQR** (HB.p6. U1.4.3. CA3.)

**Sample standard deviation** (HB.p6. U1.4.3. CA3.)

### Visualising data

**Bar charts** (HB.p5. U1.3.1. CA1.2.)
See
[Computer Activity A04](https://github.com/ljk233/AutomatingM248/blob/master/Python/a_04_bar_chart.py)
and
[Computer Activity A06](https://github.com/ljk233/AutomatingM248/blob/master/Python/a_06_bar_chart.py)

**Frequency histograms** (HB.p5. U1.3.2. CA2.1.)
See
[Computer Activities A08 and A09](https://github.com/ljk233/AutomatingM248/blob/master/Python/a_08_09_freq_hist.py)

**Boxplots** (HB.p5. U1.3.3. CA2.2.)
See
[Computer Activity A11 and A12](https://github.com/ljk233/AutomatingM248/blob/master/Python/a_11_12_boxplot.py)

**Side-by-side bar charts** (HB.p5. U1.5.1. CA4.1.)
See
[Computer Activity A16](https://github.com/ljk233/AutomatingM248/blob/master/Python/a_16_side_by_side_bar_chart.py)

**Unit-area histograms** (HB.p5. U1.5.2. CA4.2.)
See
[Computer Activity A17](https://github.com/ljk233/AutomatingM248/blob/master/Python/a_17_unit_area_hist.py)

**Comparative boxplots** (HB.p5; U1.5.3; CA4.3).
See
[Computer Activity A19](https://github.com/ljk233/AutomatingM248/blob/master/Python/a_19_comparative_boxplots.py)

**Scatterplots** (HB.p6; U1.5.4; CA4.4).
See
[Computer Activity A23](https://github.com/ljk233/AutomatingM248/blob/master/Python/a_23_scatterplot.py)

## Probability

### Discrete random variables

?> This section is served by one example.
See
[Additional example: Discrete random variables](https://github.com/ljk233/AutomatingM248/blob/master/Python/x_01_discrete_rv.py)

**Definition of discrete random variables (rvs)** (HB.p7. U2.2.1.)

**Probability mass functions (p.m.f.)** (HB.p7. U2.2.2.)

**Checking the validity of a p.m.f.** (HB.p7. U2.2.2.)

**Cumulative distribution function (c.d.f.) of a discrete rvs** (HB.p7. U2.4.2.)

**Mean of discrete rvs** (HB.p9. U4.1.1.)

**Variance of discrete rvs** (HB.p9. U4.3.1.)

**Population quantiles of discrete rvs** *(inverse c.d.f.)* (HB.p11. U5.4.2.)

### Continuous random variables

?> This section is served by one example.
See
[Additional example: Continuous random variables](https://github.com/ljk233/AutomatingM248/blob/master/Python/x_02_continuous_rv.py)

**Definition of a continuous rvs**

**Probability density functions (p.d.f.)** (HB.p7. U2.2.3. and U2.3.2)

**Checking the validity of a p.d.f.** (HB.p7. U2.3.3.)

**c.d.f. of a continuous rvs** (HB.p7. U2.4.3.)

**Mean of a continuous rvs** (HB.p9. U4.2.)

**Variance of a continuous rvs** (HB.p9. U4.4.)

**Population quantiles of continuous rvs** *(inverse c.d.f.)* (HB.p11. U5.4.1.)

### Standard probability models

?> See HB.p26 for table of formulas for the standard distributions.

**Bernoulli distributions** (*About*: HB.p7. U3.1.1; *Mean and variance*: U4.1.2. and U4.3.2).

**Binomial distributions** (*About*: HB.p8. U3.2.1; *Mean and variance*: U4.1.2. and U4.3.2).
See [Example: Binomial distribution](https://github.com/ljk233/AutomatingM248/blob/master/Python/x_03_binomial.py)

**Exponential distributions** (*About*: HB.p10. U5.2.1).
See [Example: Exponential distribution](https://github.com/ljk233/AutomatingM248/blob/master/Python/x_04_expon.py)

**Geometric distributions** (*About*: HB.p8. U3.3.1; *Mean and variance*: U4.1.2. and U4.3.2).
See [Example: Geometric distribution](https://github.com/ljk233/AutomatingM248/blob/master/Python/x_05_geom.py)

**Poisson distributions** (*About*: HB.p8. U3.4; *Mean and variance*: U4.1.2. and U4.3.2).
See [Example: Poisson distribution](https://github.com/ljk233/AutomatingM248/blob/master/Python/x_06_poiss.py)

**Uniform (continuous) distributions** (*About*: HB.p8. U3.5.2).
See [Example: Continuous uniform distribution](https://github.com/ljk233/AutomatingM248/blob/master/Python/x_07_cont_unif.py)

**Uniform (discrete) distributions** (*About*: HB.p8. U3.5.1; *Mean and variance*: U4.1.2. and U4.3.2).
See [Example: Discrete uniform distribution](https://github.com/ljk233/AutomatingM248/blob/master/Python/x_08_disc_unif.py)

**Uniform (standard) distributions** (*About*: U3.5.3).
*See uniform (continuous).*

### Linear transformations of random variables

**Linear transformations of random variables** (HB.p9. U4.5.)

## Modelling events occurring at random over time

**Poisson's approximation of rare events** (HB.p10. U5.1).
See [Example: Poisson's approximation](https://github.com/ljk233/AutomatingM248/blob/master/Python/x_09_poisson_approx.py)

**Bernoulli process** (HB.p10. U5.2.1).
See [Example: Bernoulli process](https://github.com/ljk233/AutomatingM248/blob/master/Python/x_10_bernoulli_process.py)

**Poisson process** (HB.p10. U5.3. CA10).
See [Example: Poisson process](https://github.com/ljk233/AutomatingM248/blob/master/Python/x_11_poisson_process.py)

**Is the Poisson process a good model** (HB.p10. U5.3.2. CA10)
See [Computer Activity A38](https://github.com/ljk233/AutomatingM248/blob/master/Python/a_38.py)
and
[Computer Activities A39 and A40](https://github.com/ljk233/AutomatingM248/blob/master/Python/a_39_40.py)

## Normal distributions

## Estimation

### Point estimation

### Interval estimation

## Hypothesis testing
