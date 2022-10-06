import pandas as pd
#Missing Values 
missingvalues_df = pd.read_csv("MissingValuesDataSet.csv")
x = 5
x > 5
x == 5
pd.isnull(missingvalues_df).head()
missingvalues_df[pd.isnull(missingvalues_df).any(axis=1)]