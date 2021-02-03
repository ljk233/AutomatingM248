
# =============================================================================
# References
# ==========
#
# - Computer actitity 6
# - Bar charts (HB.p5. U1.3.1. CA1.2.)
# - Plot a bar chart of aggregated data.
#
# =============================================================================

library(tidyverse)

# import the data
x <- read.csv("./data/workforce.csv")

# preview the data.frame
head(x)

# build the bar chart of Total employment by Occupation.type
g <- ggplot(data = x, aes(x = Occupation.type, y = Total))
g <- g + geom_bar(stat = "identity")
g <- g + labs(x = "", y = "Total employement")

# visualise the plot
g

# reorder the bar chart in descending order (indicated by the -)
g <- ggplot(data = x, aes(x = reorder(Occupation.type, -Total), y = Total))
g <- g + geom_bar(stat = "identity")  # plot the actual value in the data
g <- g + labs(x = "", y = "Total employement")

# visualise the plot
g
