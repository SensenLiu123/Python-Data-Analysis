"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

"""
Problem 1: Reading the field names from a CSV file
First, you will write a function called read_csv_fieldnames that takes the 
name of a CSV file and returns a list of the field names from that file. 
This function assumes that the first row of the CSV file contains the field 
names. As CSV files can use different separator characters and quote characters,
this function takes those characters as input and uses them to properly parse 
the CSV file.
"""

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    table = []
    count = 0
    with open(filename, "r") as csvfile:
        # csv.reader => from csv import reader function 
        csvreader = csv.reader(csvfile,delimiter=separator,
                               quotechar=quote)
        for row in csvreader:
            table.append(row)
            count+=1 
            if count>1: return table[0]
    

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    table = []
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   delimiter=separator,
                                   quotechar=quote)
        for row in csvreader:
            table.append(row)
    return table

"""
Problem 3: Reading a CSV file into a dictionary of dictionaries
Next, you will write a function called read_csv_as_nested_dict that takes the 
name of a CSV file and returns the data within the file as a dictionary of 
dictionaries. Each key-value pair in the outer dictionary corresponds to a row 
in the CSV file. The keys in that dictionary are the values of a header column 
in the table. The function takes the name of that header column as the input 
keyfield. If a key appears multiple times in column corresponding to keyfield, 
the last row containing the key is used to create the dictionary used as the 
corresponding value.The inner dictionaries within the outer dictionary map the 
field names to the column values for that row. As CSV files can use different 
separator characters and quote characters, this function takes those characters
 as input and uses them to properly parse the CSV file. Note that the key-value
 pair for keyfield should be in the inner dictionaries, even though its value 
 is used as the key in the outer dictionary.
"""

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   delimiter=separator,
                                   quotechar=quote)
        for row in csvreader:
            table[row[keyfield]] = row
    return table

"""
Problem 4: Writing a list of dictionaries to a CSV file
Finally, you will write a function called write_csv_from_list_dict. This 
function takes a table structured as a list of dictionaries (as if read by 
read_csv_as_list_dict) and writes it to the file named by the 
filename input. The function also takes a list of field names, 
fieldnames, as input in order to make sure the fields appear in the appropriate
 order (as specified by the order of the list fieldnames) in the CSV file. 
 The function also takes a separator character and a quote character that 
 should be used when writing the file. All non-numeric fields should be quoted 
 using the specified quote character.
"""

def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    table = []
    for dit in table:
        a_row = []
        for fieldname in fieldnames:
            a_row.append(dit[fieldname])
        table.append(a_row)

    file_handle = open(filename, 'wt', newline='')
    #
    csv_write = csv.writer(file_handle, delimiter=separator, quotechar=quote, 
                       quoting=csv.QUOTE_NONNUMERIC)
    csv_write.writerow(fieldnames)
    for row in table:
        csv_write.writerow(row)
    filename.close()