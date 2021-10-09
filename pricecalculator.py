import streamlit as st
import requests

st.subheader("NFT Worth Calculator for Non-Fungible Anime Girls")
st.write("---")
nfag = ["Anime Girl #"+str(i).zfill(4) for i in range(10000)]

selected = st.selectbox("Choose Your Non-Fungible Anime Girl", nfag)

selectedNo = int(selected.split("#")[1])+1

formula = selectedNo**(0.5) / 100

st.write("---")
st.write("Minimum price of choosed NFT is","**"+str(formula)+"**" , "**ETH**")
