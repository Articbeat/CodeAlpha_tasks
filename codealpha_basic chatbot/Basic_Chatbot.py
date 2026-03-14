print("welcome to the Asjad's chatbot!")
print("type 'exit' to quit the chatbot")
def chatbot():
    while True:
        user = input("enter a message: ").lower()
     
        if user == "hello" or user == "hi":
            print("hi how are you?")
        elif user == "how are you?":
            print("i am fine, thank you")
        elif user == "what is your name?":
            print("my name is chatbot")
        elif user == "exit":
            print("goodbye!")
            break
        else:
            print("i don't understand that")
chatbot()
