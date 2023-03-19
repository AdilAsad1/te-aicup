import csv

# Open the input and output files
with open('data.csv', 'r') as f_in, open('bu2_appliances.csv', 'w', newline='') as f_out:
    # Create a CSV reader and writer objects
    reader = csv.DictReader(f_in)
    writer = csv.DictWriter(f_out, fieldnames=reader.fieldnames)
    writer.writeheader()  # Write the header to the output file

    # Loop through the rows in the input file and filter based on the specified conditions
    for row in reader:
        if (row['company_region_name_level_1'] == 'Americas' and
            row['business_unit_group_name'] == 'Appliances'):
            writer.writerow(row)