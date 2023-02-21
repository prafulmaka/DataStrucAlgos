
import pandas as pd

# initialize list elements
data = [10,20,30,40,50,60]

# Create the pandas DataFrame with column name is provided explicitly
df = pd.DataFrame(data, columns=['Numbers'])

# print dataframe.
print(df)