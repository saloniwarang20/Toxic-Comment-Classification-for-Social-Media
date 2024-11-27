# Toxic Comment Classification Project

This project uses deep learning models to classify toxic comments into various categories such as "toxic," "severe toxic," "obscene," "threat," "insult," and "identity hate." The goal of this project is to predict whether a given comment contains harmful content based on the provided data.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Model Architecture](#model-architecture)
5. [Results](#results)

## Project Overview
The project focuses on classifying toxic comments using various machine learning models, including:
- **ANN (Artificial Neural Network)**
- **LSTM (Long Short-Term Memory)**
- **BiLSTM (Bidirectional LSTM)**
- **CNN (Convolutional Neural Network)**

The models are trained and evaluated using the **Toxic Comment Classification** dataset, and the best-performing model (BiLSTM) is deployed as part of a Flask application.

## Installation

### Prerequisites:
- Python 3.x
- TensorFlow
- Keras
- Flask
- Pandas
- Numpy
- Scikit-learn
- Matplotlib

You can install the required dependencies by running:
```bash
pip install -r requirements.txt
