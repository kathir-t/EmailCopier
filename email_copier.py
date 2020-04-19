import pandas as pd
import clipboard
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("csv", help="Name of the CSV file", type=str)
parser.add_argument("column", help="Name of the column you want to copy", type=str)
parser.add_argument("copy_count", help="Number of entries to copy in one batch", type=int)

args = parser.parse_args()

file_name = args.csv
column_name = args.column 
copy_count = int(args.copy_count)
sheet = pd.read_csv(file_name)
email_column = sheet[column_name]
iter_count = math.ceil(email_column.shape[0]/copy_count)

# Function sourced from: https://codegolf.stackexchange.com/questions/4707/outputting-ordinal-numbers-1st-2nd-3rd#answer-4712
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])


def copy_emails(email_column, iter_count, copy_count):
    for i in range(iter_count):
        cursor = (i*copy_count)
        emails = [x for x in email_column.iloc[cursor:cursor+copy_count].values]
        clipboard.copy(",".join(emails))
        print("Batch {}/{}  - Copied {} set of {} out of {} entires".format(i+1, iter_count, ordinal(i+1), copy_count, email_column.shape[0]))
        input("Press Enter to copy the next batch")
    print("No more entries to copy")


copy_emails(email_column, iter_count, copy_count)
