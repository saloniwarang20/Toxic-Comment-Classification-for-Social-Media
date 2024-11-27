# Toxic Comment Classification for Social Media 🔍

This is a toxic comment classifier web application that uses deep learning models to predict the toxicity levels of a given text input.

## 📝 Table of Contents
- 🧐 [About](#about)
- 🎯 [Getting Started](#getting-started)
- 📊 [Dataset Overview](#dataset-overview)
- 🧠 [Model Building](#model-building)
- 🎈 [Usage](#usage)
- 🌟 [Support](#support)

## 🧐 About
This is a multi-label classification problem where the given input is a text comment, and the output is a list of toxicity labels it belongs to, such as:

- toxic
- severe-toxic
- obscene
- threat
- insult
- identity hate

The input text data needs to be cleaned and pre-processed for it to be useful for the machine learning models.

For the best results, we used **BiLSTM** (Bidirectional LSTM) as the classifier, which performed well on the test data.

## 🎯 Getting Started
### Project Structure:

```bash
Toxic Comment Classification Project
├───models
│   ├───saved_models
│   └───best_bilstm_model.h5
├───notebooks
├───static
│   ├───images
│   └───style.css
├───templates
│   └───index.html
├───tasks.db
├───tokenizer1.pkl
├───submission.csv
└───app.py

```

### Prerequisites:
- **Python 3.x** (>= 3.8)
- TensorFlow
- Keras
- Flask
- Pandas
- Numpy
- Scikit-learn
- Matplotlib

## 📊 Dataset Overview
The dataset for this project was taken from a competition hosted by Jigsaw on Kaggle.

For preprocessing of the input data and text vectorization, both word and character-based TF-IDF vectorizer outputs are used as inputs to the model for better performance and minimal loss of input features.

## 🧠 Model Building
For building the classifier, we have used several deep learning models and compared their performance:

- **ANN (Artificial Neural Network)**
- **LSTM (Long Short-Term Memory)**
- **BiLSTM (Bidirectional LSTM)**
- **CNN (Convolutional Neural Network)**

The **BiLSTM** model achieved the highest test accuracy of **99.94%**, and it was chosen for deployment.

### Model Evaluation Metrics:
- **Validation Accuracy:** 0.9828
- **Validation F1-Score:** 0.9812
- **Test Accuracy:** 0.9752
- **Test F1-Score:** 0.9747

## 🎈 Usage
To run the web app locally:

1. Navigate to the main project folder.
2. Run the following command to start the Flask server:

```bash
python app.py
```
3. The server will be available at localhost:5000.
4. Go to localhost:5000, enter a comment, and click "ANALYZE" to predict its toxicity level.

## 🌟 Support
Please hit the ⭐ button if you like this project. 😄

Thank you for your support!


