import pandas as pd
import numpy as np

data=pd.read_csv("iris.csv")

print(data.head())

print(data.info())

print(data.dtypes)


def calculateStats(df):
    stats={}
    for column in ['sepal_length','sepal_width','petal_length','petal_width']:
        stats[column]={
            'mean':df[column].mean(),
            'smallest':df[column].min(),
            'biggest':df[column].max()
        }

    return stats

statistics=calculateStats(data)

print("\nstatistics: ")

for col, stat in statistics.items():
    print(f"{col}: mean = {stat['mean']}, smallest = {stat['smallest']}, biggest= {stat['biggest']}")


#count number of rows present for each type of species in the datas\et
species_count=data['species'].value_counts()
print("\nSpecies Counts: ")
for species, count in species_count.items():
    print(f"{species} : {count}")