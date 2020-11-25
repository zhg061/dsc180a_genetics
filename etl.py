import sys
import os
import json

with open('config/data-params.json') as fh:
    data_cfg = json.load(fh)
raw_data_path = data_cfg['raw_data_path']
reference_path = data_cfg['reference_path']
test_data_path = data_cfg['test_data_path']
fastqc_tool = data_cfg['fastqc_tool']
kallisto_tool = data_cfg['kallisto_tool']
kallisto_path = data_cfg['kallisto_path']

def get_subset(input_file, output_file, size):      
    #generate test_1 & test_2
    os.system('zcat ' + raw_data_path + input_file[0] + ' | head -' + str(size) + ' > ' + test_data_path + output_file[0])
    os.system('zcat ' + raw_data_path + input_file[1] + ' | head -' + str(size) + ' > ' + test_data_path + output_file[1])
    return
def get_fastqc(output_file):    
    #FastQC report for test1 & test2
    os.system('gzip ' + test_data_path + output_file[0] + ' ' +  test_data_path + output_file[1])
    os.system(fastqc_tool + ' ' + test_data_path + output_file[0] + '.gz')
    os.system(fastqc_tool + ' ' + test_data_path + output_file[1] + '.gz')
    return
def get_kallisto(output_file):    
    ## Kallisto        
    # Quantification for test1 & test2
    os.system('cd ' + kallisto_tool + '/test')
    os.system(kallisto_tool + '/kallisto' + ' quant -i ' + reference_path + '/kallisto_transcripts.idx -o ' + kallisto_path + ' -b 100 ' + test_data_path + output_file[0] + '.gz ' + test_data_path + output_file[1] + '.gz')
    return
