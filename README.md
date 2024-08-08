# Streamlit Basics Project

## Required installations

1. `pip3 install streamlit`  
   *Installs the Streamlit library, a tool for creating interactive web applications from Python scripts.*

2. `pip3 install pandas matplotlib`  
   *Installs Pandas for data manipulation and analysis, and Matplotlib for creating visualizations.*


Run this code to open a start template of Streamlit: 

```commandline
streamlit hello
```
This command will open a browser with the following (maybe a bit different) content:

![image](https://github.com/user-attachments/assets/dff5cbc8-1438-404c-8ce7-b189bb232114)


Open a new file named `main.py` inside the root directory. 
Import the Streamlit library with the following code:

```python
import streamlit as st
```
   
Create a first streamlit program:

```python
st.write("Hello World!")
```

Then we can run our first program with the following command

```commandline
streamlit run main.py
```


