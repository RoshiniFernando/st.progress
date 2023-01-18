import streamlit as st
import time

st.title('st.progress')

with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

# Creating a progress bar with a starting value of 0
my_bar = st.progress(0)

# Iterate 0 to 100
for percent_complete in range(100):
     time.sleep(0.05) # For each loop app waiting time to add 1 to complete bar progress
     my_bar.progress(percent_complete + 1)

# Setting ballons
st.balloons()
