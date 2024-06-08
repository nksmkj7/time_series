import numpy as np
import csv
import pandas as pd


station = 'ST01'
source_files= [
    {"source_file": r'source_file.NS','output_file': r'output_file.NS',type:'NS', 'max_vel': 0.004100},
    {"source_file": r'source_file.UD','output_file': r'output_file.UD', type:'UD','max_vel': 0.005042},
    {"source_file": r'source_file.EW','output_file': r'output_file.EW',type:'EW', 'max_vel': 0.003635},
]


velocity_lists={}

# Define time increment and create time array from 0 to 1 with step of 0.004
time_increment = 0.004
time_array = np.arange(0, 40 + time_increment, time_increment)
# Calculate scale factor SF


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


def generate_csv_file(output_csv_file_path, time_array, velocities,row_data = ['Time','Velocity']):
    zip_data=zip(time_array,*velocities)
    with open(output_csv_file_path, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([station])
        csv_writer.writerow(row_data)  # Write header
        for t, *v in zip_data:
            row = [t]
            row.extend(v)
            csv_writer.writerow(row)
    return output_csv_file_path


for index,file_info in enumerate(source_files):
    [source_file, output_file,type,max_vel ] = file_info.values()
    i_values = read_i_values_from_csv(source_file)
    SF = max_vel / 8388608.0

    # Ensure the length of i_values matches the length of time_array
    # If i_values has fewer elements, we will cycle through the list
    # If i_values has more elements, we will truncate the list
    i_values_extended = np.resize(i_values, time_array.shape)

    # Calculate velocities
    velocities = i_values_extended * SF
    velocity_lists[type] = velocities  
    generate_csv_file(output_file, time_array, [velocities])
    

generate_csv_file('final_result.csv', time_array, list(map(lambda x: list(x), velocity_lists.values())),['Time'] + list(velocity_lists.keys()))


# def write_file():
#     return generate_csv_file(output_csv_file_path, time_array, velocities)
