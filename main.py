import pandas as pd

#load data from the csv file
data=pd.read_csv("cw/titanic.csv")

print(data.head())
print(data.head(10))

print(data.describe())

print(data.info())

#select multiple columns together
p_classAndname=data[["Pclass","Name"]]
print(p_classAndname.head())
print(p_classAndname.shape)
print(p_classAndname.dtypes)

df = pd.DataFrame(data)

#combine multiple conditions together
class2and3=data[(data["Pclass"]==2)|(data["Pclass"]==3)]

print(class2and3[["Name","Pclass"]].head(15))

#females 1st class & males 3rd class survived

females1stclass=data[(data["Pclass"]==1)&(data["Sex"]=="female")]
print(females1stclass.head(20))

males3rdclasssurvived=data[(data["Pclass"]==3)&(data["Sex"]=="male")&(data["Survived"]==1)]
print(males3rdclasssurvived.head(20))