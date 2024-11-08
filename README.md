
# Mental Disorder Prediction App

## Overview

The **Mental Health Disorder Prediction App** uses machine learning to predict mental health disorders based on user input regarding their mood and behavioral traits. The app analyzes answers to a series of questions and provides insights into potential mental health conditions. The results include prediction confidence for each possible disorder, represented in an interactive pie chart.

This tool is designed for educational purposes only and is not intended to replace a professional diagnosis. If you or someone you know is experiencing mental health challenges, it is always recommended to seek guidance from a qualified mental health professional.

## Features

- **Prediction Model:** Predicts the mental health disorder based on the user's responses.
- **Confidence Scores:** Displays prediction confidence for each possible disorder.
- **User-Friendly Interface:** Allows users to input their mood and behavioral traits using sliders and dropdowns.
- **Visualization:** Provides an interactive pie chart to show prediction confidence.

## How It Works

The app is powered by a machine learning model that was trained on a dataset with various mental health-related factors. The model uses **Random Forest Classifier** and **Naive Bayes Classifier** with a **Voting Classifier** for improved prediction accuracy.

Users are prompted to answer several questions related to their emotions, behavior, and habits. Based on these answers, the app predicts the mental health disorder that most aligns with their responses and presents the results.

## Project Structure

```plaintext
.
├── app.py                 # Main Streamlit application file
├── model.pkl              # Trained machine learning model
├── Mental-Disorders.csv   # Dataset used for training the model
├── pexels-scottwebb-305821.jpg  # Background image for the app (can be replaced)
└── README.md              # Project description and setup instructions
```

## Installation

### Prerequisites

- Python 3.x
- Streamlit
- Plotly
- Scikit-learn
- Pandas
- Numpy
- Pickle

You can install the required libraries using `pip`:

```bash
pip install streamlit plotly scikit-learn pandas numpy
```

### Running the App

To run the app, make sure the files are in the same directory, and then run the following command:

```bash
streamlit run app.py
```

This will start a local server, and you can access the app by navigating to `http://localhost:8501` in your web browser.

### Loading the Trained Model

The machine learning model is stored in `model.pkl` and should be loaded by the app during runtime. If you'd like to retrain the model or use a different one, replace `model.pkl` with your own trained model.

### Image for Background

An image named `pexels-scottwebb-305821` is included for the app's background. You can replace this with any image of your choice by placing it in the same directory and updating the file path in `app.py`.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Here are a few ways you can help:

- Improve the user interface or make it more interactive.
- Enhance the prediction model by using different algorithms or techniques.
- Add more features to the app, such as mood tracking or journaling.


## Acknowledgements

- The dataset `Mental-Disorders.csv` was used to train the prediction model.
- Background image from Pexels: [pexels-scottwebb-305821](https://www.pexels.com/photo/photo-of-person-holding-paper-305821/).
