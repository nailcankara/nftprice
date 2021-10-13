import streamlit as st
import seaborn as sns
import pandas as pd

st.subheader("NFT Worth Calculator for Non-Fungible Anime Girls")
st.write("---")
nfag = ["Anime Girl #"+str(i).zfill(4) for i in range(10000)]

fp = st.number_input('Enter the floor price ETH',value=0.001,min_value=0.001,step=0.001,max_value=0.999,format="%f")
selected = st.selectbox("Choose Your Non-Fungible Anime Girl", nfag)

selectedNo = int(selected.split("#")[1])+1

  
coef = 100-fp*100

formula = selectedNo**(0.5) / coef
formula = round(formula,6)

st.write("---")
st.write("Minimum price of choosed NFT is","**"+str(formula)+"**" , "**ETH**")

allP = pd.DataFrame([(i**0.5)/(100-fp*100) for i in range(1,10001)],columns=["Prices"])
sns.lineplot(allP,x=allP.index,y=allP.Prices)
st.pyplot()
