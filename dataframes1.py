import pandas as pd
data = {
    "calories" : [420, 380, 390],
    "duration" : [50, 40, 45]
}

df = pd.DataFrame(data, index = ["mon", "tue", "wed"])

print(df)