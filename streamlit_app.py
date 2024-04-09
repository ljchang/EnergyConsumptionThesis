#Import packages
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
#load participant usernames
participant_progress=pd.read_csv('Partcipant Tracking Spreadsheet - Eligible Subs Progress Survey Comp.csv')
df_partic_prog= pd.DataFrame(participant_progress, columns=['Eligible Participant', 'Assigned Username'])
usernames=df_partic_prog['Assigned Username']
#st.write(usernames)
st.title('Energy Consumption Leaderboard')

#load energy consumption data
energy_consdata=pd.read_csv('Partcipant Tracking Spreadsheet - Example Energy Data.csv')
df_energy_data=pd.DataFrame(energy_consdata, columns=['username', 'new energy cons', 'old energy cons', 'energy change'])

#Participants must enter username and email to login
#pip install streamlit-authenticator
import streamlit_authenticator as stauth
#create YAML file 
credentials:
  preauthorized:
    usernames: 
    -usernames.tolist()
#need to create a list of the preauthorizes usernames and corresponding emails
#my yaml isnt working so need to fix this 
import yaml 
from yaml.loader impirt SafeLoader 
with open ('../config.yaml') as file
  config = yaml.load(file, Loader-SafeLoader)
authenticator= Authenticate( 
  config['credentials'],
  config['preauthroized']
)
#authentication pop up
name, authentucation_status, username= authenticator.login('Login', 'main')

#read authentication and forgotten username feauture 

#create buttons for seeing experimental groups (1. your energy cons vs others in the same condition, your house community energy cons, energy cons for your class year)
#need a better way to store energy data in the sheets
#build ranked leaderboard
