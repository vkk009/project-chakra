from text_to_speech import speak


def emergency_alert():
    message = "Emergency! Help needed"

    print(message)
    speak(message)


if __name__ == "__main__":
    emergency_alert()
