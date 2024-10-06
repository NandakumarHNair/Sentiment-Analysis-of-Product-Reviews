import sqlite3
import csv
import os

# Connect to the SQLite database
connection = sqlite3.connect('sentimental_analysis.db')
cursor = connection.cursor()

# Query to select all data from the product_reviews table
cursor.execute("SELECT * FROM product_reviews")

# Fetch all rows
rows = cursor.fetchall()

# Get column names
column_names = [description[0] for description in cursor.description]

# Specify the file path for the CSV (save to the data/ folder)
csv_file_path = os.path.join('data', 'product_reviews.csv')

# Create the data directory if it doesn't exist
os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

# Write the rows to a CSV file in the data/ folder
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(column_names)
    
    # Write all the data
    writer.writerows(rows)

print(f"Data successfully written to {csv_file_path}")

# Close the database connection
connection.close()

