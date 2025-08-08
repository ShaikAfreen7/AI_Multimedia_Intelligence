def run_bert(text_path):
    with open(text_path, "r") as file:
        text = file.read().lower()
    if "angry" in text:
        return "Emotion: Anger"
    elif "happy" in text:
        return "Emotion: Happiness"
    elif "fear" in text:
        return "Emotion: Fear"
    else:
        return "Emotion: Neutral"
