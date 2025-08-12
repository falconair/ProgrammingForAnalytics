import gzip
import argparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("infile")
args = parser.parse_args()

infile = args.infile

jon = 0 #variable containing Jon's score
arya = 0 #variable containing Arya's score

#Open file
file = open(infile, encoding='utf8')

#Go through each line in file
for line in file:
  tokens = line.split(',') #separate line into columns
  if tokens[4]=="Arya Stark": arya = arya + 1
  if tokens[4]=="Jon Snow": 
    jon = jon + 1

file.close()
print("Arya killed", arya, "people")
print("Jon killed", jon, "people")
