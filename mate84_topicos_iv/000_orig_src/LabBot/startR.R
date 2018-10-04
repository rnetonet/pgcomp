library(plumber)
r = plumb("LabBot.R")
r$run(port=8080)