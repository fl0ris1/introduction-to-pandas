"""
Titanic Mini Investigation
Concept Focus: Real dataset + conditional selection
Task:
Load the Titanic dataset

Answer all the below questions:

How many passengers were above 60?

How many females travelled in 1st class?

Average fare for 3rd class passengers

How many children (Age < 12) survived?
"""

import pandas as pd

data = pd.read_csv("titanic.csv")

print(data.head())

plus60 = len(data[data["Age"]>60])
print(f"There were {plus60} passengers above 60\n")

fem1stclass = data[(data["Sex"]=="female") & (data["Pclass"]==1)]
print(f"There were {fem1stclass.shape[0]} females that travelled in 1 class")

average_fair = data[(data["Pclass"] == 3)]["Fare"].mean()
print(f"The average fare for passengers in class 3 was {average_fair.round(2)}$")

children_12min_survived = len(data[(data["Age"]<12) & (data["Survived"] == 1)])
print(f"{children_12min_survived} children under 12 survived")