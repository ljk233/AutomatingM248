zconfint_mean <- function(a, x, sd, n) {
  #' @description returns a 100(a)% z-interval for a normal mean.
  #'
  #' @param a     corresponds to 100(a)%
  #' @param x     sample mean
  #' @param sd    sample standard deviation
  #' @param n     sample size
  #' 
  #' @return [mu-, mu+]

  z <- qnorm(1-(1-a)/2)
  ese <- z*(sd/sqrt(n))
  return (c(x - ese, x + ese))
}
  
zconfint_prop <- function(a, x, n) {
  #' @description returns a 100(a)% z-interval for a population proportion.
  #'
  #' @param a a numeric value between 0-1
  #' @param x number of successes
  #' @param n sample size
  #' 
  #' @return [p-, p+]

  p <- x/n; q <- 1-p; z <- qnorm(1-(1-a)/2)
  ese <- z*sqrt((p*q)/n)
  return (c(p - ese, p + ese))
}

zconfint_diff_props <- function(a, x1, n1, x2, n2) {
  #' @description returns a 100(a)% z-interval of the difference between two
  #' population proportions.
  #'
  #' @param a   corresponds to 100(a)\%
  #' @param x1  number of successes in the first sample
  #' @param n1  sample size of the first sample
  #' @param x2  number of successes in the second sample
  #' @param n2  sample size of the second sample
  #' 
  #' @return [p-, p+]

  p1 <- x1/n1; q1 <- 1-p1;
  p2 <- x2/n2; q2 <- 1-p2;
  d <- p1 - p2
  z <- qnorm(1-(1-a)/2)
  ese <- z*sqrt((p1*q1)/n1 + (p2*q2)/n2)
  return (c(d - ese, d + ese))
}

tconfint_mean <- function(a, x, sd, n) {
  #' @description returns a 100(a)% t-interval for a normal mean.
  #'
  #' @param a     corresponds to 100(a)\%
  #' @param x     sample mean
  #' @param sd    sample standard deviation
  #' @param n     sample size
  #' 
  #' @return [mu-, mu+]

  t <- qt(p = 1-(1-a)/2, df = n-1)
  ese <- t*(sd/sqrt(n))
  return (c(x - ese, x + ese))
}

tconfint_diff_means <- function(a, x1, sd1, n1, x2, sd2, n2) {
  #' @description returns a 100(a)% t-interval for the difference
  #'              between two normal means.
  #'
  #' @param a     corresponds to 100(a)\%
  #' @param x1    mean of sample 1
  #' @param sd1   std.dev of sample 1
  #' @param n1    size of sample 1
  #' @param x2    mean of sample 2
  #' @param sd2   std.dev of sample 2
  #' @param n2    size of sample 2
  #' 
  #' @return [d-, d+]
  d <- x1-x2
  dof <- n1+n2-2
  t <- qt(p = 1-(1-a)/2, df = dof)
  pooled_var <- ((n1-1)*(sd1**2) + (n2-1)*(sd2**2))/dof
  ese <- t*sqrt(pooled_var)*sqrt(1/n1 + 1/n2)
  return (c(d - ese, d + ese))
}
