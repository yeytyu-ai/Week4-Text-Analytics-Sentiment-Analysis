df["Tokens"] = df["Cleaned_Review"].apply(lambda text: text.split())

print(df[["Cleaned_Review", "Tokens"]].to_string(index=False))
