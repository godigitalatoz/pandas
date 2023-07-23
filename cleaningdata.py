import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_2.csv')

y = df['Calories'].median()
df["Calories"].fillna(y, inplace=True)

for x in df.index:
    if df.loc[x , "Duration"] > 120:
        df.loc[x, "Duration"] = 120
df.drop_duplicates(inplace = True)


plt.show()