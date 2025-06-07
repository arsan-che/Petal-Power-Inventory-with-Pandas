import codecademylib3
import pandas as pd

# Load inventory data from CSV file into a DataFrame
inventory = pd.read_csv('inventory.csv')

# Filter for the first 10 rows where the location is Staten Island
staten_island = inventory[inventory['location'] == 'Staten Island'].head(10)
# print(staten_island)
