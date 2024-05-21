import streamlit as st
from langchain_community.llms import Ollama
import os

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
models = ['tinyllama', 'phi3', 'codegemma:2b', 'gemma:2b', 'qwen:0.5b', 'deepseek-coder:latest']
selected_model = st.selectbox('Choose a model:', models)
llm = Ollama(model=selected_model)

st.write("---")
user_input = st.text_area("Enter your input here", height=150)  # Making the input box expandable
if st.button("Submit"):
    try:
        result = llm.invoke(user_input)
        # Display the result in real time (Streamlit inherently updates in real-time)
        st.write("---")
        st.write("## Output:")
        st.write(result)
        st.write("---")
        # Save the answer in markdown format
        filename = "outputs/output.md"
        counter = 1
        while os.path.isfile(filename):  # Checking if file exists
            counter += 1
            filename = f"outputs/output{counter}.md"  # Incrementing the file name if exists
        with open(filename, "w") as file:
            file.write(result)
        st.success(f"Answer saved in {filename}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.write("---")
st.write("Everything Ai says is made up!")