#!/usr/bin/env python

from deduper import *

def test_fivepstart():
    '''Tests fivepstart from deduper.py'''
    assert fivepstart(100, "3S97M", 0) == "+97", "Five Prime Start Failed: + Strand, Basic Pos Adjustment"
    assert fivepstart(97, "50M50D", 0) == "+97", "Five Prime Start Failed: + Strand, No Pos Adjustment"
    assert fivepstart(91, "7M", 147) == "-97", "Five Prime Start Failed: - Strand, No Pos Adjustment"
    assert fivepstart(1, "10S97M", 147) == "-97", "Five Prime Start Failed: - Strand, Basic Pos Adjustment"
    assert fivepstart(1, "45M45D7S", 147) == "-97", "Five Prime Start Failed: - Strand, Complex Pos Adjustment"

def test_stripchar():
    '''Tests stripchar from deduper.py'''
    assert stripchar("30S") == 30, "Strip Character Failed."
    assert stripchar("8G") == 8, "Strip Character Failed."
    assert stripchar("8MARIOTA") == 8, "Strip Character Failed."
    assert stripchar("10NIX") == 10, "Strip Character Failed."
    assert stripchar("HERBERT10") == 10, "Strip Character Failed."
    assert stripchar("MOOR5E") == 5, "Strip Character Failed."
    assert stripchar("00003HARRINGTON") == 3, "Strip Character Failed."

def test_strandedness():
    '''Tests strandedness from deduper.py'''
    assert strandedness(0) == False, "Get Strandedness Failed. + Strand Misclassified"
    assert strandedness(99) == False, "Get Strandedness Failed. + Strand Misclassified"
    assert strandedness(147) == True, "Get Strandedness Failed. - Strand Misclassified"

def test_umigrabber():
    '''Tests strandedness from deduper.py'''
    assert umigrabber("") == "ERROR:UMI", "UMI grabbing failed. Bad UMI not flagged."
    assert umigrabber("CATCATCATCA") == "CATCATCA", "UMI grabbing failed. Incorrect UMI returned"
    assert umigrabber("COOLRAINBOWS") == "RAINBOWS", "UMI grabbing failed. Incorrect UMI returned"

if __name__ == "__main__":
    test_fivepstart()
    test_stripchar()
    test_strandedness()
    test_umigrabber()
    print("All Functions Necessary to Deduplicate Work as Expected.")