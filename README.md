# Deduper 
### Reference Based PCR Duplicate Removal Tool

Deduper is a Python-based tool designed to remove [PCR](https://en.wikipedia.org/wiki/Polymerase_chain_reaction) duplicates from a sorted SAM file of uniquely mapped reads. It retains only a single copy of each read, enabling accurate and efficient downstream analysis.

    
## Assumptions
- Single-end sequencing data
- Unique Molecular Identifiers (UMIs) embedded in the QNAME field: ```NS500451:154:HWKTMBGXX:1:11101:15364:1139:GAACAGGT```
- Unique UMIS are newline separated in an UMI.txt file
- Input SAM file is uncompressed and sorted (e.g., using [samtools](https://www.htslib.org/doc/#manual-pages) sort)
- Specified UMI length (defaults to 8). 

## Features
- Efficient PCR duplicate removal
- Handles UMIs and discards erroneous ones
- Retains the **first** read encountered when duplicates are found
- Accounts for all possible CIGAR strings, including soft clipping adjustments
- Outputs a properly formatted SAM file
- Does **NOT** modify the input file
    
## Usage

### 1. To test individual functions or entire pipeline, run one of the following scripts:
```bash
$ ./test_func_deduper.py #TO TEST FUNCTIONS
$ sbatch ./test_deduper.sh # TO TEST FULL PIPELINE
```

For more information, please refer to the **[unittest manual](unittest/README.md)**. 


### 2. To Run Deduplication Pipeline:
```bash
$ ./deduper.py \
    -u <UMI.txt> \
    -f <input.sam> \
    -o <output.sam>
    -l <UMI length if not 8> #OPTIONAL
```

### 3. To Get Help:
```
$ ./deduper.py -h
```

## Additions

Planned updates will include support for paired-end reads and an option to choose which duplicate is retained in the output file.