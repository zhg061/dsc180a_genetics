import sys
import os
import json
sys.path.insert(0, 'src')

def main(targets):
    if 'test' in targets:        
        #generate test_1 & test_2
        os.system('zcat /datasets/srp073813/SRR3438851_1.fastq.gz | head -100 > ~/dsc180a_genetics/test/test_data/m7_1.fastq')
        os.system('zcat /datasets/srp073813/SRR3438851_2.fastq.gz | head -100 > ~/dsc180a_genetics/test/test_data/m7_2.fastq')

        #FastQC report for test1 & test2
        os.system('gzip ~/dsc180a_genetics/test/test_data/m7_1.fastq ~/dsc180a_genetics/test/test_data/m7_2.fastq')
        os.system('/opt/FastQC/fastqc ~/dsc180a_genetics/test/test_data/m7_1.fastq.gz')
        os.system('/opt/FastQC/fastqc ~/dsc180a_genetics/test/test_data/m7_2.fastq.gz')

        ## Kallisto        
        # Quantification for test1 & test2
        os.system('cd /opt/kallisto_linux-v0.42.4/test')
        os.system('/opt/kallisto_linux-v0.42.4/kallisto quant -i /datasets/srp073813/reference/kallisto_transcripts.idx -o ~/dsc180a_genetics/test/test_kallisto -b 100 ~/dsc180a_genetics/test/test_data/m7_1.fastq.gz ~/dsc180a_genetics/test/test_data/m7_2.fastq.gz')
    return 

if __name__ == '__main__':
    # run via:
    targets = sys.argv[1:]
    main(targets)