import streamlit as st
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
import openai
import pandas as pd
import random

#st.image("image.png")
st.image("https://github.com/shivek-sachdev/virtual-budtender/blob/master/image.png?raw=true")
tab1, tab2 = st.tabs(["Canbot", "Strain Data"])

openai.api_key = st.secrets["apikey"]

df = pd.read_csv('https://raw.githubusercontent.com/shivek-sachdev/virtual-budtender/master/combined.csv')
table_string = df.to_string(index=False)

with tab1:
    st.title("Meet Canbot from Cantrak!")
    st.subheader("🤖🚬🌿 World's first AI-Budtender")
    #st.subheader("🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿")
    st.write("Canbot's Attitude: a cowboy, a frat bro or a rude d*ck")
    st.write("Note: Refresh the site to meet a new Canbot with a different attitude")
    st.markdown("""---""")
    st.subheader("Try these conversations: ")
    st.caption("I need something to get me creative")
    st.caption("What strains do you have?")
    st.caption("Note: Canbot has been partially trained on Cantrak's data + it will not let you know the price, unless you really ask :)")
#model = st.selectbox(
#    "Select a model",
#    ("gpt-3.5-turbo", "gpt-4")
#)

# Read the contents of the file
    with open('combined.csv', 'r') as f:
        file_contents = f.read()



    options = ['Frat Bro', 'Rude Guy', 'Knowledgeable Scientists', 'Cowboy']
# Create the dropdown and get the user's selection
    selected_option = random.choices(options)
#selected_option = st.selectbox('Select a Budtender Persona:', options)

    initial_persona = f"You're a budtender, you will not give the price until being asked for, you will answer like a {selected_option}, and all prices are in Baht. Here are the data in csv format: "
    initial_persona = initial_persona + file_contents

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []

    query = st.text_input("Ask Canbot (might be a bit slow due to usage) : ", key="input")

    st.markdown("""---""")

    if 'messages' not in st.session_state:
        st.session_state['messages'] = get_initial_message(initial_persona)

    if query:
        with st.spinner("generating..."):
        
            messages = st.session_state['messages']
            messages = update_chat(messages, "user", query)
            response = get_chatgpt_response(messages, "gpt-4")
            messages = update_chat(messages, "assistant", response)
            st.session_state.past.append(query)
            st.session_state.generated.append(response)

    if st.session_state['generated']:

        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i), avatar_style="adventurer", seed=420)

        #with st.expander("Show Messages"):
            #st.write(messages)

with tab2:

    # Read the CSV file
# Display the data as a table
    st.table(df)
   
# Display the string in your Streamlit app
    #st.write(table_string)