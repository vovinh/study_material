import pandas as pd
import numpy as np

#1. read data
df = pd.read_csv("train.csv")

#2. remove Name column
del df['Name']

#check if a column has NaN value
#print(df.isnull().any())

#3. first character
def get_first_char(row):
    if row.isnull()['Cabin']:
        return row['Cabin']
    return row['Cabin'][0]
df['Deck'] = df.apply(lambda row : get_first_char(row), 1)

#4. Convert to int
def convert_to_int(row):
    if row.isnull()['Deck']:
        return row['Deck']
    return ord(row['Deck']) - ord('A');
df['Deck'] = df.apply(lambda row : convert_to_int(row), 1)
#5. 
#calc avg
ageAvg = int(df['Age'].mean())
df['Age'].fillna(ageAvg, inplace=True); 
#replace by mode
modeDeck = df['Deck'].mode()[0]
df['Deck'].fillna(modeDeck, inplace=True); 


embarkedDeck = df['Embarked'].mode()[0]
df['Embarked'].fillna(embarkedDeck, inplace=True); 


#6. write files
df.to_csv('ex1_out.csv')
df.to_json('ex1_out.json')


#print(df.head(20).to_string())