
# =============================================================================
# References
# ==========
#
# - Computer activity 4
# - Bar chart (HB.pp5; U1.3.1; CA1.2).
# - Plot a bar chart of raw data.
# =============================================================================

library(tidyverse)

# import the data
x <- read.csv("./data/tattoos.csv")

# preview the data.frame
head(x)

# build the bar chart of score
g <- ggplot(data = x, aes(Score))
g <- g + geom_bar()
g <- g + labs(y = "Frequency")

# visualise the plot
g
