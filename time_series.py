import numpy as np
import csv
import sys

source_files= {
    "ew_csv_file_path": r'source_file.EW',
    "ns_csv_file_path": r'source_file.NS',
    "ud_csv_file_path": r'source_file.UD',
}

print('hello nikesh ---->')

sys.exit(0)

# Function to read i_values from a CSV file, starting from the 18th row and reading 8 values per row
def read_i_values_from_csv(file_path):
    i_values = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for i, row in enumerate(csv_reader):
            if i >= 17:  # Skip the first 17 rows
                for value in row[:8]:
                    # Split the string by whitespace and filter out any empty strings
                    split_values = filter(None, value.split())
                    i_values.extend(float(v) for v in split_values)
    return i_values

# Read i_values from the CSV file

# Calculate scale factor SF
SF = max(i_values) / 8388608.0

# Define time increment and create time array from 0 to 1 with step of 0.004
time_increment = 0.004
time_array = np.arange(0, 40 + time_increment, time_increment)

# Ensure the length of i_values matches the length of time_array
# If i_values has fewer elements, we will cycle through the list
# If i_values has more elements, we will truncate the list
i_values_extended = np.resize(i_values, time_array.shape)

# Calculate velocities
velocities = i_values_extended * SF

# Write results to a new CSV file
output_csv_file_path = r'output_file.csv'

def generate_csv_file(output_csv_file_path, time_array, velocities):
    with open(output_csv_file_path, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Time', 'Velocity'])  # Write header
        for t, v in zip(time_array, velocities):
            csv_writer.writerow([t, v])
    return output_csv_file_path



def write_file():
    return generate_csv_file(output_csv_file_path, time_array, velocities)
