# SoulSync - Full App (v2.1)
# By: Hadia, a gentle mental health companion
# Built using Streamlit

import streamlit as st
import random
from datetime import datetime

# ---------------------------------- CONFIG & STYLING ----------------------------------
st.set_page_config(page_title="SoulSync", page_icon="🧊", layout="wide")
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #f9f5f0, #ffe4e1);
        }
        .main {
            font-family: 'Poppins', sans-serif;
        }
        .hug-screen, .kiss-screen {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: #ffd6e8;
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------- STATE VARIABLES ----------------------------------
if "animal" not in st.session_state:
    st.session_state.animal = "🐰"
if "name" not in st.session_state:
    st.session_state.name = "Moony"
if "journal" not in st.session_state:
    st.session_state.journal = []
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# ---------------------------------- SMART CHATBOT LOGIC ----------------------------------
def get_response(user_input):
    user_input = user_input.lower()
    if "sad" in user_input:
        return "Oh no bestie 😢 Want a hug or should I just listen?"
    elif "anxious" in user_input or "panic" in user_input:
        return "Deep breaths, okay? In... out... You're safe now. 💗"
    elif "tired" in user_input:
        return "You deserve to rest, like fr. Moony's curling up next to you 🐰🛌"
    elif "happy" in user_input:
        return "YAY bestie!! I'm so proud of you ✨ Wanna celebrate with sparkles?"
    elif "numb" in user_input:
        return "Even silence means something. I’m still here with you. 💞"
    else:
        return "That’s totally valid. I’m here if you wanna keep talking ✨"

# ---------------------------------- COMPANION RESPONSES ----------------------------------
quotes = [
    "You are enough, exactly as you are. ",
    "Your feelings are valid. Even the messy ones.",
    "Healing isn't linear. You're allowed to wobble.",
    "You’re not alone. Not now, not ever. ",
    "Your softness is your strength."
]

# ---------------------------------- PAGES ----------------------------------
menu = st.sidebar.radio("Go to:", ["Home", "Choose Companion", "Chat", "Mood Check-In", "Journal", "About SoulSync"])

# ---------------------------------- HOME ----------------------------------
if menu == "Home":
    st.title("Welcome to SoulSync ✨")
    st.subheader(f"{random.choice(quotes)}")
    st.write(f"Hey there! {st.session_state.name} {st.session_state.animal} is so happy to see you today.")
    st.image("https://media.tenor.com/lsYv4I4ZkgoAAAAi/cute-love.gif", width=200)

# ---------------------------------- COMPANION PICKER ----------------------------------
elist = ["🐰", "🐶", "🐱", "🐥", "🐠", "🐼", "🦜", "🐢"]

if menu == "Choose Companion":
    st.subheader("Choose your emotional support animal")
    animal = st.selectbox("Pick an animal:", elist)
    name = st.text_input("Name your companion:", value="Moony")
    if st.button("Save Companion"):
        st.session_state.animal = animal
        st.session_state.name = name
        st.success(f"Saved! Say hi to {name} {animal}")

# ---------------------------------- CHAT ----------------------------------
if menu == "Chat":
    st.subheader(f"Chat with {st.session_state.name} {st.session_state.animal}")
    for entry in st.session_state.chat_log:
        st.markdown(entry, unsafe_allow_html=True)

    user_input = st.text_input("Talk to your companion:", key="chat_input")

    if st.button("Send"):
        if user_input:
            st.session_state.chat_log.append(f"<b>You:</b> {user_input}")
            reply = get_response(user_input)
            st.session_state.chat_log.append(f"<b>{st.session_state.name} {st.session_state.animal}:</b> {reply}")
            st.session_state.chat_input = ""

    if st.button("🤍 Send Hug"):
        st.markdown("""
        <div class='hug-screen'>
            <h2>Here’s your hug. You’re safe now. ❤️</h2>
            <img src='https://media.tenor.com/hkWjFCS5FAYAAAAi/bunny-cute.gif' width='200'>
        </div>
        <script>
            setTimeout(() => window.location.reload(), 4000);
        </script>
        """, unsafe_allow_html=True)

    if st.button("Send Kiss 🦋"):
        st.markdown("""
        <div class='kiss-screen'>
            <h2>{0} {1} is blowing you a kiss! 😘</h2>
            <img src='https://media.tenor.com/6I4LFHGnZJ0AAAAi/peach-goma-love.gif' width='200'>
            <p><i>Come back anytime. I’ll be here.</i></p>
        </div>
        <script>
            setTimeout(() => window.location.reload(), 4000);
        </script>
        """.format(st.session_state.name, st.session_state.animal), unsafe_allow_html=True)

# ---------------------------------- MOOD ----------------------------------
if menu == "Mood Check-In":
    st.subheader("How are you feeling today?")
    mood = st.selectbox("Pick a mood:", ["😭 Sad", "😐 Numb", "😡 Angry", "😊 Happy", "✨ Hopeful"])
    st.write(f"{st.session_state.name} {st.session_state.animal} says:")
    if mood == "😭 Sad":
        st.info("Tears are not weakness. I'm here with you.")
    elif mood == "😐 Numb":
        st.info("Even when it’s quiet inside you, I’m still listening.")
    elif mood == "😡 Angry":
        st.info("You’re allowed to feel fire. Let’s breathe through it.")
    elif mood == "😊 Happy":
        st.info("YAY! I'm happy dancing with you bestie 🥺")
    elif mood == "✨ Hopeful":
        st.info("Hope is a soft glow. Keep following it.")

# ---------------------------------- JOURNAL ----------------------------------
if menu == "Journal":
    st.subheader("Write your heart out")
    title = st.text_input("Entry title")
    content = st.text_area("Your thoughts")
    if st.button("Save Entry"):
        timestamp = datetime.now().strftime("%d %b %Y | %I:%M %p")
        st.session_state.journal.append((title, content, timestamp))
        st.success("Saved to your memory vault 📃")
    if st.session_state.journal:
        st.markdown("---")
        for i, (t, c, ts) in enumerate(reversed(st.session_state.journal)):
            st.markdown(f"**{t}**  ")
            st.markdown(f"*{ts}*  ")
            st.markdown(f"> {c}")
            st.markdown("---")

# ---------------------------------- ABOUT ----------------------------------
if menu == "About SoulSync":
    st.title("About SoulSync")
    st.write("""
    SoulSync is a safe, sparkly corner of the internet made for when you need a hug, a friend,
    or just a moment to breathe. Your companion is always here — listening, comforting, and
    growing with you. Whether you're joyful or hurting, SoulSync meets you where you are.

    Made with stardust, code, and compassion by Hadia 🧊
    """)
