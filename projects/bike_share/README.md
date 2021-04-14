
# README

This project includes a series of visualisations and data explorations involving the Washington DC Bike Share data.

This is a test with the main focus being on the **separation of concerns**.

## TO-DO

- [ ] Add doc explaining source data

## NOTEBOOKS

The notebooks folder contains 3 sub-folders, each dealing with a different area of concern.

**1_setup**
: contains a series of notebooks that will recreate the  processed data sets in out, so long as the source file is saved in the **data/in** sub-folder.
They may not be independent, so the series of notebooks that eed to be run prior to the running of a particular notebook will be noted at the top.

**2_exploration**
: contains a series of notebooks that are concerned with exploring the data set.
These act as staging grounds for the building of the support classes in **src** which are used in the **3_final** notebooks.
*They should be considered to be unstable.*

**3_final**
: the finished products that use the static classes in **src** to display the desired visualisations.
