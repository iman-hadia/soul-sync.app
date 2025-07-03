# SoulSync: A Mental Health Comfort App with Streamlit

import streamlit as st
import random
from PIL import Image
import os

# Load animal avatars
animal_emojis = {
    "Bunny": "🐰",
    "Puppy": "🐶",
    "Cat": "🐱",
    "Chick": "🐥",
    "Fish": "🐠",
    "Panda": "🐼",
    "Parrot": "🦜",
    "Turtle": "🐢"
}

# Streamlit Page Config
st.set_page_config(
    page_title="SoulSync",
    page_icon="🌺",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Session State
if "animal" not in st.session_state:
    st.session_state.animal = None
if "name" not in st.session_state:
    st.session_state.name = None

# Animal Companion Selection
st.title("SoulSync 🌺")
st.subheader("A gentle space for your feelings")
st.markdown("---")

if not st.session_state.animal:
    st.markdown("### Choose your emotional support animal:")
    selected = st.selectbox("Pick your companion", list(animal_emojis.keys()))
    name = st.text_input("Give your companion a name (e.g., Moony)")

    if st.button("Start With My Companion") and name:
        st.session_state.animal = selected
        st.session_state.name = name
        st.success(f"{animal_emojis[selected]} {name} is now with you.")
        st.experimental_rerun()
else:
    # Welcome Message
    animal = st.session_state.animal
    name = st.session_state.name
    emoji = animal_emojis[animal]
    st.markdown(f"### Hi, I'm {name} {emoji}. I'm right here with you.")
    st.caption("Want to talk? Share your feelings below.")

    # Mood Check-In
    mood = st.selectbox("How are you feeling today?", ["", "🙂 Happy", "😞 Sad", "😕 Anxious", "😶 Numb"])
    if mood:
        if "Happy" in mood:
            st.success(f"{name} {emoji} says: 'That's amazing! Keep soaking in the sunshine!' ☀️")
        elif "Sad" in mood:
            st.info(f"{name} {emoji} says: 'It’s okay to feel sad. I’m here with you.'")
        elif "Anxious" in mood:
            st.warning(f"{name} {emoji} says: 'Deep breaths, bestie. You’re not alone in this.'")
        elif "Numb" in mood:
            st.info(f"{name} {emoji} says: 'Even feeling nothing is still a feeling. Let’s sit together in this.'")

    # Chatbot
    st.markdown("---")
    st.markdown(f"#### Talk to {name} {emoji}:")
    user_input = st.text_input("What's on your mind?")
    if user_input:
        responses = [
            f"{name} {emoji} says: That sounds tough. Want to tell me more?",
            f"{name} {emoji} says: I’m proud of you for even sharing this.",
            f"{name} {emoji} says: You're doing better than you think.",
            f"{name} {emoji} says: Totally valid. I’m here for you."
        ]
        st.write(random.choice(responses))

    # Hug/Kiss Buttons
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🫂 Send Virtual Hug"):
            st.markdown(f"### {name} {emoji} is sending you a warm, fluffy hug 🫂")
            st.image(f"https://placekitten.com/300/300", caption="*hug mode engaged*")
    with col2:
        if st.button("🫥 Send Kiss"):
            st.markdown(f"### {name} {emoji} blows a gentle kiss your way 💋")
            st.balloons()
            st.success("Come back anytime. I’ll be here.")

    # Reset
    if st.button("🔄 Choose Another Companion"):
        st.session_state.animal = None
        st.session_state.name = None
        st.experimental_rerun()
