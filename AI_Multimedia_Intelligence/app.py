import streamlit as st
from models.cnn_image_classifier import run_cnn
from models.lstm_sentiment import run_lstm
from models.bert_emotion import run_bert
from models.audio_autoencoder import run_audio_autoencoder
from models.video_anomaly_detection import run_video_sim

st.title("🎯 AI Multimedia Intelligence System")

option = st.selectbox(
    "Choose input type",
    ["Image Classification", "Text Sentiment", "Emotion Detection", "Audio Anomaly", "Video Anomaly"]
)

if option == "Image Classification":
    if st.button("Run CNN"):
        result = run_cnn("data/test_image.jpg")
        st.success(result)

elif option == "Text Sentiment":
    if st.button("Run LSTM"):
        result = run_lstm("data/test_text.txt")
        st.success(result)

elif option == "Emotion Detection":
    if st.button("Run BERT"):
        result = run_bert("data/test_text.txt")
        st.success(result)

elif option == "Audio Anomaly":
    if st.button("Run Autoencoder"):
        result = run_audio_autoencoder("data/test_audio.wav")
        st.success(result)

elif option == "Video Anomaly":
    if st.button("Run DQN Simulation"):
        result = run_video_sim("data/test_video_sim.txt")
        st.success(result)


## .venv\Scripts\activate

##cd "c:\Users\Shaik Afreen\OneDrive\Documents\ML Algorithms\AI_Multimedia_Intelligence"

## streamlit run app.py
