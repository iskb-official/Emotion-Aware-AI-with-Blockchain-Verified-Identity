import pandas as pd
from transformers import pipeline

# Step 1: Load the CSV file
df = pd.read_csv("sentiment_data_1000.csv")

# Step 2: Load the sentiment classifier
classifier = pipeline("sentiment-analysis")

# Step 3: Run sentiment analysis on each text
texts = df["Text"].tolist()
results = classifier(texts, truncation=True)

# Step 4: Add sentiment and confidence to the DataFrame
df["Sentiment"] = [res["label"] for res in results]
df["Confidence"] = [res["score"] for res in results]

# Step 5: Save the results to a new CSV file
df.to_csv("sentiment_results_1000.csv", index=False)

print("Sentiment analysis complete. Results saved to sentiment_results_1000.csv")
