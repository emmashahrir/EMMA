import streamlit as st
import pandas as pd
import seaborn as sns

st.write("# Sales Price Prediction Emma App")
st.write("This app predicts the **Sales Price** type!")

st.sidebar.header('User Input Parameters')

def user_input_features():
    #('X', min, max, default)
    TV = st.sidebar.slider('TV', 1, 300, 100)
    Radio = st.sidebar.slider('Radio', 0, 50, 25)
    Newspaper = st.sidebar.slider('Newspaper', 0, 114, 70)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)

loaded_modelSvr = pickle.load(open("Salespred.h5", "rb")) #rb: read binary
TV=loaded_modelSvr.predict(df)
st.write(prediction_proba)
