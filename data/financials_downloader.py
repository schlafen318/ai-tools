import csv
import requests
import os

# Read links from the CSV file
csv_path = "Financials - AMZN.csv"
links = []

with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        links.append(row[2])  # Assuming the links are in the first column

# Directory on your machine where you want to save the reports
save_directory = "amzn_reports/"

# Create the directory if it doesn't exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Download and save each link
for link in links:
    response = requests.get(link)
    filename = os.path.join(save_directory, link.split("/")[-1])
    with open(filename, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {link} to {filename}")
