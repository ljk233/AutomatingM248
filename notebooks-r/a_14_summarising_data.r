
# =============================================================================
# References
# ==========
#
# Computer activity A.14
#
# Summarising data
# - Sample mean (HB.pp6; U1.4.1; CA3).
# - Sample median (HB.pp6; U1.4.1; CA3).
# - Sample quartiles (HB.pp6; U1.4.1; CA3).
# - Sample IQR (HB.pp6; U1.4.1; CA3).
# - Sample standard deviation (HB.pp6; U1.4.1; CA3).
#
# Use Pandas to calculate numerical summaries of some data.
#
# =============================================================================

library(tidyverse)

# import the data
x <- read.csv("./data/response-inhibition.csv")

# preview the data.frame
head(x)

# =============================================================================
# output a simple table of summary measures
# Two methods to compile a summary table.
# =============================================================================

# Method 1
summary(x["Weight.change"])

# Method 2, using dplyr
data <- as_tibble(x)

x %>%
  summarise(count = n() - sum(is.na(Weight.change)),
            count.na = sum(is.na(Weight.change)),
            mean = mean(x = Weight.change, na.rm = TRUE),
            q1 = quantile(x = Weight.change, na.rm = TRUE, prob = 0.25),
            median = median(x = Weight.change, na.rm = TRUE),
            q3 = quantile(x = Weight.change, na.rm = TRUE, prob = 0.75),
            iqr = IQR(x = Weight.change, na.rm = TRUE),
            std = sd(x = Weight.change, na.rm = TRUE))

# =============================================================================
# Return individual summary measures.
# =============================================================================

# Assign the field as a local var
w <- x$Weight.change

# sample size
sum(complete.cases(w))

# sample mean
mean(x = w, na.rm = TRUE)

# sample median
median(x = w, na.rm = TRUE)

# lower sample quartile
quantile(x = w, na.rm = TRUE, prob = 0.25)

# upper sample quartile
quantile(x = w, na.rm = TRUE, prob = 0.75)

# sample IQR
IQR(x = w, na.rm = TRUE)

# sample standard deviation
sd(x = w, na.rm = TRUE)
