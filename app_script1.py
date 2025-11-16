import streamlit as st
import random
import time

st.set_page_config(page_title="Welcome!", page_icon="😄", layout="centered")

time = time.time()

status_placeholder = st.empty()

st.title("Welcome! 😄")
st.markdown("Let's have a friendly chat together!✨")

questions = [
    "How are you feeling today? 😄",
    "What's something that made you smile recently? 😊",
    "What are you grateful for right now? 🙏",
    "What's a fun fact about yourself? 🤔",
    "If you could travel anywhere in the world, where would you go? ✈️",
    "What is your favorite hobby or pastime? 🎨",
    "What's a goal you're working towards? 🎯",
    "Whats your favorite way to relax? 🛀",
    "What is your favourite food? 🍕",
    "Who is someone that inspires you? 🌟",
    "What is your favourite movie or TV show? 🎬",
    "What's a book that you love? 📚",
    "What is your dream job? 💼",
    "If you could have dinner with any historical figure, who would it be? 🍽️",
    "What is your favourite sport or physical activity? ⚽",
    "What's a skill you'd like to learn? 🎸",
    "What is your favourte game? 🎮",
    "If you could have any superpower, what would it be? 🦸‍♂️"
]


name = st.text_input("What's your name?")

if name:
    st.success(f"Great to meet you, **{name}**! Ready for a chat? :smile:")
    st.write("Press the button below!")
    if st.button("Start Chatting!"):
        question = random.choice(questions)
        status_placeholder.write("🤖 *Thinking...*")
        time.sleep(1)
        status_placeholder.empty()
        st.markdown(f"**Question:** {question}")
        answer = st.text_area("Your Answer:", height=100)
        if st.button("Submit Answer"):
            status_placeholder.write("🤖 *Thinking...*")
            time.sleep(1)
            status_placeholder.empty()
            st.success("Thanks for sharing! That was interesting. 😊")

    st.markdown("---")

    st.subheader("⚡ Charge your Energy Meter")

    if st.button("Start charging!"):
        progress = st.progress(0)
        for i in range(60):
            time.sleep(0.02)
            progress.progress(i + 1)
        time.sleep(0.3)
        for i in range(60, 90):
            time.sleep(0.05)
            progress.progress(i + 1)
        time.sleep(0.5)
        for i in range(90, 100):
            time.sleep(0.1)
            progress.progress(i + 1)

        st.success("Energy fully charged! 🎉")
        time.sleep(1)
        st.balloons()
        st.badge("Energized!")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit, f"                                              {time}")

# run with: streamlit run c:/Rishi_Python/HelloWorld.py
