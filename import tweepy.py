import tweepy
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Function to clean tweet text
def clean_tweet(tweet):
    tweet = re.sub(r'http\S+', '', tweet)  # Remove URLs
    tweet = re.sub(r'@\w+', '', tweet)  # Remove mentions
    tweet = re.sub(r'#', '', tweet)  # Remove hashtags
    tweet = re.sub(r'\W', ' ', tweet)  # Remove special characters
    tweet = re.sub(r'\s+', ' ', tweet)  # Remove extra whitespace
    tweet = tweet.lower()  # Convert to lowercase
    return tweet

# Function to get sentiment
def get_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')
api = tweepy.API(auth)

# Collect tweets
query = 'specific topic'
tweets = tweepy.Cursor(api.search_tweets, q=query, lang='en', since='2022-01-01', until='2022-12-31').items(1000)

# Create DataFrame
data = {'tweet': [], 'sentiment': [], 'date': []}
for tweet in tweets:
    clean_text = clean_tweet(tweet.text)
    sentiment = get_sentiment(clean_text)
    data['tweet'].append(clean_text)
    data['sentiment'].append(sentiment)
    data['date'].append(tweet.created_at.date())

df = pd.DataFrame(data)

# Aggregate sentiment scores
sentiment_trends = df.groupby(['date', 'sentiment']).size().unstack(fill_value=0)

# Plot sentiment trends
plt.figure(figsize=(14, 7))
sns.lineplot(data=sentiment_trends)
plt.title('Sentiment Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Tweets')
plt.show()
