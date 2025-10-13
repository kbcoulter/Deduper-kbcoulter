# Deduper unittest

## test.sam:
#### Test file covering all test cases in DeDup in the order:

- Line 11: Same Adjusted Position (From Cigar String)
- Line 13: Different Chromomsome Number
- Line 15: Different Strand
- Line 17: Different Position (With Cigar String)
- Line 19: Different UMI 
- Line 21: Same Everything (Without Cigar String Adjustment)
- Line 23: UMI Not in Bank

## out_test.sam:
#### Contains the expected output from test.sam after DeDup

Lines 11, 21, and 23 should be missing from final output, as they are Duplicates with lines appearing before them, or the UMI does not exist.
Because we are opting to keep the 1st appearing record, these will not appear in our output. 

