import streamlit as st
import pandas as pd
import joblib
import time

st.title("Titanic Survival Predictor")

start = time.time()

model = joblib.load("titanic_model.pkl")

st.write("Model loaded in:", round(time.time() - start, 2), "seconds") # for seeing how fast model loads on streamlit


# taking input from user and storing in respecive variables (to be used further for making the individual's dataframe)
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["Male", "Female"])
age = st.number_input("Age", min_value=0, max_value=100, value=25, step=1
)
sibsp = st.number_input("Siblings / Spouses", min_value=0, max_value=10, value=0)
parch = st.number_input("Parents / Children", min_value=0, max_value=10, value=0)
fare = st.number_input("Fare", min_value=0.0, value=30.0)
embarked = st.selectbox(
    "Port of Embarkation",
    ["Southampton", "Cherbourg", "Queenstown"]
)

if st.button("Predict"):

    sex_value = 0 if sex == "Male" else 1 

    embarked_c = 1 if embarked == "Cherbourg" else 0
    embarked_q = 1 if embarked == "Queenstown" else 0  # writing 3 conditions because ive used one-hot encoding 
    embarked_s = 1 if embarked == "Southampton" else 0


    # finally creating the input dataframe as a pandas dataframe (similar to x_test but here we only have 1 row)
    my_data = pd.DataFrame([{
        "Pclass": pclass,
        "Sex": sex_value,
        "Age": age,  
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked_C": embarked_c,
        "Embarked_Q": embarked_q,
        "Embarked_S": embarked_s
    }])

    my_data = my_data[model.feature_names_in_] # arranging the columns in the same order as the training data to avoid errors

    prediction = model.predict(my_data)
    
    # also showing probability of survival
    probability = model.predict_proba(my_data)

    if prediction[0] == 1:
        st.success("🎉 You would have survived!")
    else:
        st.error("Unfortunately, you would not have survived.")

    st.write(
        f"Survival probability: {probability[0][1] * 100:.1f}%"
    )