faq = {
    "how to mark attendance":
    "Open dashboard and scan QR",

    "forgot password":
    "Use reset password option"
}

def get_answer(question):

    return faq.get(
        question.lower(),
        "Question not found"
    )