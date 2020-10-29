import sys
import os
import json

sys.path.insert(0, 'src')

def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data'. 
    
    '''

    if 'data' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)

        # print the name of all the file in dataset into output.txt
        print(os.listdir(data_cfg['path']), file=open("output.txt", "a"))
    return 

if __name__ == '__main__':
    # run via:
    targets = sys.argv[1:]
    main(targets)