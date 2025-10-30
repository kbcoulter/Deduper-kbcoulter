#!/usr/bin/env python

############################################################
### DEDUPER: Removes PCR Duplicates From Sorted SAM File ###
############################################################

###########################
### IMPORT AND ARGPARSE ###
###########################

import argparse
import re

def get_args():
     parser = argparse.ArgumentParser(description="Script to remove PCR duplicates, accepting a sorted paired end SAM file and UMI file")
     parser.add_argument("-f", "--file", help="Absolute file path for sorted input SAM file", required=True, type=str)
     parser.add_argument("-o", "--outfile", help="Absolute file path for deduplicated SAM file", required=True, type=str)
     parser.add_argument("-u", "--umi", help="File containing list of UMIs", required = True, type=str)
     parser.add_argument("-h", "--help", help="HELP ME", required = False, type=str)
     return parser.parse_args()

#################
### FUNCTIONS ###
#################

def fivepstart(POS:int, CIGAR:str, FLAG:int) -> int:

    def stripchar (chunk:str) -> int:
        return(int(re.sub('[A-Z]', '', chunk)))

    pattern = r'\d+[A-Z]'
    chunks = re.findall(pattern, CIGAR)

    if FLAG & ( 1 << 16): # MINUS STRAND
        for chunk in chunks:
            if "D" or "M" or "S" in chunk:
                POS += stripchar(chunk)

        first = chunk[-1]
        if "S" in first:
            POS += stripchar(first)

    else: # PLUS STRAND 
        first = chunks[0]
        if "S" in chunk:
            POS -= stripchar(first) #SUBTRACT NUM FROM REFERENCE

    return POS

def umigrabber(QNAME:str) -> str:
    if len(QNAME) < 8:
        return(f"ERROR: UMI TOO SHORT")
    else:
        return QNAME[-8:]
    
###################
### SCRIPT BODY ###
###################

def main():
    args = get_args()
    with open(outfile, 'x') as outfile:
        with open(file, 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                if "@" in line[0]:
                    outfile.write(line)
                else:
                    linecols = line.split('\t')
                    UMI = linecols[UH]
                    if UMI not in UMISET:
                        continue
                    else:

        


















if __name__ == "__main__":
    main()