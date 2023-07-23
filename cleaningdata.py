import pandas as pd

df = pd.read_csv('data_1.csv')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset=['Date'], inplace=True)

x = df['Calories'].median()[0]
df["Calories"].fillna(x, inplace=True)

print(df.to_string())