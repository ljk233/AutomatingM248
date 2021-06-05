
calc_test_power <- function(a, d, sd, n, one_sided) {
  #' @description       calculates the power of a test.
  #'
  #' @param a           alpha, significance level
  #' @param d           difference between true and hypothesised means
  #' @param sd          known population standard deviation
  #' @param n           sample size
  #' @param one-sided   boolean, TRUE if one-sided, else FALSE

  if (one_sided) {
    q <- qnorm(1-a)
  } else {
    q <- qnorm(1-a/2)
  }

  return (
    1 - pnorm(q - d/(sd/sqrt(n)))
  )
}


calc_sample_size <- function(a, d, sd, pow_, one_sided) {
  #' @description       calculates the required sample size of a test.
  #'
  #' @param a           alpha, significance level of test
  #' @param d           difference between true and hypothesised means
  #' @param sd          known population standard deviation
  #' @param pow_        power of the test (a percentage)
  #' @param one-sided   boolean, TRUE if one-sided, else FALSE

  if (one_sided) {
    q <- qnorm(1-a)
  } else {
    q <- qnorm(1-a/2)
  }

  qp <- qnorm(1-pow_/100)

  return (
    sd/d**2 * (q - qp)**2
  )
}


calc_chi_sq <- function(obs, exp) {
  #' @description   calculates the chi-sq test statistic
  #'
  #' @param obs     a vector of observed results
  #' @param exp     a vector of expected results

  return (
    sum(((obs-exp)**2)/exp)
  )
}


calc_slr_std <- function(sum_x = NULL, sum_y = NULL, sum_sq, n) {
  #' @description   calculates the value of Sxx, Syy, or Sxy
  #'                in simple linear regression.
  #'                
  #' @note          If calculating Sxy, then it is expected both sum_x
  #'                and sum_y will be passed as arguments.
  #'
  #' @param sum_x     sum of x, default is NULL
  #' @param sum_y     sum of y, default is NULL
  #' @param sum_sq    sum of x^2, y^2, or xy
  #' @param n         sample size


  if (!is.null(sum_x) & !is.null(sum_y)) {
    sum_ <- sum_x * sum_y
  } 
  else if (!is.null(sum_x)) {
    sum_ <- sum_x ** 2
  }
  else if (!is.null(sum_y)) {
    sum_ <- sum_y ** 2
  }
  else {
    return ('Please pass valid args')
  }

  return (
    sum_sq - sum_/n
  )
}


calc_conf_int_beta <- function(ci, b, n, Sxx, sd = NULL, var = NULL) {
  #' @description   calculate ci for beta. returns a vector.
  #'                
  #' @note          it is expected one of sd or var will be passed.
  #'                if both are passed, uses sd
  #'
  #' @param ci      float, confidence interval to return  
  #' @param b       theorised value of beta
  #' @param n       sample size
  #' @param Sxx     value of Sxx
  #' @param sd      standard deviation, default is NULL
  #' @param var     variance, default is NULL

  if (!is.null(sd)) {
    ese <- sd/sqrt(Sxx)
  } 
  else if (!is.null(var)) {
    ese <- sqrt(var/Sxx)
  }
  else {
    return ('Please pass valid args')
  }

  qa <- (ci + (1 - ci)/2)  # transform ci to quantile
    
  t <- qt(qa, n-2)

  return (
    c(b - t*ese, b + t*ese)
  )
}


calc_pooled_sample_var <- function(v1, n1, v2, n2) {
  #' @description   calculates the pooled sample variance of two samples.
  #'                
  #' @param v1, v2  sample variances of samples 1 and 2 
  #' @param n1, n2  sizes of samples 1 and 2

  df <- n1 + n2 - 2
  num <- (n1-1)*v1 + (n2-1)*v2
  return (num/df)
}


tconfint_diff_means <- function(a, x1, n1, x2, n2, sp) {
  #' @description returns a 100(a)% t-interval for the difference
  #'              between two normal means.
  #'
  #' @param a       corresponds to 100(a)\%
  #' @param x1, x2  means of sample 1 and 2 
  #' @param n1, n2  sizes of samples 1 and 2
  #' @param sp      pooled sample standard deviation
  #' 
  #' @return a vector of the lower, upper boundaries

  d <- x1-x2
  dof <- n1+n2-2
  t <- qt(p = 1-(1-a)/2, df = dof)
  ese <- t*sp*sqrt(1/n1 + 1/n2)
  return (c(d - ese, d + ese))
}


calc_norm_approx_mann_whit <- function(u, nA, nB) {
  #' @description   returns the parameters of the normal approx of a
  #'                mann-whitney test, including the z-value.
  #'
  #' @param u       calculated test statistic
  #' @param nA, nB  sizes of samples A and B.
  #' 
  #' @return a vector (z, Eu, Vu)
  
  Eu <- nA*(nA + nB + 1)*0.5
  Vu <- nA*nB*(nA + nB + 1)*(1/12)
  z <- (u-Eu)/sqrt(Vu)
  return (c(z, Eu, Vu))
}


calc_norm_approx_wilcoxon <- function(w, n) {
  #' @description   returns the parameters of the normal approx of a
  #'                wilcoxon sign rank test, including the z-value.
  #'
  #' @param w       calculated test statistic
  #' @param n       sample size
  #' 
  #' @return a vector (z, Ew, Vw)
  
  Ew <- n*(n + 1)/4
  Vw <- (n*(n+1)*(2*n + 1))/24
  z <- (w-Ew)/sqrt(Vw)
  return (c(z, Ew, Vw))
}
