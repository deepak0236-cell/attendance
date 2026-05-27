responses = {
    "hello": "Hello Student",
    "attendance": "Your attendance is 89%",
    "marks": "Your marks are updated"
}

def chatbot(message):

    message = message.lower()

    return responses.get(
        message,
        "I do not understand"
    )