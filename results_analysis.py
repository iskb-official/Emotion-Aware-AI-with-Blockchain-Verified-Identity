import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file with column names
df = pd.read_csv('21000emotion_analysis_results.csv', names=['text', 'emotion', 'confidence_score'])

# Step 2: Categorize data by emotion and save to new CSV
# This will sort the data by emotion for easier categorization
df_sorted = df.sort_values(by='emotion')
df_sorted.to_csv('categorized_emotions.csv', index=False)
print("Categorized data saved to 'categorized_emotions.csv'.")

# Step 3: Plot confidence score distribution for each emotion
plt.figure(figsize=(10, 6))
for emotion in df['emotion'].unique():
    subset = df[df['emotion'] == emotion]
    plt.hist(subset['confidence_score'], bins=20, alpha=0.5, label=emotion)

plt.xlabel('Confidence Score')
plt.ylabel('Frequency')
plt.title('Confidence Score Distribution by Emotion')
plt.legend()
plt.tight_layout()
plt.savefig('confidence_score_by_emotion.png')
plt.show()

# Confidence statistics per emotion
conf_stats = df.groupby('emotion')['confidence_score'].describe()
print("\nConfidence Score Statistics by Emotion:\n", conf_stats)

# Boxplot for confidence scores
plt.figure(figsize=(10, 6))
df.boxplot(column='confidence_score', by='emotion')
plt.title('Confidence Score by Emotion')
plt.suptitle('')
plt.xlabel('Emotion')
plt.ylabel('Confidence Score')
plt.tight_layout()
plt.savefig('confidence_boxplot.png')
plt.show()