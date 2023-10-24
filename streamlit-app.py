#!/usr/bin/env python
# coding: utf-8

# import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np

# Add CSS for the background image
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://a.espncdn.com/photo/2020/0331/r684654_1296x864_3-2.jpg");
background-size: 100%;
background-position: center;
background-repeat: no-repeat;
background-attachment: local;
background-size: cover;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


st.title("The ValuSoccer Visionary")
st.markdown('''
####  <span style="color:white"> Market value of Soccer players </span> 
''', unsafe_allow_html=True)
st.write('---')
data = pd.read_csv('Final dataset with predictions.csv')


datanice = data.copy()
datanice = datanice.set_index('names', drop=False)
datanice = datanice[["Team names","Age","Overall rating","Height","Weight","Agility","Ball control","Shot power",
                     "Long shots","new_release_clause_series","Orignial Market Value","Predicted Market Value"]]

team_names = data["Team names"].unique()

st.sidebar.markdown(" # Select Your Team & Player")
image_url = "https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt98be642dcfd8ccce/62ff3c3d51bdff32151ccf9a/Messi.jpg?auto=webp&format=pjpg&width=1200&quality=60"  # Replace with the URL of your image


st.sidebar.image(image_url)
team = st.sidebar.selectbox("Team :",
                                   sorted(team_names))


player = st.sidebar.selectbox("Player :",
                                     (data[data['Team names'] == team].names.unique()))

release_clause = round(datanice.loc[player]["new_release_clause_series"]/1000000,3)
market_value = round(datanice.loc[player]["Orignial Market Value"]/1000000,3)
pred_market_value = round(datanice.loc[player]["Predicted Market Value"]/1000000,3)
st.write(f'''
         ##### <span style="color:orange">{player}</span>, this year has a release clause of <span style="color:orange"> ${release_clause}M </span>
            ##### His Original market value is <span style="color:orange">${market_value}M</span>
            ##### The predicted market value by the model is <span style="color:orange">${pred_market_value}M</span>
         ''', unsafe_allow_html=True)

st.write('---')
st.write(f'''
         
         #### {team}:
         ''')



my_data = datanice[datanice['Team names'] == team]

st.dataframe(my_data)

