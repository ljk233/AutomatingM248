
PATH <- "../data/"

conc <- function(f) {
  return(paste(PATH, f, ".csv", sep=""))
}

load <- function(f) {
  return(read.csv(conc(f)))
}

load_glass_fibres <- function() {
  return(load("glass-fibres"))
}

load_plasma <- function() {
  return(load("plasma"))
}

load_accidents <- function() {
  return(load("accidents"))
}

load_skulls <- function() {
  return(load("skulls"))
}

load_sewer <- function() {
  return(load("sewer"))
}

load_schoolgirls <- function() {
  return(load("schoolgirls"))
}

load_practical_test <- function() {
  return(load("practical-test"))
}

load_darwin <- function() {
  return(load("darwin"))
}

load_movements <- function() {
  return(load("movements"))
}

load_lesions <- function() {
  return(load("lesions"))
}

load_dopamine <- function() {
  return(load("dopamine"))
}

load_osa <- function() {
  return(load("osa"))
}

load_uniform_goals <- function() {
  return(load("uniform_goals"))
}
