#http://stackoverflow.com/questions/18172851/deleting-dataframe-row-in-pandas-based-on-column-value
#for replacement of a given value with NaN

#!/usr/bin/env python


import argparse, os, sys, csv, IPython
import pandas
import pdb
from pandas import *
from IPython import get_ipython


#output and input file name to give with the script
parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output', help="sort snp table to remove identical and no hit")
parser.add_argument('-s', '--snp_table', help="snp table to sort")

args = parser.parse_args()
output_file = args.output
input_file = args.snp_table

#read in file as dataframe
df = read_csv(input_file, index_col=[0,1], header=[0,1], dtype=unicode)
df=df.drop('syn/nsyn/intergenic', axis=1, level=1)


#replaces lines with "No Hits" with NaN and removes lines with NaN in qbase columns
no_hit= df.mask(df=='No Hit')
removed=no_hit.dropna()


#replaces lines with indel

indel=removed.mask(removed=='indel')
indel2=indel.dropna()



# remove identical lines
bases=['A','C','G','T']


for i in bases:

    indel2=indel2[indel2 !=i]  #!=i
    indel2=indel2.dropna(how='all')
    indel2=indel2.fillna(i)


#creates dataframe with rows that have '/' in it
count_qbase=indel2.columns.values
qindexes=[]
for i, v in enumerate(count_qbase):
    if 'qbase:' in v[1]:
        qindexes.append(i)

empty=DataFrame()


for x in qindexes:
    empty=empty.append((indel2[(indel2.iloc[:,x]).str.contains('/')]))

pdb.set_trace()



#save file with output name
with open(output_file,'w') as output:
    indel2.to_csv(output)
