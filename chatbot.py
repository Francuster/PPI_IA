import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load data from CSV file
# Function to load data from CSV file
def load_data_from_csv(csv_file):
    questions = []
    answers = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in reader:
            questions.append(row[0])
            answers.append(row[1])
    return questions, answers

# Load questions and answers from CSV
questions, answers = load_data_from_csv('data.csv')

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
