"""
Mini projet Twitter

Etape 2:
Créer une fonction qui compte le nombre de mots d'une phrase, un fonction qui prend en entrée une phrase et qui ressort une liste de mots sans les stopwords 
=> NEW : Faire des tests unitaires pour chaque fonction !

Run: python3 apply_twitter.py
"""

import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



tweet = pd.read_csv('output_got.csv')

# ETAPE 1 : Passage en minuscule
def tweet_lower(sentence):
    result = sentence.lower()
    return result

# ETAPE 2: Tokenisation
def tweet_tokenisation(sentence):    
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    tokenized_tweet = tokenizer.tokenize(sentence)
    return tokenized_tweet

# ETAPE 3: Retrait des stopwords
def del_stop_word(sentence): 
    stop_words = set(stopwords.words('french'))
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(sentence)
 
    new_sentence = []
 
    for word in words:
        if word not in stop_words:
            new_sentence.append(word)
 
    return new_sentence

# ETAPE 4 : Nombre de word
def word_number(sentence):
    result = len(sentence)
    return result

# ETAPE 5: Dataframe
tweet["tweet_lower"] = tweet["text"].apply(tweet_lower)  
tweet["tokenized_tweet"] = tweet["tweet_lower"].apply(tweet_tokenisation)  
tweet["no_stop_words"] = tweet["tweet_lower"].apply(del_stop_word)
tweet["word_number"] = tweet["no_stop_words"].apply(word_number)

data = [tweet['username'],tweet['date'], tweet['text'], tweet["word_number"], tweet["no_stop_words"]]
df_tweet = pd.concat(data, axis=1)
print(df_tweet.head())

df_tweet.to_csv('df_tweet.csv')
df_tweet.to_json('df_tweet.json', orient='records')
print("exportation csv et json, ok!")