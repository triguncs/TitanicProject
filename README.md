# Titanic Survival Prediction

A simple machine learning project that predicts whether a Titanic passenger survived based on passenger information.

## Dataset

Titanic passenger dataset containing information such as:

- Passenger class
- Sex
- Age
- Number of siblings/spouses
- Number of parents/children
- Fare
- Port of embarkation

## What I Did

- Explored the dataset using Pandas and Matplotlib
- Handled missing values
- Selected relevant features
- Encoded categorical features
- Split the data into training and testing sets
- Trained Logistic Regression and Random Forest models
- Compared the two models
- Evaluated the models using accuracy, precision, recall and F1-score
- Used 5-fold cross-validation

## Results

| Model | Test Accuracy | Mean CV Accuracy |
|---|---:|---:|
| Logistic Regression | 79.21% | 79.64% |
| Random Forest | 80.90% | 80.66% |

Random Forest performed slightly better overall, but its high training accuracy indicated overfitting.

## Streamlit App

The project also includes a Streamlit web app where you can enter passenger details and get a survival prediction from the trained Random Forest model.

### Run Locally

1. Clone the repository:

   `git clone https://github.com/triguncs/TitanicProject.git`

2. Open the project folder:

   `cd TitanicProject`

3. Install the required libraries:

   `pip install streamlit pandas numpy matplotlib scikit-learn joblib`

4. Run the Streamlit app:

   `python -m streamlit run app.py`

5. Open the local URL shown in the terminal, usually:

   `http://localhost:8501`

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib

## Files

- `Titanic_dataset.ipynb` — Complete analysis and machine learning notebook
- `app.py` — Streamlit web application
- `titanic_model.pkl` — Trained Random Forest model
- `README.md` — Project documentation
