#!/usr/bin/env python

############################################################
### DEDUPER: Removes PCR Duplicates From Sorted SAM File ###
############################################################

import re

#################
### FUNCTIONS ###
#################

def fivepstart(POS:int, CIGAR:str, FLAG:int) -> int:


    pattern = r'\d+[A-Z]'
    re.findall(pattern, CIGAR)


    # MINUS STRAND GOING 3 -> 5
    M = # MATCH
    D = - # DELETION
    S = + # SOFTCLIPPING
    N = + # SKIPPING


    leading = True # is the leading letter

    if FLAG & ( 1 << 16): # MINUS STRAND
        read_len = 0
        val = "0"
        for char in CIGAR:
            if char.isnumeric:
                val.join(str(char))
            else:
                if char == "S":
                    if not leading:
                        #SUBTRACT NUM FROM REFERENCE
                        leading = False # SET TO FALSE
                    else:
                        # DO NOTHING
                elif char == "M":
                    leading = False

                else: # if character = D, N
                    read_len += int(val)

    else: # PLUS STRAND DONE 
        val = "0"
        for char in CIGAR:
            if char.isnumeric:
                val = val.join(str(char))
            else:
                if char == "S" and leading:
                    POS = POS - int(val) #SUBTRACT NUM FROM REFERENCE
                    continue

        return POS


def umigrabber(QNAME:str) -> str:
    if len(QNAME) < 8:
        return(f"ERROR w UMI: {QNAME}")
    else:
        return QNAME[-8:]

def main():
    # print(umigrabber("NS500451:154:HWKTMBGXX:1:11101:6251:1098:GTTACGTA")) # TESTING

if __name__ == "__main__":
    main()