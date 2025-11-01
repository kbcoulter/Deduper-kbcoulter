#!/usr/bin/env python

############################################################
### DEDUPER: Removes PCR Duplicates From Sorted SAM File ###
############################################################

##########################
### IMPORTS & ARGPARSE ###
##########################

import argparse
import re

CIGAR_PATTERN = re.compile(r'\d+[A-Z]')
STRIP_PATTERN = re.compile(r'[A-Z]')

def get_args():
     parser = argparse.ArgumentParser(
     description=(
                  "################################\n"
                  "# Deduper | kcoulter | 10-2025 #\n"
                  "################################\n\n"
                  "PURPOSE: Given a SAM file of uniquely mapped reads, remove all PCR duplicates (retain only a single copy of each read):\n\n"
                  "Deduper script requires: (refer to options below):\n"
                  "\t Uncompressed, Absolute Sorted SAM File Path \n\t Absolute Outfile Path (Without New Dir) \n\t Line Separated UMI File \n\n"
                  "NOTE: This script assumes SAM file contains unique paired end reads, UMI length of 8, uncompressed file inputs.\n"
                  "First read of duplicates is saved.\n"
                  "No Summary file is created. Summary prints to stream (stdout).\n"),
                  formatter_class=argparse.RawTextHelpFormatter)
     parser.add_argument("-f", "--file", help="Absolute File Path for Sorted Input SAM File", required=True, type=str)
     parser.add_argument("-o", "--outfile", help="Absolute File Path for Deduplicated SAM File", required=True, type=str)
     parser.add_argument("-u", "--umifile", help="Line Separated File Containing List of UMIs", required = True, type=str)
     return parser.parse_args()

#################
### FUNCTIONS ###
#################

def strandedness(FLAG:int) -> bool:
    if (FLAG) & 16:
        return True
    else:
        return False

def stripchar(chunk:str) -> int:
    return(int(STRIP_PATTERN.sub('', chunk)))
    
def fivepstart(POS:int, CIGAR:str, FLAG:int) -> str:

    chunks = CIGAR_PATTERN.findall(CIGAR)
    if strandedness(FLAG): # MINUS STRAND
        POS -= 1
        for chunk in chunks:
            if chunk[-1] in ("D", "M", "N"):
                POS += stripchar(chunk)

        last = chunks[-1]
        if last[-1] == "S":
            POS += stripchar(last)
        return f"-{POS}"
    
    else: # PLUS STRAND 
        first = chunks[0]
        if first[-1] == "S":
            POS -= stripchar(first) #SUBTRACT NUM FROM REFERENCE
        return f"+{POS}"

def umigrabber(QNAME:str) -> str:
    if len(QNAME) < 8:
        return(f"ERROR:UMI")
    else:
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
    chrom_counter = {}
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
                    outfile.write(line)
                    header_lines += 1
                    continue

                total_reads += 1
                cols = line.strip().split('\t')
                UMI = umigrabber(cols[0]) #QNAME

                if UMI not in UMISET: # IF UMI BAD, COUNT AND KEEP GOING
                    bad_umi += 1 
                    continue

                CHROM = (cols[2]) #RNAME
                FLAG = int(cols[1]) #FLAG
                POS = int(cols[3])
                CIGAR = cols[5].strip()

                read = f"{UMI},{fivepstart(POS, CIGAR, FLAG)}" # TRUEPOS from POS, CIGAR, STRAND

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

    print(f"Deduplicated!\n")
    #print(f"File can be found at {str(outfile)}\n")
    print("#############################\n### DEDUPLICATION SUMMARY ###\n#############################")
    print(f"Header Lines:   {header_lines}")
    print(f"Bad UMIs:   {bad_umi}")
    print(f"Total Reads:    {total_reads}")
    print(f"Duplicates Removed: {duplicates_removed}")
    print(f"Total Unique Reads: {unique_reads}\n")
    print("### UNIQUE READS BY CHROM ###")
    for k,v in chrom_counter.items():
        print(f"{k}\t{v}")

if __name__ == "__main__":
    main()