# Toxic Comment Classification using Flask 🔍

[![forthebadge](https://forthebadge.com/images/badges/now-maintained.svg)](https://forthebadge.com)

This is a toxic comment classifier web application that uses deep learning models to predict the toxicity levels of a given text input.

[Link to the web app](http://localhost:5000) *(replace with actual deployment link if available)*

Disclaimer: The dataset for this project contains text that may be considered profane, vulgar, or offensive.

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

## 🎯 Getting Started
### Project Structure:

```bash
Toxic Comment Classification Project
├───data
│   ├───cleaned-data
│   └───raw-data
├───images
├───models
├───notebooks
├───static
│   └───css
├───templates
└───__pycache__
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
