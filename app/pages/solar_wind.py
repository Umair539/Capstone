import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

st.title("Real Time Solar Wind Properties")

solar = pd.read_csv('data/transformed/solar.csv')
solar.loc[:, 'time_tag'] = pd.to_datetime(solar['time_tag']) 
solar.set_index('time_tag', inplace=True)

solar_agg = pd.read_csv('data/transformed/solar_agg.csv')
solar_agg.loc[:, 'time_tag'] = pd.to_datetime(solar_agg['time_tag']) 
solar_agg.set_index('time_tag', inplace=True)

feature = st.selectbox(
    label = 'Select feature',
    options = solar_agg.columns[:],
    index = 0
)

st.dataframe(
    solar_agg[[str(feature)]]
)

st.line_chart(
    solar_agg[[str(feature)]]
)

#st.slider('slider', solar_agg.index[0], solar_agg.index[-1])

min_epoch = 0.0
max_epoch = solar_agg.index[-1].timestamp() -solar_agg.index[0].timestamp()
st.slider(
    "Select Time (seconds)",
    min_epoch,
    max_epoch,
    step = 1,
    )
# Remember to convert the slider output back to datetime for use