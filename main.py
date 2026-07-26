import pandas as pd

#load data from the csv file
data=pd.read_csv("titanic.csv")

print(data.head())
print(data.head(10))

print(data.describe())

print(data.info())

#select multiple columns together
p_classAndname=data[["Pclass","Name"]]
print(p_classAndname.head())
print(p_classAndname.shape)
print(p_classAndname.dtypes)

kbenzodagga

'''df = pd.DataFrame(data)

print(df)'''