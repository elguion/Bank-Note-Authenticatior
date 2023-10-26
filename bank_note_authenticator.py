# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 01:39:19 2023

@author: Gregory Bazuaye
"""

import numpy as np
import pandas as pd
import flask as Flask
import pickle
import streamlit as st


pickle_in = open('classifier.pkl' , 'rb')
classifier = pickle.load(pickle_in)


def predict_note_authenticity(variance , skewness , curtosis , entropy) :
     prediction = classifier.predict([[variance , skewness , curtosis , entropy]])
     if (prediction == 0):
        return 'The note is not authentic'
     else :
        return 'The note is authentic'
    
    
def main():
    st.header('A Bank Note Authenticator')
    html_temp = """
    <div style="background-color: tomato; padding: 10px;">
    <h2 style="text-align: center; color: white;">Bank Authenticator</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = (st.text_input('variance', ''))
    skewness = (st.text_input('skewness', ''))
    curtosis = (st.text_input('curtosis', ''))
    entropy = (st.text_input('entropy', ''))
    prediction = ''  # Initialize prediction variable
    
    if st.button ('Predict') :
      if is_valid(variance) and is_valid(skewness) and is_valid(curtosis) and is_valid(entropy):
        variance = float (variance)
        skewness = float(skewness)
        curtosis = float(curtosis)
        entropy = float(entropy)
      
        prediction= predict_note_authenticity(variance , skewness , curtosis , entropy)
    
        st.success(f'The prediction is {prediction}')
      else :
          return 'Please enter values for all input fields'
    
    if st.button('About'):
        st.text("Let's learn")
        st.text('Built with Streamlit')
    
    
def is_valid(value):
    try :
        float(value)
        return True
    except ValueError:
        return False
if __name__ == '__main__':
    main()
    
    
    