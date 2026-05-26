from datetime import datetime


def chatbot_response(command):
    command = command.lower()

    if "hello" in command:
        return "Hello, how can I help you?"

    elif "time" in command:
        return datetime.now().strftime("Current time is %H:%M")

    elif "your name" in command:
        return "I am Jarvis Assistant"

    elif "help" in command:
        return "How can I assist you today?"

    else:
        return "Sorry, I did not understand"
