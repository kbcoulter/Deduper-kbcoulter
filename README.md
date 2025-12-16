# Deduper 
## Reference Based PCR Duplicate Removal Tool

Deduper is a Python-based tool designed to remove PCR duplicates from a sorted SAM file of uniquely mapped reads. It retains only a single copy of each read, enabling accurate and efficient downstream analysis.

    
### Assumptions
- Single-end sequencing data
- Unique Molecular Identifiers (UMIs) embedded in the QNAME field
        Example:```NS500451:154:HWKTMBGXX:1:11101:15364:1139:GAACAGGT```. 
- Unique UMIS are newline separated in UMI.txt file
- UMI length is 8 bases. 
- Input SAM file is uncompressed and sorted (e.g., using samtools sort)

### Features
- Efficient PCR duplicate removal
- Handles UMIs and discards erroneous ones
- Retains the first read encountered when duplicates are found
- Accounts for all possible CIGAR strings, including soft clipping adjustments
- Outputs a properly formatted SAM file
- Does **NOT** modify the input file
    
### Usage

To Test Individual Functions or entire pipeline, see: ```unittest/README.md```

To Run Deduplication Pipeline:
    ```
    $ ./deduper.py -u <UMI.txt> -f <input.sam> -o <output.sam>
    ```

To Get Help:
    ```
    $ ./deduper.py -h
    ```

### Additions

Future updates will include support for paired-end reads, handling randomers instead of UMIs, error correction for known UMIs rather than discarding errors, compatibility with longer UMIs (>8 bases), and an option to choose which duplicate is retained in the output file.