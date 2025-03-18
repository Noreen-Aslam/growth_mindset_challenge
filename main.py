import streamlit as st

# Page Configuration
st.set_page_config(page_title="Growth mindset project", page_icon="★")

# Title and Introduction
st.title("Growth Mindset Challenge: Web App With Streamlit")
st.header("Welcome to your Growth Journey!")
st.write("lorem ipsum mieofn mriuwj mirjfir mfirh jih fjieh nfi  mfihr fnirh jfief nfur fur jfie jfie  nfiehf nfue ")

# Quote Section
st.header("💡 Today's Growth Mindset Quote")
st.write('"Success is not final, failure is not fatal: it is the courage to continue that counts." -Winston Churchill')

# User Input for Challenge
st.header("🚀 What's your challenge today!")
user_input = st.text_input("Describe the challenge you're facing")

if user_input:
    st.success(f"You're facing: {user_input}. Keep pushing forward towards your goals!")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflection Section
st.header("📚 Reflect on your learning")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Great insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past experiences helps you grow! Share your difficulties.")

# Achievements Section
st.header("🎉 Celebrate your wins")
achievements = st.text_input("Share something you're proud of:")

if achievements:
    st.success(f"Amazing! You achieved: {achievements}")
else:
    st.info("Big or small, every achievement counts! Share one now.")

# Footer
st.write("_ _ _")
st.write("You're doing amazing! Every step counts. Keep growing and shining! ✨")
st.write("**⛔ Created by Noreen Aslam**")
