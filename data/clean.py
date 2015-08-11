#!/usr/bin/python
#
import sys
import argparse
import re

parser = argparse.ArgumentParser(description='Used to clean files of bad chars.',
    prog='cleaner')
parser.add_argument('--version', action='version',
    version='%(prog)s 0.1')
parser.add_argument('infile', nargs='?',
    help='the name of the text file to parse.',
    default=sys.stdin)
parser.add_argument('outfile', nargs='?',
    help='the name of the text file to output.',
    default=sys.stdout)
args = vars(parser.parse_args())

fileout = open(args['outfile'],'wb')
filein = open(args['infile'],'r')

goodchars = re.compile("[^ABCDEFGHIJKLMNOPQURSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,;.!?:'\\\"|_@#$%^&*~`+/-=() \r\n]")

for line in filein.readlines():
    fixedline = goodchars.sub("", line)
    fileout.write(fixedline)
