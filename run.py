from flask import Flask, render_template, request
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

app = Flask(__name__)
tokenizer = DistilBertTokenizer.from_pretrained(r'C:\Users\Aniket\Downloads\model_14-07-2024')
model = DistilBertForSequenceClassification.from_pretrained(r'C:\Users\Aniket\Downloads\model_14-07-2024')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    sample_text = request.form['inputText']
    inputs = tokenizer(sample_text, return_tensors='pt')
    outputs = model(**inputs)
    predicted_label_id = outputs.logits.argmax().item()
    predicted_label = model.config.id2label[predicted_label_id]

    label_dict = {
        'LABEL_8': ['positive', 'desire'],
        'LABEL_0': ['positive', 'pride'],
        'LABEL_17': ['positive', 'joy'],
        'LABEL_5': ['positive', 'caring'],
        'LABEL_15': ['positive', 'gratitude'],
        'LABEL_18': ['positive', 'love'],
        'LABEL_7': ['ambiguous', 'curiosity'],
        'LABEL_13': ['positive', 'excitement'],
        'LABEL_21': ['positive', 'optimism'],
        'LABEL_20': ['ambiguous', 'neutral'],
        'LABEL_14': ['negative', 'fear'],
        'LABEL_26': ['negative', 'remorse'],
        'LABEL_3': ['negative', 'annoyance'],
        'LABEL_11': ['negative', 'disgust'],
        'LABEL_12': ['negative', 'embarrassment'],
        'LABEL_9': ['negative', 'disappointment'],
        'LABEL_2': ['negative', 'anger'],
        'LABEL_6': ['ambiguous', 'confusion'],
        'LABEL_23': ['ambiguous', 'realization'],
        'LABEL_27': ['ambiguous', 'surprise']
    }

    emotion_text = label_dict[predicted_label][0]
    confidence = label_dict[predicted_label][1]

    return render_template('index.html', inputText=sample_text, detectedEmotion=emotion_text, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True)
