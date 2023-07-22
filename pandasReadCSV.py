import pandas as pd

df = pd.read_csv("data.csv")

pd.options.display.max_rows = 9999 

print(df.info())

