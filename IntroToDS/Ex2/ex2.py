import pandas as pd
import numpy as np
import string
from stemming.porter2 import stem
#C:\Python27\python -m pip install stemming
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk import PorterStemmer
from nltk.tokenize import word_tokenize

with open('Automotive_5.json') as f:
    content = f.readlines()
json= '[' + ','.join([x.strip('\n') for x in content]) + ']'

df = pd.read_json(json)

#1 remove punctuation
table = dict.fromkeys(map(ord, string.punctuation))
stop_words = set(stopwords.words('english'))

def remove_punctuation(text):
    text = text.translate(table)
    #return text.lower()
    #return PorterStemmer().stem(text.lower())
    text = PorterStemmer().stem(text.lower())
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    return ' '.join(filtered_sentence)

df['reviewText'] = df['reviewText'].apply(remove_punctuation)
df[df['overall'] >= 4]['reviewText'].to_csv('pos.txt', header=None, index=None)
df[df['overall'] <= 2]['reviewText'].to_csv('neg.txt', header=None, index=None)

print(df[df['overall'] >= 4].head(20).to_string())

