# Text_summarization
Overview
This project is a lightweight AI-powered text summarizer that takes any news article or blog post and produces a concise 3-sentence summary using a pre-trained transformer model via the Hugging Face Transformers pipeline with an optional Streamlit UI exposed from Google Colab using ngrok.
The core relies on the facebook/bart-large-cnn checkpoint for abstractive summarization, accessed through a high-level pipeline that abstracts tokenization, model loading, generation, and postprocessing for inference-only usage.

Features
Abstractive text summarization with a proven BART Large checkpoint fine-tuned on CNN/DailyMail for general-purpose summarization.

One-file Streamlit UI with a text area and a summarize button for interactive use without front-end code.

Google Colab-friendly run path with ngrok tunneling to publish a temporary public URL for the Streamlit app.

Deterministic summaries via do_sample=False and length guidance via max_length and min_length for approximate 3-sentence outputs.

Tech stack
Hugging Face Transformers pipeline for summarization (model and tokenizer orchestration).

facebook/bart-large-cnn for high-quality, general-purpose abstractive summarization.

Streamlit for building a minimal, reactive Python UI with caching for fast reruns.

pyngrok/ngrok to expose the local Streamlit server from Colab to a public HTTPS URL.

Architecture and flow
Input text is collected through a Streamlit text area and passed to a cached summarization pipeline instance built on facebook/bart-large-cnn.

The Transformers pipeline handles tokenization, encoder-decoder inference, and decoding to a human-readable summary string in a single call.

The Streamlit app runs in the Colab runtime on port 8501, and pyngrok opens an authenticated HTTP tunnel so the UI is reachable via a temporary public URL.

Quick start (Colab)
Install dependencies in a Colab cell: transformers, streamlit, and pyngrok for tunneling.

Save the Streamlit app file (summarizer_app.py) in the working directory and run Streamlit headlessly on port 8501, then create an ngrok tunnel to that port.

Open the printed public URL to access the app and summarize any article in a few seconds after model warm-up.
