from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Sample dataset of questions and answers
questions = [
    "What is your name?",
    "How are you?",
    "What is the weather today?",
    "How old are you?",
    "Tell me a joke."
]
answers = [
    "I am ChatBot.",
    "I'm doing well, thank you!",
    "I'm not sure. You can check a weather website.",
    "I don't have an age. I'm just a computer program.",
    "Why don't skeletons fight each other? They don't have the guts."
]

# Vectorize the text data
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Train a k-nearest neighbors model
knn_model = NearestNeighbors(n_neighbors=1, algorithm='brute', metric='cosine')
knn_model.fit(X)

# Function to generate response
def generate_response(input_text):
    input_vector = vectorizer.transform([input_text])
    _, index = knn_model.kneighbors(input_vector)
    return answers[index[0][0]]

# Chatbot interface
def chatbot():
    print("Hi! I'm ChatBot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        response = generate_response(user_input)
        print("ChatBot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
