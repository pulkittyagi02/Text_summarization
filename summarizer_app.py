import streamlit as st
from transformers import pipeline

# Page Title
st.title('📰 AI Text Summarizer (3-Sentence)')

# Info
st.write('Paste any news article or blog post below and click **Summarize**.')

# Text input
input_text = st.text_area('Input text:', height=300)

# Summarization logic (runs when button pressed)
if st.button('Summarize'):
    if not input_text.strip():
        st.warning('Please paste some text to summarize!')
    else:
        # Load the model only once per session (caches for speed)
        @st.cache_resource
        def load_summarizer():
            return pipeline('summarization', model='facebook/bart-large-cnn')
        summarizer = load_summarizer()
        # Call the model
        summary = summarizer(
            input_text,
            max_length=130,   # total tokens for 3-4 sentences
            min_length=30,
            do_sample=False
        )[0]['summary_text']
        st.subheader('Summary:')
        st.success(summary)
