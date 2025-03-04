def spam_detector(message):
    spam_keywords = ["win", "free", "cash", "prize"]
    for word in message.lower().split():
        if word in spam_keywords:
            return "Spam"
    return "Not Spam"

print(spam_detector("You won a free prize!"))  # Output: Spam
