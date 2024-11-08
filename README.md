# Mental Disorder Prediction

This project aims to predict the mental health status of individuals based on various input parameters using machine learning techniques. The system analyzes user-provided data, such as lifestyle, behavior, and survey responses, to predict the likelihood of mental health issues such as anxiety, depression, and stress.


### Prerequisites

Before running this project, ensure that you have the following installed:

- Python 3.x
- pip (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/IshikaSaini001/Mental-Disorder-Prediction.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Mental-Disorder-Prediction
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure all data files (such as survey data) are in the correct format (e.g., CSV, JSON).
2. Run the prediction script:
   ```bash
   python predict.py
   ```

3. The model will output a prediction, such as:
   ```
   Prediction: Depression Risk (High)
   ```

## Data

This project requires a dataset with information on mental health, including but not limited to:

- Lifestyle factors (e.g., sleep patterns, exercise)
- Behavioral data (e.g., social media use, screen time)
- Survey responses related to emotional well-being

Ensure that the data is preprocessed and cleaned before feeding it into the model.

## Model

This project uses machine learning algorithms such as:

- **Logistic Regression**: For binary classification of mental health conditions.
- **Random Forest**: To evaluate the importance of different features.
- **Neural Networks**: For more complex patterns in data.

The models can be found in the `models/` directory.

## Contributing

We welcome contributions! If you'd like to contribute, please fork this repository, make your changes, and submit a pull request. Make sure to follow the guidelines:

1. Write clear and concise commit messages.
2. Follow the coding standards of the project.
3. Write tests for any new features or fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Dataset Source] – For providing the data used in the model.
- [Machine Learning Libraries] – For tools like scikit-learn and TensorFlow that power the model.
