
# =============================================================================
# References
# ==========
#
# - Computer activity 8 and Computer activity 9
# - Frequency histograms (HB.p5. U1.3.2. CA2.1.)
# - Plot a frequency histogram.
# =============================================================================

library(tidyverse)

# import the data
x <- read.csv("./data/membership.csv")

# preview the data.frame
head(x)

# plot a frequency histogram, default bins
g <- ggplot(x, aes(Percentage))
g <- g + geom_histogram()
g <- g + labs(y = "Frequency")

g

# plot a frequency histogram, change binwidth to 1
g <- ggplot(x, aes(Percentage))
g <- g + geom_histogram(binwidth = 1)
g <- g + labs(y = "Frequency")

g
