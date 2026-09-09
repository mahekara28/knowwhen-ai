import streamlit as st
from datetime import datetime
from ai_engine import get_recommendation
from history import save_history

st.set_page_config(
    page_title="KnowWhen AI",
    page_icon="✦",
    layout="centered"
)

# ---------- CUSTOM CSS ----------

st.markdown("""
<style>
.stApp {
    background: #0B0D12;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    max-width: 760px;
    padding-top: 3rem;
}

/* Hero */
.hero {
    text-align: center;
    margin-bottom: 35px;
}

.logo {
    width: 60px;
    height: 60px;
    margin: 0 auto 18px auto;
    border-radius: 18px;
    background: linear-gradient(135deg, #7C3AED, #4F46E5);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 28px;
    font-weight: bold;
}

.hero-title {
    color: #F8FAFC;
    font-size: 44px;
    font-weight: 700;
    margin-bottom: 8px;
}

.hero-subtitle {
    color: #94A3B8;
    font-size: 16px;
    line-height: 1.6;
}

/* Input labels */
.stTextInput label {
    color: #CBD5E1 !important;
    font-weight: 600 !important;
}

/* Inputs */
.stTextInput input {
    background-color: #11151D !important;
    color: #F8FAFC !important;
    border: 1px solid #2A3040 !important;
    border-radius: 12px !important;
    padding: 12px !important;
}

.stTextInput input:focus {
    border-color: #7C3AED !important;
}

/* Button */
.stButton button {
    width: 100%;
    height: 50px;
    border: none;
    border-radius: 12px;
    background: linear-gradient(135deg, #7C3AED, #4F46E5);
    color: white;
    font-size: 16px;
    font-weight: 600;
}

.stButton button:hover {
    border: none;
    color: white;
}

/* Result */
.result {
    background: #12151C;
    border: 1px solid #2A3040;
    border-radius: 18px;
    padding: 25px;
    margin-top: 30px;
}

.result-heading {
    color: #F8FAFC;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 15px;
}

.footer-text {
    text-align: center;
    color: #64748B;
    font-size: 13px;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)


# ---------- HERO ----------

st.markdown("""
<div class="hero">
    <div class="logo">✦</div>
    <div class="hero-title">KnowWhen AI</div>
    <div class="hero-subtitle">
        Find the right time to do what matters.<br>
        Personalized around your schedule and goals.
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- INPUTS ----------

activity = st.text_input(
    "What do you want to do?",
    placeholder="e.g. Study Python"
)

available_time = st.text_input(
    "When are you available?",
    placeholder="e.g. 6 PM to 10 PM"
)

goal = st.text_input(
    "What are you trying to achieve?",
    placeholder="e.g. Build my AI project"
)


# ---------- BUTTON ----------

if st.button("✦  Get my best time"):

    if not activity or not available_time or not goal:

        st.warning(
            "Please fill in all three fields."
        )

    else:

        with st.spinner("Finding your best time..."):

            current_time = datetime.now().strftime(
                "%A, %d %B %Y, %I:%M %p"
            )

            recommendation = get_recommendation(
                activity,
                available_time,
                goal,
                current_time
            )

            save_history(
                activity,
                recommendation
            )

        st.markdown("""
        <div class="result">
            <div class="result-heading">
                ✦ Your personalized recommendation
            </div>
        """, unsafe_allow_html=True)

        st.markdown(recommendation)

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# ---------- FOOTER ----------

st.markdown("""
<div class="footer-text">
    Powered locally by Ollama · Python · Streamlit
</div>
""", unsafe_allow_html=True)