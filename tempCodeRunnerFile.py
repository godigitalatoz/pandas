import pandas as pd

mydata = {
    "cars" : ["BMW", "Volvo", "Ford"],
    "passings" : [3, 5, 7]
} 

myvar = pd.DataFrame(mydata)

print(myvar)