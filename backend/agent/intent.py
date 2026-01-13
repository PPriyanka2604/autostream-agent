def detect_intent(user_input: str) -> str:
    """
    Classifies user intent into:
    - greeting
    - product_inquiry
    - high_intent
    """

    text = user_input.lower()

    # Casual greetings
    if any(word in text for word in ["hi", "hello", "hey", "good morning", "good evening"]):
        return "greeting"

    # High intent signals (ready to try or buy)
    if any(phrase in text for phrase in [
        "sign up",
        "get started",
        "try the pro",
        "try pro",
        "i want pro",
        "i want the pro",
        "for my channel",
        "for my youtube",
        "for my instagram"
    ]):
        return "high_intent"

    # Everything else defaults to product inquiry
    return "product_inquiry"
