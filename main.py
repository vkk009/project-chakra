from speech_to_text import recognize_speech
from text_to_speech import speak
from chatbot import chatbot_response

print("Jarvis Assistant Started...")

while True:
    print("1. Voice Input")
    print("2. Text Input")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        text = recognize_speech()
        print("User:", text)

        response = chatbot_response(text)
        print("Jarvis:", response)
        speak(response)

    elif choice == '2':
        text = input("Type your message: ")

        response = chatbot_response(text)
        print("Jarvis:", response)
        speak(response)

    elif choice == '3':
        speak("Goodbye")
        break

    else:
        print("Invalid choice")
