import matplotlib.pyplot as plt

sentiment_counts = df["Sentiment"].value_counts()

print("Sentiment Distribution:")
print(sentiment_counts)

sentiment_counts.plot(kind="bar")

plt.title("Customer Review Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)

plt.show()
