import csv
import random
from faker import Faker

fake = Faker()

# Emotion categories and corresponding sentence templates
emotion_templates = {
    'joy': [
        "I'm so happy about {thing}!",
        "This is the best day ever because of {thing}!",
        "I feel absolutely delighted by {thing}.",
        "What a wonderful {thing} we're experiencing!",
        "My heart is full of joy because of {thing}.",
        "I can't stop smiling about {thing}!",
        "{thing} makes me feel ecstatic!",
        "I'm over the moon about {thing}!",
        "This {thing} brings me so much happiness!",
        "I'm thrilled beyond words about {thing}!"
    ],
    'anger': [
        "I'm absolutely furious about {thing}!",
        "This {thing} makes me so angry I could scream!",
        "How dare they {thing}!",
        "I'm boiling with rage because of {thing}.",
        "{thing} has me seeing red!",
        "I'm so mad I can't even think straight about {thing}!",
        "This {thing} is completely unacceptable!",
        "I'm enraged by {thing}!",
        "My blood is boiling because of {thing}!",
        "{thing} is making me livid!"
    ],
    'sadness': [
        "I'm feeling so down about {thing}...",
        "This {thing} has me feeling blue.",
        "I can't stop crying about {thing}.",
        "My heart aches because of {thing}.",
        "I'm overwhelmed with sorrow about {thing}.",
        "{thing} is making me feel so lonely.",
        "I'm in the depths of despair because of {thing}.",
        "This {thing} has left me heartbroken.",
        "Tears won't stop falling because of {thing}.",
        "I'm grieving over {thing}."
    ],
    'fear': [
        "I'm terrified of {thing}!",
        "This {thing} scares me to death!",
        "I can't handle the fear of {thing}.",
        "My anxiety about {thing} is overwhelming.",
        "I'm shaking with fear because of {thing}.",
        "The thought of {thing} fills me with dread.",
        "I'm paralyzed with fear about {thing}.",
        "{thing} is my worst nightmare!",
        "I can't sleep because I'm so scared of {thing}.",
        "My heart races whenever I think about {thing}."
    ],
    'surprise': [
        "I'm completely shocked by {thing}!",
        "I never expected {thing} to happen!",
        "{thing} took me completely by surprise!",
        "I'm astonished by {thing}!",
        "Wow! I can't believe {thing} happened!",
        "{thing} left me speechless!",
        "I'm flabbergasted by {thing}!",
        "This {thing} came out of nowhere!",
        "What an unexpected {thing}!",
        "My jaw dropped when I saw {thing}!"
    ],
    'love': [
        "I adore {thing} with all my heart!",
        "My love for {thing} knows no bounds.",
        "I'm head over heels for {thing}!",
        "{thing} makes my heart flutter!",
        "I cherish {thing} more than words can say.",
        "My affection for {thing} grows every day.",
        "I'm completely enamored with {thing}!",
        "{thing} is the love of my life!",
        "I feel such deep love for {thing}.",
        "My soul is filled with love because of {thing}."
    ],
    'neutral': [
        "I'm thinking about {thing}.",
        "This {thing} is neither good nor bad.",
        "I noticed {thing} today.",
        "{thing} happened as expected.",
        "I observed {thing} without much reaction.",
        "There's nothing special about {thing}.",
        "{thing} is just normal.",
        "I'm indifferent about {thing}.",
        "{thing} doesn't affect me much.",
        "This {thing} is quite ordinary."
    ]
}

# Things to fill in the templates
things = [
    "the weather", "my job", "my relationship", "this situation", "the news",
    "my family", "my friends", "this decision", "the future", "the past",
    "this movie", "this book", "this song", "this food", "this place",
    "this event", "this conversation", "these changes", "this opportunity",
    "this challenge", "my health", "my finances", "this memory", "this moment",
    "this achievement", "this failure", "this surprise", "this gift",
    "this realization", "this discovery"
]

# Generate sentences
sentences = []
for _ in range(21000):  # Generate 2100 sentences
    emotion = random.choice(list(emotion_templates.keys()))
    template = random.choice(emotion_templates[emotion])
    thing = random.choice(things)
    sentence = template.format(thing=thing)
    sentences.append(sentence)  # Only storing the sentence now

# Shuffle the sentences
random.shuffle(sentences)

# Write to CSV file with only one column
with open('21000emotion_test_sentences.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['sentence'])  # Single column header
    for sentence in sentences:
        writer.writerow([sentence])

print("emotion_test_sentences.csv")