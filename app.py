import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title("My First Streamlit App")
st.write(":100: Hello Nishikant")
st.text("Lets start")

name=st.text_input("Enter Name:")
if st.button("Greet"):
    st.success(f"Hello, {name}")
    
    
# creating charts using pandas and Numpy
df=pd.DataFrame(np.random.randn(10,2),columns=['A','B'])


st.line_chart(df)
st.bar_chart(df)

# sideBar, Image & video
st.sidebar.title("Navigation")
st.image(r"C:\Users\ADMIN\Downloads\yash.jpg",caption="Releasing Soon")
st.video("https://youtu.be/cXymbHU5i-U?si=HG4iOqV1XGYhe2lQ")

#upload csv file
upload_csv=st.file_uploader("upload a csv file", type="csv")

if upload_csv:
    df=pd.read_csv(upload_csv)
    st.dataframe(df)
    
    # Text & Markdown Formating 
    st.header("This is a Header")
    st.subheader("this is a subheader")
    
    st.markdown("**Bold**, *Itlatic*, 'code' [Link](http://streamlit.io)")
    st.code("for i in range(s): print(i)", language="python")

# input components in streamlit
st.text_input("what's your name?")
st.text_area("write something....")
st.number_input("pick a number",min_value=0,max_value=100)
st.slider("choose a range",0,100)
st.selectbox("select a fruit",["apple","banna","mango"])
st.multiselect("choose toppings",["cheese","tomato","olives"])
st.radio("pick one",["option A","option B"])
st.checkbox("I agree to the items.")

#matplotlib Integration
fig, ax=plt.subplots()
ax.plot([1,2,3],[1,4,9])
st.pyplot(fig)
