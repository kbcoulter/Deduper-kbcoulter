# Deduper unittest

## Deduper Function Testing
To Ensure that All Functions Necessary to Deduplicate are functioning properly, from Deduper-kbcoulter/ please run the script test_func_deduper.py with:

```{bash}
$ ./test_func_deduper.py 
```

## Deduper Deduplication Testing
To ensure that the Deduplication pipeline is functioning properly, from Deduper-kbcoulter/ please run the script test_deduper.py with:

```{bash}
$ sbatch ./test_deduper.sh
```

This will run Deduper on test files in unittest dir:

``` 
test.sam 
test_two.sam
```

And compare them to:
```
test.out.sam
test_two.out.sam
```
**In test.sam:** Specific cases covered are detailed in the test.sam file beyond the columns necessary for deduplication. 

**In test_two.sam** Specific cases covered are not detailed, as this file is designed to more closely (but not perfectly) resemble a SAM file. 

### Note: Please allow script to run **completely** to clean up .tmp files. 
