import streamlit as st 
import pandas as pd


st.header('Pengembangan Dashboard')
st.title('Belajar Analisis Data') 
st.write(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

st.text('Halo, calon praktisi data masa depan.')

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
 
st.dataframe(data=df, width=500, height=150)


df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)

text = st.text_area('Feedback')
st.write('Feedback: ', text)