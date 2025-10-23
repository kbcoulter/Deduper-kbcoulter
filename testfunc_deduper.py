if __name__ == "__main__":
    assert umigrabber("NS500451:154:HWKTMBGXX:1:11101:6251:1098:GTTACGTA") == "GTTACGTA"
    assert umigrabber("XYLOPHONEGTAGTAGT")

    assert fivepstart(130171693, "71M*", 0) == 130171693
    assert fivepstart(1, 