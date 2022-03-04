# MOUNTING THE DRIVE
from google.colab import drive
drive.mount('/content/gdrive')

%cd /content/gdrive/MyDrive/Sales Analysis Project

# IMPORTING LIBRARIES
import pandas as pd
import os

# MERGING 12 MONTHS DATA TO A SINGLE CSV FILE
## df = pd.read_csv("/content/gdrive/MyDrive/Sales Analysis Project/SalesAnalysis/Sales_Data/Sales_April_2019.csv")

files = [file for file in os.listdir("/content/gdrive/MyDrive/Sales Analysis Project/SalesAnalysis/Sales_Data")]

all_months_data = pd.DataFrame()

for file in files:

  df = pd.read_csv("/content/gdrive/MyDrive/Sales Analysis Project/SalesAnalysis/Sales_Data/"+ file)
  all_months_data = pd.concat([all_months_data, df])

all_months_data.to_csv("All_data.csv", index = False)    

# READ IN UPDATED DATAFRAME
all_data = pd.read_csv("/content/gdrive/MyDrive/Sales Analysis Project/All_data.csv")
all_data.head()

# DROP ROWS OF NaN(so that we can convert string month to int type)
nan_df = all_data[all_data.isna().any(axis=1)]
nan_df.head()
all_data = all_data.dropna(how = 'all')

# DROP ROWS WHOSE ORDER DATE COLUMN IS HAVING "Or" INSTEAD OF DATE
## temp_df = all_data[all_data['Order Date'].str[0:2] == 'Or']
## temp_df.head()
## INSTEAD OF DROPING THE UNWANTED COLUMN, WE CAN ASSIGN THE WANTED COLUMN TO THE DATA FRAME
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

# CHANGING TYPE OF QUANTITY ORDERED AND PRICE COLUMN TO INT AND FLOAT RESPECTIVELY
all_data['Quantity Ordered'] = all_data['Quantity Ordered'].astype(int) #to int
all_data['Price Each'] = pd.to_numeric(all_data['Price Each']) #another way of type casting 

# ADDING MONTH COLUMN
all_data['Month'] = all_data['Order Date'].str[0:2]
## TYPE CASTING STRING VALUE TO INT VALUE
all_data['Month'] = all_data['Month'].astype(int)  
all_data.head()

# ADD A SALES COLUMN
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
all_data.head()

# ADD A CITY COLUMN
def get_city(address):
  return address.split(',')[1]

def get_state(address):
  return address.split(',')[2].split(' ')[1]

all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) + ' (' + get_state(x) + ')')## we can also use f string for appending
all_data.head()

# BEST MONTH FOR SALES
results = all_data.groupby('Month').sum()
import matplotlib.pyplot as plt
months = range(1,13)
plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month Number')
plt.show()

# BEST CITY FOR SALES
results = all_data.groupby('City').sum()
results

import matplotlib.pyplot as plt
##cities = all_data['City'].unique() ## as due to this our x values are getting arranged in different order as compared to y values i.e sales
cities = [city for city, df in all_data.groupby('City')]

plt.bar(cities, results['Sales'])
plt.xticks(cities, rotation = 'vertical', size= 8)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month Number')
plt.show()

# What time should we display advertisements to maximize likelihood of customers buying product ?

all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])

all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute
all_data.head()

hours = [hour for hour, df in all_data.groupby('Hour')]
plt.plot(hours, all_data.groupby(['Hour']).count())
plt.xticks(hours)
plt.xlabel('Hour')
plt.ylabel('Number of Orders')
plt.grid()
plt.show

##recommendation is around 11am or 7pm

# What products are most often sold together?

df = all_data[all_data['Order ID'].duplicated(keep=False)]
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df = df[['Order ID', 'Grouped']].drop_duplicates()
df.head()

## wrong cuz suppose if in our grouped column one row value comes like 20in Monitor,27in FHD Monitor and in some other
## row it is goven as 27in FHD Monitor,20in FHD Monitor then it will comsider both of them as different values instead
##it should cosider them as same values but arran=ged in different orders.
#new_df = df
#new_df.groupby(['Grouped']).count() 

from itertools import combinations
from collections import Counter
count = Counter()

for row in df['Grouped']:
  row_list = row.split(',')
  count.update(Counter(combinations(row_list,2)))

for key, value in count.most_common(10):
  print(key,value)
  
# What product sold the most?

product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered'] 

products = [product for product, df in product_group]

plt.bar(products, quantity_ordered)
plt.ylabel('Quantity Ordered')
plt.xlabel('Product')
plt.xticks(products, rotation = 'vertical', size = 8)
plt.show()

# Overlaying a second Y-Axis

prices  = all_data.groupby('Product').mean()['Price Each']
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(products, quantity_ordered, color='g')
ax2.plot(products, prices, 'b-')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price ($)', color='g')
ax1.set_xticklabels(products, rotation = 'vertical', size=8)

plt.show()
