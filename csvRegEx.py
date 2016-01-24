""" @file csvRegEx
    @author Matthew Chan
    @date 01/24/2016
    @brief This program reads from a .csv file containing two columns (name, phone) and
    outputs a .csv file with all names and phone numbers organized

    Inputted names and numbers from the .csv file are formatted in various ways
    i.e. Luna, Candace X.
         Candace X. Luna
         Candace Luna
         1-(318)-266-1334
         318.266.1334
         3182661334
         318 266 1334
     The outputted names and numbers are all of the same format and are split into 4 columns (first, middle, last, phone)
     i.e. First      M.I.  Last   Phone
          Candance   X.    Luna   (318) 266-1334

"""
import re
import csv

# Open files for reading and writing
ifile = open('data.csv', 'rb')
reader = csv.reader(ifile)
ofile = open('data2.csv', 'wb')
writer = csv.writer(ofile)

# Write the header for the output .csv file
lines = [line.strip() for line in ifile]
header = ['First', 'M.I.', 'Last', 'Phone']
writer.writerow(header)

# Use regular expressions to search each row of the input .csv file and capture data, then print to output .csv file
for line in lines:
    comma = re.search(r'(\w+)\,\s(\w+)\s?(\w?\.?).*(\d{3})\)?[\-\.\s]?(\d{3})[\-\.]?(\d{4})', line)
    if comma:
        phone = "(" + comma.group(4) + ")" + " " + comma.group(5) + "-" + comma.group(6)
        rows = [comma.group(2), comma.group(3), comma.group(1), phone]
        writer.writerow(rows)
    noComma = re.search(r'(\w+)\s?(\w?\.?)\s(\w{2,}).*(\d{3})\)?[\-\.\s]?(\d{3})[\-\.]?(\d{4})', line)
    if noComma:
        phone = "(" + noComma.group(4) + ")" + " " + noComma.group(5) + "-" + noComma.group(6)
        rows = [noComma.group(1), noComma.group(2), noComma.group(3), phone]
        writer.writerow(rows)
        
# Close the files (all reading and writing has been completed)
ifile.close()
ofile.close()

