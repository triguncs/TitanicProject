# Titanic Survival Prediction

A simple machine learning project that predicts whether a Titanic passenger
survived based on passenger information.

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
- Evaluated them using accuracy, precision, recall and F1-score
- Used 5-fold cross-validation

## Results

| Model | Test Accuracy | Mean CV Accuracy |
|---|---:|---:|
| Logistic Regression | 79.21% | 79.64% |
| Random Forest | 80.90% | 80.66% |

Random Forest performed slightly better overall, but its high training
accuracy indicated overfitting.

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Files

- `Titanic_dataset.ipynb` — Complete analysis and machine learning notebook
