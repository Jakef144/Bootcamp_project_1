import pandas as pd

# Load the CSV file
file_path = r"C:\Class project 1\death-rates-from-mental-and-substance-disorders-by-age-who.csv"
data = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Information:")
print(data.info())

# Display summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Display the first few rows of the dataset
print("\nFirst Few Rows:")
print(data.head())

