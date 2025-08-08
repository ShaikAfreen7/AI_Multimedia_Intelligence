def run_lstm(text_path):
    with open(text_path, "r") as file:
        text = file.read().lower()
    if "happy" in text or "joy" in text:
        return "Sentiment: Positive"
    elif "sad" in text or "angry" in text:
        return "Sentiment: Negative"
    else:
        return "Sentiment: Neutral"
