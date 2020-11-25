import sys
import os
import json
sys.path.insert(0, 'src')
from etl import *

def main(targets):  
    input_file = ['SRR3438851_1.fastq.gz','SRR3438851_2.fastq.gz']
    output_file = ['SRR3438851_1.fastq','SRR3438851_2.fastq']
    if 'subset' in targets:
        get_subset(input_file, output_file, 100)
    if 'fastqc' in targets:
        get_fastqc(output_file)
    if 'kallisto' in targets:
        get_kallisto(output_file)        
    if 'test' in targets: 
        get_subset(input_file, output_file, 100)
        get_fastqc(output_file)
        get_kallisto(output_file)
    return 

if __name__ == '__main__':
    # run via:
    targets = sys.argv[1:]
    main(targets)