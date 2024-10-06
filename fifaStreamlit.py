import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv('/workspaces/Streamlit-Task/fifa_eda.csv')
df=load_data()

st.header("Explore the Fifa Data 2018")
# st.sidebar.header('Fifa Players and Clubs')
st.sidebar.markdown("<h1 style='color: Red;'>Fifa Players and Clubs</h1>", unsafe_allow_html=True)
st.sidebar.image('fifa.png')
c1=st.sidebar.selectbox("select club: ",df['Club'].unique())
c2=st.sidebar.selectbox("select Player: ",df['Name'].unique())

cc1 , cc2 = st.columns(2)
cc1.metric('Avg Ages',df[df['Club']== c1]['Age'].mean().round(0))
cc2.metric('Avg Values',df[df['Club']== c1]['Value'].mean().round(0))


tab1,tab2,tab3,tab4,tab5=st.tabs(['Ages','Values','Preferred Foot','Nationality','Position'])

tab1.plotly_chart(px.bar(df[df['Club']==c1],x='Name',y='Age',color='Age',title='Ages of players in the team'))
tab2.plotly_chart(px.bar(df[df['Club']==c1],x='Name',y='Value',color='Value',title='Values of players in the team'))
tab3.plotly_chart(px.bar(df[df['Club']==c1],x='Preferred Foot',color='Preferred Foot',title='Foot Preference by Club'))
tab4.plotly_chart(px.bar(df[df['Club']==c1],x='Nationality',color='Nationality',title='Nationality of players in the team'))
tab5.plotly_chart(px.bar(df[df['Club']==c1],x='Position',color='Position',title='Position of players in the team'))
df2=df2=df.drop(columns=['ID'])
st.subheader(f"Info about {c2}")
# st.write(df2[df2['Club']==c1],)
st.write(df2[df2['Name']==c2])

st.markdown("<h3 style='color: blue;'>Top 10 Highest Valued Players</h3>", unsafe_allow_html=True)
top_players = df[['Name', 'Value']].sort_values(by='Value', ascending=False).head(10)
st.plotly_chart(px.bar(top_players, x='Name', y='Value'))

st.markdown("<h3 style='color: red;'>Where Most Players Come From</h3>", unsafe_allow_html=True)
nationality_counts = df['Nationality'].value_counts().reset_index()
nationality_counts.columns = ['Nationality', 'Player_Count']
st.plotly_chart(px.choropleth(nationality_counts,locations='Nationality',locationmode='country names',color='Player_Count',color_continuous_scale='Reds'))


