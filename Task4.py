import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load your CSV
df = pd.read_csv('reviews.csv')  # Make sure this file has the text column

# 🔍 Check what columns exist
print("📋 Available Columns:", df.columns)

# Adjust based on actual column name
text_column = 'Review'  # Change this if your column name is different

# Analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis
df['Sentiment'] = df[text_column].apply(analyze_sentiment)

# Summary
print(df.head())

# Plot
df['Sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'gray'])
plt.title("Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.show()
