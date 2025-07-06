import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('21000emotion_analysis_results.csv')

# Emotion distribution
emotion_counts = df['predicted_emotion'].value_counts()
print("Emotion Distribution:\n", emotion_counts)

# Plot
emotion_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Predictions per Emotion')
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('emotion_distribution.png')
plt.show()