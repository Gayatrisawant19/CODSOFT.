# Simple rule-based chatbot using if-else statements

def chatbot():
    print("Hello! I am a simple chatbot. How can I help you today?")
    
    while True:
        # Get input from the user
        user_input = input("You: ").lower()
        
        # Check for common user inputs and respond
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        
        elif "your name" in user_input:
            print("Chatbot: I am your friendly chatbot. I don't have a specific name.")
        
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M")
            print(f"Chatbot: The current time is {current_time}.")
        
        elif "exit" in user_input or "bye" in user_input:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you rephrase?")

# Start the chatbot
chatbot()
