import argparse
import pandas as pd

# create arguments
parser = argparse.ArgumentParser(description='get size of file')
parser.add_argument('input_filename', metavar='input_filename', type=str)
parser.add_argument('-out', metavar='output_filename', type=str)
parser.add_argument('-cs', metavar='chunk_size', type=int)
args = parser.parse_args()

# pass in arguments
input_filename = args.input_filename
output_filename = args.out
chunk_size = args.cs

if not output_filename:
	output_filename = 'chunk-' + input_filename
if not chunk_size:
	chunk_size = 100

df = pd.read_csv(input_filename)
row_count = len(df.index)

i = 0
while i < row_count:
    # print df[i:i+chunk_size]
    temp_df = df[i:i+chunk_size]
    filename = str(i) + '-' + output_filename
    temp_df.to_csv(filename, index=0)
    print 'wrote:' + filename
    i += chunk_size
