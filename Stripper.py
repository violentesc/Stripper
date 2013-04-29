#! /usr/bin/env python
##Stripper.py v0.2##
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse, sys
#create the parse function:
def fileparse(delimiter, infile, outfile, append, verbose, replace):
        try:
		infile = open(infile, 'r')
	except:
		print("Input File not found!")
		exit(1)
	if append: 
		try:
			outfiles = [open(outfile[0], 'a'), open(outfile[1], 'a')]
		except:
			print("Cant open output file(s)!")
			exit(1)
	else:
		try:
			outfiles = [open(outfile[0], 'w'), open(outfile[1], 'w')]
		except:
			print("Cant open output file(s)!")
			exit(1)
        for line in infile:
		if line:
            		line = line.strip()
            		line = line.split(delimiter)
			#test the index
			if len(line) >= 2:
				if verbose:
            				print(line[0]+line[1])
				outfiles[0].write(line[0].strip()+"\n")
				outfiles[1].write(line[1].strip()+"\n")
	infile.close()
	outfiles[0].close()
	outfiles[1].close()		
##strip the user name from a file and place it into a new file:
#def userstrip(infile, outfile, append, verbose):
##Strip the end of an email url from the user name:
def emailstrip(infile, outfile, append, verbose):
	try:
		infile = open(infile, 'r')
	except:
		print("Input File not found!")
		exit(1)
	if append: 
		try:
			outfiles = open(outfile[0], 'a')
		except:
			print("Cant open output file(s)!")
			exit(1)
	else:
		try:
			outfiles = open(outfile[0], 'w')
		except:
			print("Cant open output file(s)!")
			exit(1)
	for line in infile:
		try:
			i = line.index('@')
			if verbose:
				print(line+'-> '+line[:i])
			outfiles.write(line[:i]+'\n')
		except:
			print(line+"-> not an Email")

if __name__ == "__main__":
        #Set all args:
        #Username and Pass Parser:
        parser = argparse.ArgumentParser(description='Stripper v0.2')
        #Delimiter Parser:
        parser.add_argument('-d', dest='delimiter', action='store', help='The char you would like to split the string by.')
        #Input File:
        parser.add_argument('-i', dest='input', action='store', help='Input file to be parsed')
        #Output File(s):
        parser.add_argument('-o', dest='output', action='store', nargs='+', help='Output file(s)')
        #Append Argument to append the output to exsiting files:
        parser.add_argument('-a', dest='append', action='store_true', help='Append to output file(s). If you do not add this argument files will be over written.')
        #Verbose
        parser.add_argument('-v', dest='verbose', action='store_true', help='Verbose')
        #E-Mail Parser:
        parser.add_argument('-e', dest='email', action='store_true', help='parse username from a E-Mail address.')
        #Replace Argument to replace chars or strings in a file:
        parser.add_argument('-r', dest='replace', action='store', help='replace a char or string in the file. **Not yet active')
        args = parser.parse_args()
        #Handle all the args
        #If the -e is not passed it will do a file parse:
        if args.email == 1:
           	emailstrip(args.input, args.output, args.append, args.verbose)
	elif args.delimiter and args.input and args.output:
		fileparse(args.delimiter, args.input, args.output, args.append, args.verbose, args.replace)
        else:
		parser.print_help(None)
