"""Flask web server for Watson NLP emotion detection."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detection():
    """Handle emotion detection requests from user input."""
    if request.method == 'POST':
        text_to_analyze = request.form['text']
    else:
        text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_output = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']}, 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_output


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
