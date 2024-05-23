import streamlit as st
from langchain_community.llms import Ollama
import os
import datetime
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time
formatted_date_time = now.strftime("%Y-%m-%d-%I:%M:%S-%p")

# Set Streamlit page config
st.set_page_config(page_title="Ollama", page_icon=":llama:")

# Function to read HTML file
def load_html_file(path):
    with open(path, 'r') as file:
        return file.read()

# Load and display the HTML
html_content = load_html_file('style.html')
with st.container():
    st.markdown(html_content, unsafe_allow_html=True)

######################################################

st.write("---")
st.write("Language Model Selection and Input Handler")
# change and add your installed models.
models = ['tinyllama', 'phi3', 'codegemma:2b', 'gemma:2b', 'qwen:0.5b', 'deepseek-coder:latest']
selected_model = st.selectbox('Choose a model:', models)
llm = Ollama(model=selected_model)

st.write("---")
user_input = st.text_area("Enter your input here", height=150)  # Making the input box expandable
if st.button("Submit"):
    try:
        result = llm.invoke(user_input)
        st.write("---")
        st.write("## Output:")
        st.write(result)
        st.write("---")
        # Save the output in markdown format
        filename = "outputs/{formatted_date_time}_{selected_model}_output.md"
        counter = 1
        while os.path.isfile(filename):  # Checking if file exists
            counter += 1
            filename = f"outputs/{formatted_date_time}_{selected_model}_output_{counter}.md"  # Incrementing the file name if exists
        with open(filename, "w") as file:
            file.write(f"# Model: {selected_model}\n---\n## Input\n\n{user_input}\n\n## Output\n\n{result}")
        st.success(f"Output saved in {filename}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.write("---")
st.write("Everything Ai says is made up!")
st.write("---")
st.write("anlaki©")