sentiment_counts = df["Sentiment"].value_counts()

total_reviews = len(df)

print("Total Reviews:", total_reviews)
print("\nSentiment Analysis Results:")

for sentiment, count in sentiment_counts.items():
    percentage = (count / total_reviews) * 100

    print(sentiment, ":", count, "reviews")
    print("Percentage:", round(percentage, 2), "%")
    print()
