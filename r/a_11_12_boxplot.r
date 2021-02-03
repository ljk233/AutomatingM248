
# =============================================================================
# References
# ==========
#
# - Computer activity 11 and Computer activity 12
# - Boxplots (HB.p5. U1.3.3. CA2.2.)
# - Plot a boxplot.
# =============================================================================

library(tidyverse)

# import the data
x <- read.csv("./data/membership.csv")

# preview the data.frame
head(x)

# plot a horizontal boxplot
g <- ggplot(data = x, aes(x = Percentage))
g <- g + geom_boxplot()

# add the visual
g

# plot a vertical boxplot, swap the x for y
# plot a horizontal boxplot
g <- ggplot(data = x, aes(y = Percentage))
g <- g + geom_boxplot()

# add the visual
g
