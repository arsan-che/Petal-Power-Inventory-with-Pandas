import codecademylib3
import pandas as pd

# Load inventory data from CSV file into a DataFrame
inventory = pd.read_csv('inventory.csv')

# Filter for the first 10 rows where the location is Staten Island
staten_island = inventory[inventory['location'] == 'Staten Island'].head(10)
# print(staten_island)
# Extract product descriptions from the Staten Island filtered data
product_request = staten_island['product_description']
# print(product_request)

# Filter inventory for products located in Brooklyn AND of product type 'seeds'
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]
