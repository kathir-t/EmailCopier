# EmailCopier
Copy Emails in bulk to paste in online

## Usage
```
usage: email_copier.py [-h] csv column copy_count delimiter

positional arguments:
  csv         Name of the CSV file
  column      Name of the column you want to copy
  copy_count  Number of entries to copy in one batch
  delimiter   Delimiter to concatenate the data

optional arguments:
  -h, --help  show this help message and exit
```

### Example
```
python email_copier.py  graphics\ -\ Sheet2.csv E-mail\ Id: 100 ,
```
