from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment.polarity, sentiment.subjectivity

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form['text']
    polarity, subjectivity = analyze_sentiment(user_input)
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return render_template('index.html', sentiment=sentiment, polarity=polarity, subjectivity=subjectivity, text=user_input)

if __name__ == '__main__':
    app.run(debug=True)
