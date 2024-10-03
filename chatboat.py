import nltk
nltk.download('punkt')
nltk.download('wordnet')

import spacy
spacy.cli.download("en_core_web_sm")

import nltk
from nltk.chat.util import Chat, reflections
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

pairs = [
    [
        r"(hi|hello|hey)",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Hey! How can I help?"]
    ],
    [
        r"what is your name ?",
        ["I am a simple chatbot created using Python.", "You can call me Chatbot!"]
    ],
    [
        r"how are you ?",
        ["I'm just a bunch of code, so I don't have feelings, but thanks for asking! How are you?"]
    ],
    [
        r"(.*)(location|city)",
        ["I'm virtual, so I don't have a location, but I'm here to help you no matter where you are."]
    ],
    [
        r"what (.*) do ?",
        ["I can chat with you, answer some of your questions, and provide information."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day.", "See you later!", "Bye! Take care."]
    ],
]

# Initialize the chatbot with the pairs
chatbot = Chat(pairs, reflections)
def chatbot_response(user_input):
    # Use spaCy to process the user input (optional for more advanced processing)
    doc = nlp(user_input.lower())
    
    # Generate response using NLTK-based Chat
    response = chatbot.respond(user_input)
    
    return response

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("Chatbot:", chatbot_response(user_input))
        break
    
    response = chatbot_response(user_input)
    print("Chatbot:", response)
