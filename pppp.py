import csv
import pandas as pd


def f(i, j):
    # Your function that produces a value for a given i and j
    return i + j


# Define the range for i and j
i_range = range(0, 10)
j_range = range(0, 10)

# Create a list to store the data
data = []

# Loop through the range for i and j
for i in i_range:
    for j in j_range:
        # Calculate the value for f(i, j)
        value = f(i, j)
        # Append the values for i, j, and value to the data list
        data.append([i, j, value])

# Write the data to a CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['i', 'j', 'value'])
    # Write the data rows
    writer.writerows(data)

df = pd.read_csv('data.csv')
print(df.head())
