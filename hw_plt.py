import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('cw/titanic.csv')

class1=data[(data["Pclass"]==1)]
class2=data[(data["Pclass"]==2)]
class3=data[(data)["Pclass"]==3]
clas_tot=[len(class1),len(class2),len(class3)]
classes=["1","2","3"]

plt.bar(classes,clas_tot)
plt.xlabel("Class")
plt.ylabel("Passenger Count")
plt.title("Passenger Count per Class on Titanic")
plt.show()