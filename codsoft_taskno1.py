def simple_chatbot(user_input):
    user_input = user_input.lower()
    
    greetings = ["hello", "hi", "hey"]
    farewells = ["bye", "goodbye", "see you"]
    questions = ["how are you", "what's up", "how's it going"]
    
    if user_input in greetings:
        response = "Hello! How can I help you?"
    elif user_input in farewells:
        response = "Goodbye! Have a great day!"
    elif any(q in user_input for q in questions):
        response = "I'm just a simple chatbot, but I'm here to assist you!"
    else:
        response = "I'm sorry, I don't understand that."
    
    return response

def main():
    print("Simple Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Simple Chatbot: Goodbye! Have a great day!")
            break
        response = simple_chatbot(user_input)
        print("Simple Chatbot:", response)

if __name__ == "__main__":
    main()
