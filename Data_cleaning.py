import pandas as pd
import numpy as np

df = pd.read_csv('Data_sets/BL-Flickr-Images-Book.csv')

to_drop = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Contributors', 'Issuance type', 'Shelfmarks']
df.drop(columns=to_drop, inplace=True, axis=1)

df.set_index('Identifier', inplace=True)

# accessing Specific indexes
# By Idex number - print(df.loc[206])
# By index position - print(df.iloc[0])

print(df.dtypes.value_counts(),"\n")

print(df.loc[1905:, 'Date of Publication'].head(10),"\n")
# Dates are messy

extr = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
print(extr.head(),"\n")

# convert obj dtype -> numerical
df['Date of Publication'] = pd.to_numeric(extr)
print(df['Date of Publication'].dtype, "\n")


pub = df['Place of Publication']
london = pub.str.contains('London')
oxford = pub.str.contains('Oxford')
print(london[:5], "\n")


df['Place of Publication'] = np.where(london, 'London', np.where(oxford, 'Oxford', pub.str.replace('-', ' ')))
print(df.head())
