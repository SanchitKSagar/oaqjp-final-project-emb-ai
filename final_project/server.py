"""Flask server for detecting emotions from text input."""
from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """Endpoint that receives text and returns emotion analysis."""
    text_to_analyze = request.args.get('textToAnalyze')
    data = emotion_detector(text_to_analyze)
    dominant = data.pop("dominant_emotion")
    if dominant is None:
        return "Invalid text! Please try again!"
    items = [f"'{k}': {v}" for k, v in data.items()]
    formatted_scores = ", ".join(items[:-1]) + f" and {items[-1]}"
    return (f"For the given statement, the system response is {formatted_scores}. "
    f"The dominant emotion is {dominant}.")
