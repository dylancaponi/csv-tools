import argparse
import csv
# import pandas

parser = argparse.ArgumentParser(description='get size of file')
parser.add_argument('filename', metavar='filename', type=str)
args = parser.parse_args()
filename = args.filename

# df = pandas.read_csv(filename)
# print df.shape

with open(filename,"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)

print row_count