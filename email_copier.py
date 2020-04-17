import pandas as pd
import clipboard
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("csv", help="Name of the CSV file")
parser.add_argument("column", help="Name of the column you want to copy")
parser.add_argument("copy_count", help="Number of entries to copy in one batch")
parser.add_argument("delimiter", help="Delimiter to concatenate the data")

args = parser.parse_args()

file_name = args.csv 
column_name = args.column 
copy_count = int(args.copy_count)
sheet = pd.read_csv(file_name)
df = sheet[column_name]
iter_count = math.ceil(df.shape[0]/copy_count)
delimiter = args.delimiter


def copy_emails(df, iter_count, copy_count, delimiter):
    for i in range(iter_count):
        idx = (i*100)
        emails = [x[0] for x in df.iloc[idx:idx+100].values]
        clipboard.copy(",".join(emails))
        print("Copied {}th {} entires".format(i+1, len(emails)))
        input("Press Enter to copy the next batch")
    print("No more entries to copy")


copy_emails(df, iter_count, copy_count, delimiter)
