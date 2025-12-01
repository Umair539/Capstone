import streamlit as st
import pandas as pd


def main():
    
    solar = pd.read_csv('data/transformed/solar.csv')
    solar.set_index('time_tag', inplace=True)
    solar_agg = pd.read_csv('data/transformed/solar_agg.csv')
    solar_agg.set_index('time_tag', inplace=True)

    feature = st.selectbox(
        label = 'Select feature',
        options = solar.columns[:],
        index = 0
    )
    
    st.dataframe(
        solar[[str(feature)]]
    )


if __name__ == "__main__":
    main()