#Read through an online course in SQL
#   sqlcourse.com, sql-tutorial.net, ...

#Write a python program to lookup the scientific name for a user-supplied
#organism name.

import sys
import sqlite3

if len(sys.argv) < 2:
    print("Usage: python WillistonHW11Q2.py <common_name>")
    sys.exit()
    
common_name = sys.argv[1]
conn = sqlite3.connect('taxa.db3')                      #connect to database
c = conn.cursor()

#JOIN name table to tax_id
query = """
    SELECT sci.name, com.name_class
    FROM name sci
    JOIN name com ON sci.tax_id = com.tax_id                
    WHERE com.name = ?
        AND sci.name_class = 'scientific name'
    LIMIT 1;
    """
c.execute(query, [common_name])                         #execute the query with the common name input
found=False                                                 
for row in c:
    scientific_name = row[0]                            #get the scientific name
    print("Scientific Name:", scientific_name)
    found=True
    break

if not found:
    print("Scientific name not found for this organism")

conn.close()
