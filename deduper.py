#!/usr/bin/env python

############################################################
### DEDUPER: Removes PCR Duplicates From Sorted SAM File ###
############################################################

#################
### FUNCTIONS ###
#################

def fivepstart(POS:int, CIGAR:str, FLAG:int) -> int:

    one = FALSE # is the letter the first one 

    # MINUS STRAND
    M = # MATCH
    D = - # DELETION
    S = + if one - if not one  # SOFTCLIPPING
    N = + # SKIPPING

    # PLUS STRAND
    M = 
    D = +
    S = -
    N = -

    if FLAG: # MINUS STRAND
        val = ""
        for char in CIGAR:
            if char.isnumeric:
                append char
            else:
                POS MINUSOPERATIONMAP val
    


                
    else: # PLUS STRAND
        

def umigrabber(QNAME:str) -> str:
    if len(QNAME) < 8:
        return(f"ERROR w UMI: {QNAME}")
    else:
        return QNAME[-8:]

def main():
    print(umigrabber("RAINBOWRAINBOW"))

if __name__ == "__main__":
    main()