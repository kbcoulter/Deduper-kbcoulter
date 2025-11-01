#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=1
#SBATCH --nodes=1
#SBATCH --job-name=test_dedup.sh

mamba activate dedup

./coulter_deduper.py -f unittest/test.sam -o /projects/bgmp/kcoulter/bioinfo/Bi624/Deduper-kbcoulter/test.out.sam.tmp -u /projects/bgmp/kcoulter/bioinfo/Bi624/Deduper-kbcoulter/STL96.txt

./coulter_deduper.py -f unittest/test_two.sam -o /projects/bgmp/kcoulter/bioinfo/Bi624/Deduper-kbcoulter/test_two.out.sam.tmp -u /projects/bgmp/kcoulter/bioinfo/Bi624/Deduper-kbcoulter/STL96.txt

if cmp -s test.out.sam.tmp unittest/test.out.sam && cmp -s test_two.out.sam.tmp unittest/test_two.out.sam; then
    echo -e "\nDeduplication Test Passed! File Deduplicated as Expected!"
else
    echo -e "\nDeduplication Test Failed... Expected output not achieved."
fi

echo -e "\nCleaning Up...\n"

rm test_two.out.sam.tmp
rm test.out.sam.tmp