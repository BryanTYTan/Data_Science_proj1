import pandas as pd
import numpy as np

def get_citystate(item):
        if ' (' in item:
            return item[:item.find(' (')]
        elif '[' in item:
            return item[:item.find('[')]
        else:
            return item


university_towns = []

with open('Data_sets/university_towns.txt') as file:
    for line in file:
        if '[edit]' in line:
            state = line
        else:
            university_towns.append((state, line))

# data with [edit] in them
towns_df = pd.DataFrame(university_towns, columns=['State', 'RegionName'])

# "dirt" is not localized to one column, use applymap that applies a function to all elements in DF
towns_df =  towns_df.applymap(get_citystate)

print(towns_df.head())