import pickle
from flask import Flask, request, render_template
from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore

app = Flask(__name__)

# Load the model
model = keras.models.load_model("best_bilstm_model.h5")

# Load the tokenizer
with open('tokenizer1.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

max_length = 200  # Adjust based on your model's input length

@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = ""
    if request.method == "POST":
        comment = request.form["comment"]
        
        # Preprocess the comment
        cleaned_comment = comment.lower()
        cleaned_comment = ''.join(char for char in cleaned_comment if char.isalnum() or char.isspace())
        
        sequences = tokenizer.texts_to_sequences([cleaned_comment])
        padded_sequence = pad_sequences(sequences, maxlen=max_length, padding='post')

        # Predict using the model
        predictions = model.predict(padded_sequence)

        # Interpret predictions
        labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
        prediction_results = [labels[i] for i, val in enumerate(predictions[0]) if val > 0.5]

        # Construct the output message
        if prediction_results:
            prediction_text = f"The comment is classified as: {', '.join(prediction_results)}"
        else:
            prediction_text = "Yay! The comment is clean."
        
    return render_template("index.html", prediction=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
