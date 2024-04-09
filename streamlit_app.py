pip install streamlit
#Import packages
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
#load participant usernames
participant_progress=pd.read_csv('/content/Partcipant Tracking Spreadsheet - Eligible Subs Progress Survey Comp.csv')
df_partic_prog= pd.DataFrame(participant_progress, columns=['Eligible Participant', 'Assigned Username'])
usernames=df_partic_prog['Assigned Username']


