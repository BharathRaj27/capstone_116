import pickle
import streamlit as st
import pandas as pd
from PIL import Image
model_file = 'model1.pkl'

with open(model_file, 'rb') as f_in:
	model = pickle.load(f_in)
# creating a function for Prediction

def churn_prediction(gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges):

    prediction=model.predict([[gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges]])
    print(prediction)
    return prediction

def main():
	add_selectbox = st.sidebar.selectbox(
	"How would you like to predict?",
	("Online", "Batch"))
	st.title("Predicting Customer Churn")

	if add_selectbox == 'Online':
		gender = st.selectbox('Gender:', ['male', 'female'])
		seniorcitizen= st.selectbox(' Customer is a senior citizen:', [0, 1])
		partner= st.selectbox(' Customer has a partner:', ['yes', 'no'])
		dependents = st.selectbox(' Customer has  dependents:', ['yes', 'no'])
		phoneservice = st.selectbox(' Customer has phoneservice:', ['yes', 'no'])
		multiplelines = st.selectbox(' Customer has multiplelines:', ['yes', 'no', 'no_phone_service'])
		internetservice= st.selectbox(' Customer has internetservice:', ['dsl', 'no', 'fiber_optic'])
		onlinesecurity= st.selectbox(' Customer has onlinesecurity:', ['yes', 'no', 'no_internet_service'])
		onlinebackup = st.selectbox(' Customer has onlinebackup:', ['yes', 'no', 'no_internet_service'])
		deviceprotection = st.selectbox(' Customer has deviceprotection:', ['yes', 'no', 'no_internet_service'])
		techsupport = st.selectbox(' Customer has techsupport:', ['yes', 'no', 'no_internet_service'])
		streamingtv = st.selectbox(' Customer has streamingtv:', ['yes', 'no', 'no_internet_service'])
		streamingmovies = st.selectbox(' Customer has streamingmovies:', ['yes', 'no', 'no_internet_service'])
		contract= st.selectbox(' Customer has a contract:', ['month-to-month', 'one_year', 'two_year'])
		paperlessbilling = st.selectbox(' Customer has a paperlessbilling:', ['yes', 'no'])
		paymentmethod= st.selectbox('Payment Option:', ['bank_transfer_(automatic)', 'credit_card_(automatic)', 'electronic_check' ,'mailed_check'])
		tenure = st.number_input('Number of months the customer has been with the current telco provider :', min_value=0, max_value=240, value=0)
		monthlycharges= st.number_input('Monthly charges :', min_value=0, max_value=240, value=0)
		totalcharges = tenure*monthlycharges
		output= ""

    # code for Prediction
     Result = ''
    
    # creating a button for Prediction
    
    if st.button('predict'):
        Result= Fall_prediction(TIME,SL,EEG,BP,HR,CIRCLUATION)
    st.success('The output is {}'.format(Result))
    if st.button("About"):
       st.text('Lets LEarn')
       st.text("Built with Streamilt")


if __name__ == '__main__':
    main()