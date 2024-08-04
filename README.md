# codetech-task-1
Name:STEVE TANEX P
company:CODTECH IT SOLUTIONS
ID:CT4DA5250
Domain:DATA ANALYIST
Duration:July to  20 August ,2024
Mentor:Muzammil Ahmed
Contact: +91 96401 28015 

objective: To analyise the given data set and to represent the given data in simpler form


# tweets sentiments analysis
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




![Screenshot 2024-08-01 184842](https://github.com/user-attachments/assets/dc5ec726-f63c-442f-b76a-07a9a7fde757)



![Screenshot 2024-08-03 222808](https://github.com/user-attachments/assets/03806fcd-2f71-493a-88ca-89d6ba42af95)


