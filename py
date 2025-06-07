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
# Add a new column 'in_stock' that is True if quantity > 0, else False
inventory['in_stock'] = inventory['quantity'] > 0
# print(inventory)

# Add a new column 'total_value' calculated by multiplying price by quantity
inventory['total_value'] = inventory['price'] * inventory['quantity']
# print(inventory)
# Create a lambda function to combine product_type and product_description into one string
combine_lambda = lambda row: f'{row.product_type} - {row.product_description}'

# Apply the lambda function row-wise to create a 'full_description' column
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

# Print the updated inventory DataFrame with new columns
print(inventory)
