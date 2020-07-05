# https://pypi.org/project/GetOldTweets3/
# https://medium.com/@AIY/getoldtweets3-830ebb8b2dab
# https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1

"""
Mini projet Twitter

Etape 1: récupérer des tweets sur le sujet de votre choix via l'api de twitter et ou scrapping

GetOldTweets3 is a free Python 3 library that allows you to scrape data from twitter without requiring any API keys. 
It also allows you to scrape historical tweets.

First 1000 tweets that include the word "Municipales2020" in France from 28/06/2020 and 29/06/2020.

Run: GetOldTweets3 --querysearch "Municipales2020" --maxtweets 1000
"""

import GetOldTweets3 as got

text_query = 'Municipales2020'
since_date = '2019-06-28'
until_date = '2019-06-29'
count = 1000# Creation of query object


# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query).setSince(since_date).setUntil(until_date).setMaxTweets(count).setLang("fr")# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)# Creating list of chosen tweet data
text_tweets = [[tweet.date, tweet.text] for tweet in tweets]

