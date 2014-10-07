#!/usr/bin/env python



import argparse, os, sys, csv, IPython
import pandas
import pdb
import glob
from pandas import *
from IPython import get_ipython
from glob import glob

#output and input file name to give with the script
parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output', help="sort snp table to remove identical and no hit")
parser.add_argument('-s', '--snp_table', help="snp table to sort")

args = parser.parse_args()
output_file = args.output
input_file = args.snp_table

#read in file as dataframe
df = read_csv(input_file, index_col=[0,1], header=[0,1], dtype=unicode)
pdb.set_trace()
#replaces lines with "No Hits" with NaN and removes lines with NaN in qbase columns
no_hit= df.mask(df=='No Hit')
header_list =no_hit.columns.values

removed=no_hit.dropna()
#level=[qb[1] for qb in header_list if "qbase:" in qb[1]]
qindexes= []
for i, v in enumerate(header_list):
    if 'qbase:' in v[1]:
        qindexes.append(i)

#identical_a=removed.mask(df[3:qindexes[-1]], 'A')
# remove identical lines
pdb.set_trace()

#save file with output name
with open(output_file,'w') as output:
    XXX.to_csv(output)
