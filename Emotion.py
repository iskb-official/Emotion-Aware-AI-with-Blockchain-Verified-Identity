import pandas as pd
from transformers import pipeline
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration
MODEL_PATH = "./emotion-english-distilroberta-base"
CSV_FILE = "21000emotion_test_sentences.csv"
OUTPUT_FILE = "21000emotion_analysis_results.csv"

# Load the emotion classifier
emotion_classifier = pipeline(
    "text-classification",
    model=MODEL_PATH,
    tokenizer=MODEL_PATH,
    return_all_scores=False
)

# Load the test data
df = pd.read_csv(CSV_FILE)

# Analyze samples in batches to avoid memory issues
batch_size = 100
predictions = []
confidences = []

for i in range(0, len(df), batch_size):
    batch = df['sentence'].iloc[i:i+batch_size].tolist()
    results = emotion_classifier(batch, truncation=True)
    predictions.extend([res['label'] for res in results])
    confidences.extend([res['score'] for res in results])

# Add predictions to DataFrame
df['predicted_emotion'] = predictions
df['confidence'] = confidences

# Save full results
df.to_csv(OUTPUT_FILE, index=False)

# Generate analysis metrics
if 'expected_emotion' in df.columns:
    print("\nClassification Report:")
    print(classification_report(df['expected_emotion'], df['predicted_emotion']))
    
    # Confusion matrix
    cm = confusion_matrix(df['expected_emotion'], df['predicted_emotion'])
    plt.figure(figsize=(10,8))
    sns.heatmap(cm, annot=True, fmt='d', 
                xticklabels=emotion_classifier.model.config.id2label.values(),
                yticklabels=emotion_classifier.model.config.id2label.values())
    plt.title('Confusion Matrix')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.savefig('confusion_matrix.png')
    plt.close()
    print("Confusion matrix saved as confusion_matrix.png")

# Calculate confidence statistics
confidence_stats = df.groupby('predicted_emotion')['confidence'].describe()
print("\nConfidence Statistics:")
print(confidence_stats)

# Sample some high and low confidence predictions
print("\nHigh Confidence Examples:")
print(df.sort_values('confidence', ascending=False).head(5)[['sentence', 'predicted_emotion', 'confidence']])

print("\nLow Confidence Examples:")
print(df.sort_values('confidence').head(5)[['sentence', 'predicted_emotion', 'confidence']])

print(f"\nAnalysis complete. Full results saved to {OUTPUT_FILE}")