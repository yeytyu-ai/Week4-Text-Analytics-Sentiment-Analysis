from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = " ".join(df["Cleaned_Review"])

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white"
).generate(text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Beauty and Wellness Customer Reviews Word Cloud")
plt.show()
