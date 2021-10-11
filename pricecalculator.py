import streamlit as st

st.subheader("NFT Worth Calculator for Non-Fungible Anime Girls")
st.write("---")
nfag = ["Anime Girl #"+str(i).zfill(4) for i in range(10000)]

fp = st.number_input('Enter the floor price ETH',value=0.001,min_value=0,step=0.001)
selected = st.selectbox("Choose Your Non-Fungible Anime Girl", nfag)

selectedNo = int(selected.split("#")[1])+1


if fp >= 0.99:
  fp = 0.99
  
coef = 100-fp*100

formula = selectedNo**(0.5) / coef
formula = round(formula,6)

st.write("---")
st.write("Minimum price of choosed NFT is","**"+str(formula)+"**" , "**ETH**")
