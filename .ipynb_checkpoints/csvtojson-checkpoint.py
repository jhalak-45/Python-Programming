import csv
import json

# Define the CSV file path and JSON file path
csv_file_path =input("Enter path:")  # Replace with your CSV file path
json_file_path =input("Destationation path:")  # Replace with your desired JSON file path

# Read the CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)  # Read as a dictionary
    data = list(csv_reader)  # Convert to a list of dictionaries

# Convert the list of dictionaries to JSON and write to a file
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)  # Write JSON with pretty print

print(f'Converted {csv_file_path} to {json_file_path}')
