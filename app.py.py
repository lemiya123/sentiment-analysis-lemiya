import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Initialize session state
if 'review_list' not in st.session_state:
    st.session_state.review_list = []
if 'sentiment_list' not in st.session_state:
    st.session_state.sentiment_list = []

# Custom background and styling
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
    }
    .reportview-container {
        background: linear-gradient(to right, #fdfbfb, #ebedee);
        padding: 20px;
    }
    .title {
        font-size: 36px;
        text-align: center;
        color: #4B8BBE;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: gray;
        font-size: 18px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<div class='title'>🛍️ Sentiment Analysis of Product Reviews</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>By Lemiya Suhail | AWH Engineering College Kuttikattoor</div>", unsafe_allow_html=True)
st.write("---")

# Sentiment function
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

# Input Section
st.markdown("### ✍️ Enter your product review:")
user_input = st.text_area(" ", height=150, placeholder="Type your review here...")

if st.button("🔍 Analyze Sentiment"):
    sentiment = get_sentiment(user_input)
    st.success(f"🧠 Sentiment: **{sentiment}**")
    st.session_state.review_list.append(user_input)
    st.session_state.sentiment_list.append(sentiment)

# Bar Chart
st.write("---")
st.markdown("### 📊 Sentiment Distribution")
if st.button("📈 Show Sentiment Summary"):
    sentiment_df = pd.DataFrame(st.session_state.sentiment_list, columns=["Sentiment"])
    count = sentiment_df["Sentiment"].value_counts()
    st.bar_chart(count)

# Word Cloud
st.write("---")
st.markdown("### ☁️ Word Cloud of Entered Reviews")
if st.button("☁️ Generate Word Cloud"):
    text = " ".join(st.session_state.review_list)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

# Footer
st.write("---")
st.markdown("<p style='text-align: center; color: grey;'>✨ Made with ❤️ by Lemiya Suhail</p>", unsafe_allow_html=True)