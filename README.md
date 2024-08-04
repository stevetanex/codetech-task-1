# codtech task-1 
# SOCIAL MEDIA SENTIMENT ANALYSIS
## Name:STEVE TANEX P
## Company:CODTECH IT SOLUTIONS
## ID:CT4DA5250
## Domain:DATA ANALYTICS
## Duration:July to 20,August,2024
## Mentor:Muzammil Ahmed
## Contact: +91 96401 28015 

# objective topic"task-4  SOCIAL MEDIA SENTIMENT ANALYSIS"
perfomed data analysis on the topic "tweets sentiment analysis" from the provided data set and created  simple data representation in tableau software and charts in spreadsheets. 

# code
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


# screenshots
![Screenshot 2024-08-01 184842](https://github.com/user-attachments/assets/6a04b6f8-ef28-4167-a7e0-3075aacb0400)
![Screenshot 2024-08-03 222808](https://github.com/user-attachments/assets/ffac961c-9647-4289-8a35-85e12431d529)
![Screenshot 2024-08-03 222948](https://github.com/user-attachments/assets/7c39588e-912a-400b-a946-8d54a3c46b60)
![Screenshot 2024-08-03 223045](https://github.com/user-attachments/assets/289b7ea2-cc92-4d6c-a9f5-f9e9813c8f1e)
![Screenshot 2024-08-03 223633](https://github.com/user-attachments/assets/b75169b4-6735-4ef5-9121-dc21c756074c)
![Screenshot 2024-08-03 223947](https://github.com/user-attachments/assets/aeb30ea0-ff46-4220-985b-d1ea59a8f50c)
![Screenshot 2024-08-03 224329](https://github.com/user-attachments/assets/7aebbc63-577b-4058-8fc9-060fd1ec5627)

![Screenshot 2024-08-03 224441](https://github.com/user-attachments/assets/89e9ae91-7516-4a0d-843a-6937414669e4)
![Screenshot 2024-08-03 224530](https://github.com/user-attachments/assets/e425f4be-6cc7-49d0-acc1-fc3adcedd296)









