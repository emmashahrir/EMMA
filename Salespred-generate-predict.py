import streamlit as st
import pandas as pd
import seaborn as sns
import pickle

st.write("# Sales Price Prediction App")
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

loaded_modelSvr = pickle.load(open("Salespred.h5", "rb")) #rb: read binary
pred = loaded_modelSvr.predict(df)

st.subheader('Sales Price Prediction')
st.write(pred)
