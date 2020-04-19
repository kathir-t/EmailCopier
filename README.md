# EmailCopier
Copy Emails in batches for sending bulk email batchwise

## Usage
```
usage: email_copier.py [-h] csv column copy_count

positional arguments:
  csv         Name of the CSV file
  column      Name of the column you want to copy
  copy_count  Number of entries to copy in one batch

optional arguments:
  -h, --help  show this help message and exit
```

### Example
```
python email_copier.py 100_sample_contacts.csv email 10
```
