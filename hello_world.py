import streamlit as st

# Define the options for the dropdown
options = ['Frat Bro', 'Rude Guy', 'Knowledgeable Scientists', 'Cowboy']

# Create the dropdown and get the user's selection
selected_option = st.selectbox('Select a Budtender Persona:', options)

# Read the contents of the file
with open('virtual-budtender/combined.csv', 'r') as f:
    file_contents = f.read()

# Define the string to concatenate with the file contents
message = f"You're a budtender, you will not give the price until being asked for, you will answer like a {selected_option}, and all prices are in Baht. Here are the data in csv format: "

# Concatenate the message with the file contents
result = message + file_contents

# Display the result on the screen
st.write(result)
