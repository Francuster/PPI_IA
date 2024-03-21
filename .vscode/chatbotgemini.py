import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords  # Import stopwords for preprocessing

# Sample training data (consider expanding for better accuracy)
data = pd.DataFrame({
    'text': [
        "Can you help me with a refund?",
        "What are your opening hours?",
        "I'd like to place an order.",
        "Hello! How can I help you today?"
    ],
    'category': [
        "complaint",
        "question",
        "order",
        "greeting"
    ]
})

# Preprocess text data (lowercase, remove stop words, optional stemming/lemmatization)
stop_words = stopwords.words('english')
data['text_processed'] = data['text'].apply(lambda text:
                                             ' '.join([word for word in text.lower().split() if word not in stop_words]))

# Feature extraction using TF-IDF vectorization
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(data['text_processed'])
y_train = data['category']

# Train a classifier model (Naive Bayes in this example)
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Chatbot loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    # Preprocess user input
    user_input_processed = ' '.join([word for word in user_input.lower().split() if word not in stop_words])
    user_input_vectorized = vectorizer.transform([user_input_processed])

    # Predict category using the trained model
    predicted_category = classifier.predict(user_input_vectorized)[0]

    # Provide a response based on the predicted category
    response_map = {
        "complaint": "I'm sorry to hear you're having trouble. Let me know how I can assist you.",
        "question": "I'm happy to answer any questions you have.",
        "order": "Sure, let's get started with placing your order.",
        "greeting": "Hello! How can I be of service today?"
    }
    print("Chatbot:", response_map.get(predicted_category, "I'm still under development and learning to understand your requests better."))
