#!/usr/bin/env python

############################################################
### DEDUPER: Removes PCR Duplicates From Sorted SAM File ###
############################################################

##########################
### IMPORTS & ARGPARSE ###
##########################

import argparse
import re

def get_args():
     parser = argparse.ArgumentParser(
     description=(
            "BLAH\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
     parser.add_argument("-f", "--file", help="Absolute file path for sorted input SAM file", required=True, type=str)
     parser.add_argument("-o", "--outfile", help="Absolute file path for deduplicated SAM file", required=True, type=str)
     parser.add_argument("-u", "--umifile", help="File containing list of UMIs", required = True, type=str)
     return parser.parse_args()

#################
### FUNCTIONS ###
#################

def strandedness(FLAG:int) -> str:
    if FLAG & ( 1 << 16): # MINUS STRAND
        return "-"
    else:
        return "+"

def fivepstart(POS:int, CIGAR:str, STRAND:str) -> int:

    def stripchar (chunk:str) -> int:
        return(int(re.sub('[A-Z]', '', chunk)))

    pattern = r'\d+[A-Z]'
    chunks = re.findall(pattern, CIGAR)

    if STRAND == "-": # MINUS STRAND
        POS -= 1
        for chunk in chunks:
            if any(x in chunk for x in ("D", "M", "N")):
                POS += stripchar(chunk)

        last = chunks[-1]
        if "S" in last:
            POS += stripchar(last)
        return POS
    
    else: # PLUS STRAND 
        first = chunks[0]
        if "S" in first:
            POS -= stripchar(first) #SUBTRACT NUM FROM REFERENCE
        return POS

def umigrabber(QNAME:str) -> str:
    if len(QNAME) < 8:
        return(f"ERROR: UMI TOO SHORT")
    else:
        #return QNAME.split(":")[7]
        return QNAME[-8:]
    
###################
### SCRIPT BODY ###
###################

def main():
    args = get_args()
    file = args.file
    outfile = args.outfile
    umifile = args.umifile

    header_lines = 0
    bad_umi = 0 
    unique_reads = 0
    total_reads = 0
    duplicates_removed = 0

    chrom_counter:dict = {}
    UMISET = set()
    print("Gathering UMIs...")
    with open(umifile, 'r') as umifile: # MAKE UMISET
        for umi in umifile:
            UMISET.add(umi.strip())

    print("Opening SAM...")
    with open(outfile, 'x') as outfile:
        with open(file, 'r') as file:
            print("Deduplicating...")
            chrom_tracker = None
            read_set = set()

            for line in file:
                if "@" in line[0]: # WRITE HEADER AND COUNT
                    outfile.write(line.strip('\n'))
                    header_lines += 1
                    continue

                total_reads += 1
                cols = line.strip().split('\t')
                UMI = umigrabber(cols[0]) #QNAME

                if UMI not in UMISET: # IF UMI BAD, COUNT AND KEEP GOING
                    bad_umi += 1 
                    continue

                CHROM = (cols[2]) #RNAME
                STRAND = strandedness(int(cols[1])) #FLAG
                read = f"{UMI},{STRAND},{fivepstart(int(cols[3]), cols[5], STRAND)}" # TRUEPOS from POS, CIGAR, STRAND

                if CHROM != chrom_tracker: # IF NEW CHROM, UPDATE TRACKER, CLEAR SET
                    chrom_tracker = CHROM 
                    read_set = set()

                if read not in read_set: # IF THE READ IS UNIQUE, ADD IT TO SET, WRITE, COUNT, COUNT FOR CHROM, 
                    read_set.add(read) 
                    outfile.write(line)
                    unique_reads += 1 
                    if CHROM in chrom_counter:
                        chrom_counter[CHROM] += 1
                    else:
                        chrom_counter[CHROM] = 1 
                else: # IF READ NOT UNIQUE, COUNT DUPLICATE
                    duplicates_removed += 1 

    ####################
    ### PRINT OUTPUT ###
    ####################

    print(f"Deduplicated. File can be found at {outfile}\n")
    print("### DEDUPLICATION SUMMARY ###")
    print(f"Header Lines:   {header_lines}")
    print(f"Bad UMIs:   {bad_umi}")
    print(f"Total Reads:    {total_reads}")
    print(f"Duplicates Removed: {duplicates_removed}")
    print(f"Total Unique Reads: {unique_reads}")
    for k,v in chrom_counter.items():
        print(f"Chrom{k} Unique Reads:  {v}")

if __name__ == "__main__":
    main()