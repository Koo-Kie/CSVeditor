import csv

# Set the input and output file names
input_file = "data.csv"
output_file = "output.csv"

# Open the input file for reading
with open(input_file, "r") as f:
    reader = csv.reader(f)
    data = [row for row in reader]

# Strip any extra commas from the end of each row
for row in data:
    while len(row) > 0 and row[-1] == "":
        row.pop()

# Open the output file for writing
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
    
print(f"{input_file} has been stripped and saved as {output_file}")