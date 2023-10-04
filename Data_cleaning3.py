import pandas as pd
import numpy as np

olympics_df = pd.read_csv('Data_sets/olympics.csv', header=1)

# lots of messy data
new_names =  {'Unnamed: 0': 'Country', '? Summer': 'Summer Olympics', '01 !': 'Gold', '02 !': 'Silver', '03 !': 'Bronze', '? Winter': 'Winter Olympics', '01 !.1': 'Gold.1', '02 !.1': 'Silver.1', '03 !.1': 'Bronze.1', '? Games': '# Games', '01 !.2': 'Gold.2', '02 !.2': 'Silver.2', '03 !.2': 'Bronze.2'}

# Rename the columns
olympics_df.rename(columns=new_names, inplace=True)

print(olympics_df.head())