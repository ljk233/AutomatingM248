
# README

## `m248.Discrete`

A class to model a small discrete random variable.

### Parameters

### Constructor

`Discrete(x: list[int], pr: list[int]) -> None`
: Constructor for objects of type Discrete.
Assigns arg `x`, `p` and object's `X`, `Pr` respectively.

: @params
: `x`
:: A list of integers that represents the range of X.

: `pr`
:: A list of floats that represents the Pr(X = x).
Element `pr[i]` should correspond the the Pr of `x[i]` occuring.

### Methods

`get_pmf()`
