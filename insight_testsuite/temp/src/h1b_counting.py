#!/usr/bin/python 
import h1b
import os
import sys

# inputfilepath = sys.argv[1]
# outputfilepathforocc = sys.argv[2]
# outputfilepathforst = sys.argv[3]

inputfile = sys.argv[1]
outputfile_occ = sys.argv[2]
outputfile_state = sys.argv[3]


#check the columns
status, soc, state = h1b.checkcolumns(inputfile)


#Get sorted dictionaries for occupations and state
d_occ, d_state, total_certified =  h1b.makedicts(inputfile, status, state, soc)

#Write those dictionaries in file
h1b.writefiles(d_occ, total_certified, outputfile_occ, "TOP_OCCUPATIONS")
h1b.writefiles(d_state, total_certified, outputfile_state, "TOP_STATES")

