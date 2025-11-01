#!/usr/bin/env python

from coulter_deduper import *

def test_fivepstart():
    assert fivepstart(100, "3S97M", 0) == "+97", "Five Prime Start Failed: + Strand, Basic Pos Adjustment"
    assert fivepstart(97, "50M50D", 0) == "+97", "Five Prime Start Failed: + Strand, No Pos Adjustment"
    assert fivepstart(91, "7M", 147) == "-97", "Five Prime Start Failed: - Strand, No Pos Adjustment"
    assert fivepstart(1, "10S97M", 147) == "-97", "Five Prime Start Failed: - Strand, Basic Pos Adjustment"
    assert fivepstart(1, "45M45D7S", 147) == "-97", "Five Prime Start Failed: - Strand, Complex Pos Adjustment"

def test_stripchar():
    assert stripchar("30S") == 30, "Strip Character Failed."
    assert stripchar("8G") == 8, "Strip Character Failed."
    assert stripchar("8MARIOTA") == 8, "Strip Character Failed."
    assert stripchar("10NIX") == 10, "Strip Character Failed."
    assert stripchar("HERBERT10") == 10, "Strip Character Failed."
    assert stripchar("MOOR5E") == 5, "Strip Character Failed."
    assert stripchar("00003HARRINGTON") == 3, "Strip Character Failed."

def test_strandedness():
    assert strandedness(0) == False, "Get Strandedness Failed. + Strand Misclassified"
    assert strandedness(99) == False, "Get Strandedness Failed. + Strand Misclassified"
    assert strandedness(147) == True, "Get Strandedness Failed. - Strand Misclassified"

if __name__ == "__main__":
    test_fivepstart()
    test_stripchar()
    test_strandedness()
    print("All Functions Necessary to Demultiplex Work as Expected. HOORAY!")