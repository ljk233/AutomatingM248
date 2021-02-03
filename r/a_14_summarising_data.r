
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
# - Boxplots (HB.p5. U1.3.3. CA2.2).
#
# Use Pandas to calculate numerical summaries of some data.
# Output comparative boxplots of the data.
#
# =============================================================================

library(tidyverse)

# import the data
x <- read.csv("./data/response-inhibition.csv")

# preview the data.frame
head(x)

# =============================================================================
# output a simple table of summary measures
# =============================================================================

# output a simple table of summary measures
data <- as_tibble(x)

q1 <- quantile(x = x$Weight.change, na.rm = TRUE, prob = 0.25, type = 1)
q3 <- quantile(x = x$Weight.change, na.rm = TRUE, prob = 0.75, type = 1)
i.q.r <- quantile(x = x$Weight.change, na.rm = TRUE, prob = 0.75, type = 1) -
  quantile(x = x$Weight.change, na.rm = TRUE, prob = 0.25, type = 1)
i.q.r

x %>%
  summarise(
          count = n() - sum(is.na(Weight.change)),
          count.na = sum(is.na(Weight.change)),
          mean = mean(x = Weight.change, na.rm = TRUE),
          q1 = quantile(x = Weight.change, na.rm = TRUE, prob = 0.25),
          median = median(x = Weight.change, na.rm = TRUE),
          q3 = quantile(x = Weight.change, na.rm = TRUE, prob = 0.75),
          iqr = IQR(x = Weight.change, na.rm = TRUE),
          std = stats::sd(x = Weight.change, na.rm = TRUE),
          )

# =============================================================================
# Return individual summary measures.
# =============================================================================

# sample mean

# sample median

# lower sample quartile

# upper sample quartile

# Sample IQR

# sample standard deviation
