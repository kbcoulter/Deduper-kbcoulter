#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=1
#SBATCH --nodes=1
#SBATCH --job-name=dedup.sh
#SBATCH --error=dedup%j_err.log
#SBATCH --output=dedup%j_out.log

mamba activate dedup

/usr/bin/time -v ./deduper.py -f C1_SE_uniqAlign.sorted.sam -o /projects/bgmp/kcoulter/bioinfo/Bi624/Deduper-kbcoulter/C1_SE.out.sam -u STL96.txt