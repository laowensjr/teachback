import os
import csv

cereal_csv = os.path.join(os.getcwd(), "Resources", "cereal.csv")

# Open and read csv
with open(cereal_csv, newline="" ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    #for row in csvreader:
        
        #List Comprehension
    #row = [fields for fields in csvreader if float(fields[7]) >= 5]
        
    
    # List of Dictionaries
    results = [fields for fields in csv.DictReader(open(cereal_csv, newline="" )) if float(fields['fiber']) > 5]
   
        # Convert row to float and compare to grams of fiber
        #if float(row[7]) > 5:
           # print(row)
   
    print(results)