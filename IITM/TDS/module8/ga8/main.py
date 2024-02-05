import numpy as np
import pandas as pd
import streamlit as st

def welcome():
    return "Hello world"

def main():
  st.title("Multiplication app")
  html_temp = """
  <div style="background-color:tomato;padding:10px">
  <h2 style="color:white;text-align:center;">Multiplication of 2 numbers using Streamlit</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num1 = st.number_input("Number 1")
  num2 = st.number_input("Number 2")
  result = num1 * num2
  st.success('The output is {}'.format(result))
  if st.button("Made By"):
      st.text("Manish Kumar")
      st.text("21f1006597")

if __name__=='__main__':
  main()
