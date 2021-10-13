import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showPyplotGlobalUse', False)

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
st.write("---")

fig, ax = plt.figure(figsize=(15,5))

allP = pd.DataFrame([(i**0.5)/(100-fp*100) for i in range(1,10001)],columns=["Prices"])
fig = sns.lineplot(x=allP.index,y=allP.Prices.values)
st.pyplot(fig)
