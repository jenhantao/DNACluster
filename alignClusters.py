#!/usr/bin/python

# First arguement is path to input .dnaclust file
# Second argument is the interval of the number of sequences in an accepted cluster
#      Format is [a,b] where the number of sequences in a cluster is a <= n <= b
#      If a is less than b, then the values will be switched
#      To specify an unbounded interval such as a<=n use [a,] likewise for n<=b use [,b]
# Third argument specifies whether files should be printed to standard output or 
# printed into one file per cluster. "p" for print "f" for file. Printing is default.
# Fourth argument argument is path to output directory. If one is needed and not given, 
# the directory containing the script will be used

import os
import sys

# verify the arguments and parse them
if len(sys.argv) < 3:
   print "A minimum of three arguments must be given. The format is as follows:\nFirst arguement is path to input .dnaclust file\nSecond argument is the interval of the number of sequences in an accepted cluster\n\tFormat is [a,b] where the number of sequences in a cluster is a<=n<=b\nThird argument specifies whether files should be printed to standard output or\n printed into one file per cluster. 'p' for print 'f' for file. Printing is default.\nFourth argument argument is path to output directory."

filePath = str(sys.argv[1])
tokens = sys.argv[2][1:len(sys.argv[2])-1].split(",")
if len(tokens[0]) > 0:
   lowerBound = float(tokens[0]) # lower bound of the interval for cluster size
else:
   lowerBound = 0;
if len(tokens[1]) > 0:
   upperBound = float(tokens[1]) # upper bound of the interval for cluster size
else:
   upperBound = 999999 # arbitrarily large value
outputFile = False # whether or not output files should be created
outputFileDirectory = "./"# directory where files will be created
if sys.argv[3] != "f" and sys.argv[3] != "p":
   outputFile = False
elif sys.argv[3] == "f":
   outputFile = True

if len(sys.argv) > 4:
   outputFileDirectory = str(sys.argv[4]);

# Create output directory if it doesn't exist
if not os.path.exists(outputFileDirectory) and outputFile:
    os.makedirs(outputFileDirectory)

print "input file: " + filePath
print "interval: " + str(lowerBound) + "<= n <= " + str(upperBound)
print "output file?: " + str(outputFile)+ " to: " + outputFileDirectory

with open(filePath) as f:
     inputFileLines = f.readlines()

clusterCount = 0
numFiles = 0;
for line in inputFileLines:
   line = line.rstrip("\n")
   if line.startswith("#"):
      numFiles = numFiles +1
      numberInCluster = float(line.rstrip("\n")[1:])
      if (numberInCluster >= lowerBound and numberInCluster <= upperBound) and outputFile:
         file = open(outputFileDirectory+"/cluster_"+str(clusterCount)+".fasta", 'w+')
         clusterCount = clusterCount +1
   elif numberInCluster >= lowerBound and numberInCluster <= upperBound:
      if len(line)>0:
          if outputFile:
             file.write(line+"\n")
          else:
             print(line)
