
# README

This project includes a series of visualisations and data explorations involving the Washington DC Bike Share data.

This is a test with the main focus being on the **separation of concerns**.

## TO-DO

- [ ] Add doc explaining source data

## QUESTIONS

- [X] **z-test** Comparing average casual users 2011 v 2012
  - fields: `casual`
- [ ] **Mann-whitney** median casual 2011 v median casual 2012?
  - fields: `casual`
- [ ] **SLR** temperature and casual user count
  - fields: `atemp` `casual`
- [ ] **SLR** temperature and registered user count
  - fields: `atemp` `registered`
- [ ] **MLR** temp AND humidity and casual user count
  - fields: `atemp` `hum` `registered`

## DATA

fields
: `dteday` `yr` `season` `workingday` `atemp` `hum` `casual` `registered` `dailycount`

filters
: `season=[2,3]` `workingday=[0]`

additional filter
: **2011** `yr=[0]` // **2012** `yr=[1]`

- [X] SPRING-SUMMER 2011
- [X] SPRING-SUMMER 2012

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
