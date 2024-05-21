
# Ollama: Streamlit Language Model Selector

Welcome to Ollama, a Streamlit-based application that allows you to interact with various language models. This app provides a user-friendly interface to select a model, input text, and receive generated responses.

## Features

- **Model Selection**: Choose from a list of pre-configured models.
- **Input Handling**: Enter your text input and receive responses generated by the selected model.
- **Output Management**: Generated responses are displayed in the app and saved as Markdown files for further use.
- **Custom Styling**: The app includes custom HTML styling for enhanced UI/UX.

## Usage

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/anlaki-py/ollama-on-streamlit.git
    cd ollama-on-streamlit
    ```

2. **Install Dependencies**:
    Ensure you have Ollama and Python installed on your system. Install the required packages using:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    Start the Streamlit server by running:
    ```sh
    streamlit run ollama.py
    ```

4. **Interact with the App**:
    - Open your web browser and navigate to the displayed URL (usually `http://localhost:8501`).
    - Choose a language model from the dropdown menu.
    - Enter your text input in the provided text area.
    - Click the "Submit" button to generate a response.
    - View the generated response and check the `outputs` directory for saved Markdown files.

## File Structure

- `ollama.py`: The main application script.
- `style.html`: Custom HTML file for styling the Streamlit app.
- `outputs/`: Directory where generated responses are saved as Markdown files.
- `requirements.txt`: List of dependencies for the project.