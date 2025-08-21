# LLM Blog Generator

This Streamlit application generates blogs using the LLAMA 2 language model. Users can specify the blog topic, desired word count, and target audience style. The app leverages LangChain and CTransformers to interface with the LLAMA 2 model and produce contextually relevant blog posts.

## Features

- **User-Friendly Web Interface**: Powered by Streamlit, allowing easy input of blog requirements.
- **Model-Based Text Generation**: Uses LLAMA 2 via CTransformers for high-quality blog content.
- **Customizable Output**: Choose topic, word count, and audience style (Researchers, Data Scientists, or Common People).

## How It Works

1. **Input Fields**:
    - **Blog Topic**: Enter the subject of your blog.
    - **Number of Words**: Specify the desired length.
    - **Blog Style**: Select the target audience.

2. **Blog Generation**:
    - The app constructs a prompt based on user input.
    - It calls the LLAMA 2 model via LangChain’s CTransformers integration.
    - The generated blog is displayed on the page.

![image](https://github.com/kalpitrcc/LLM/assets/109504750/c0663daa-8896-4b68-a08d-99b72e62467e)

## Requirements

- Python 3.7+
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [CTransformers](https://github.com/marella/ctransformers)
- LLAMA 2 model file (`.bin`), path must be set in the code.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/kalpitrcc/LLM.git
    cd LLM
    ```

2. **Install Dependencies**
    ```bash
    pip install streamlit langchain ctransformers
    ```

3. **Download LLAMA 2 Model**
    - Place the model file in the appropriate directory and update the path in `app.py`:
      ```
      llm = CTransformers(model="path/to/llama-2-7b-chat.ggmlv3.q8_0.bin", ...)
      ```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open the provided local URL in your browser to access the blog generator.

## Notes

- The model file path must be correct and accessible.
- Make sure all required packages are installed.
- The code assumes familiarity with LangChain and CTransformers.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [LLAMA 2](https://ai.meta.com/llama/)
- [CTransformers](https://github.com/marella/ctransformers)


