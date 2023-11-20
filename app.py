import streamlit as st
import pandas as pd

@st.cache_data
def load_data():    
    df = pd.read_csv('data.csv', sep='|')
    
    return df

st.title('Licitor Dashboard')
data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache_data)")

ads_number = data.ad_number.nunique()

st.write(ads_number)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
