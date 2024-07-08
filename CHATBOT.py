def chatbot_response(user_input):
    user_input = user_input.lower().strip()  

    
    if user_input in ["hello", "hi", "hey"]:
        return "Hello! How can I help you today?"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm a chatbot, so I don't have feelings, but I'm here to help you!"
    elif user_input in ["what's your name", "who are you"]:
        return "I'm a simple rule-based chatbot created to assist you."
    elif "help" in user_input:
        return "Sure, I can help you! What do you need assistance with?"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase? If I can't solve your problem, you might want to consult our support team."

def main():
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
