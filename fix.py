import csv

input_file_loc = "Subaru_impreza_original.csv"
output_file_loc = "Subaru_impreza_fixed.csv"

# Open the CSV file for reading and create a new CSV file for writing
with open(input_file_loc, 'r') as input_file, open(output_file_loc, 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Iterate through each row in the input CSV file
    for row in reader:

        # print(row[2])

        price_int = int(row[2].strip().replace('$', '').replace('*', ''))
        odo_int = int(row[3].strip().replace(',', '').replace(' km', ''))

        row[7] = row[7].replace('//cars', '/cars')

        row.append(price_int)
        row.append(odo_int)

        # Write the updated row to the output CSV file
        writer.writerow(row)
