from flask import Flask, request, jsonify
from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch

app = Flask(__name__)

tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForSequenceClassification.from_pretrained('digital.eaj.se.com/SEMV_Failure_Management/bot/roberta_symptom_classifier')
model.eval()

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()
    text = data.get("text")
    
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(probabilities).item()
    confidence = probabilities[0][predicted_class].item()
    
    return jsonify({
        'predicted_class': predicted_class,
        'confidence': confidence
    })

if __name__ == '__main__':
    app.run(debug=True)