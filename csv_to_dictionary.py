'''
* Open file
* use csv.DictReader() to extract as dictionary (but of type DictReader)
* extract rows and convert into int and append every row into main dictionary data
'''

import csv

data = [] # Its a list of dictionaries. 1 dictionary = 1 row
column_heads = [] # list of headings

# Open the CSV file
with open('data.csv', mode='r') as file:
    table = csv.DictReader(file) # table from csv extracted as type class DictReader
    column_heads = table.fieldnames # extracts headings for using as keys in dictionaries
  
    for row in table: # it is extracted in string format, therefore it has to be converted to int
        for column_head in column_heads:
            row[column_head] = int(row[column_head])
        data.append(row)

print(data)
