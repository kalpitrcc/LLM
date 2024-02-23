import streamlit as st
from langchain.prompts import * # Adjust the import path accordingly
from langchain.llms import CTransformers
from langchain.prompts import promptsTemplate

# Function to get response from LLAMA 2 model
def getLLamaresponse(input_text, no_words, blog_style):

    # Calling the llama model
    llm = CTransformers(model="C:\\Users\\malviyak\\Documents\\kalpit\\python\\LLM\\llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})

# Add the necessary imports at the beginning of your script:
# from llm import CTransformers

                
    # Prompt Template
    template="""
        Write a blog for {blog_style} Job Profile for a topic {input_text}
        within {no_words} words.
    """
    prompt=promptTemplate(input_variables=['blog_style','input_text','no_words'],
    tempalte=template)

    ## Generate the response from the llama 2 model
    llm(prompt.format(style=blog_style,text=input_text,no_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')


st.header("Generate blogs 🤖")

input_text=st.text_input('Enter the blog topic')

#Creating 2 more cols for additional 2 fields
col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of words')
with col2:
    blog_style=st.selectbox('Write the blog for',( "Reseachers","Data Scientists",'Common People')
            ,index=0)

submit=st.button("Generate")
 
## Final Response
if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))
