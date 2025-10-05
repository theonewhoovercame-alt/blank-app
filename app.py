import streamlit as st
import openai

# 🧠 Set your OpenAI API Key here
openai.api_key = "your-api-key-here"

# 🎯 Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 24.9:
        status = "Normal weight"
    elif 25 <= bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obese"
    return round(bmi, 2), status

# 💬 Function for AI health advice
def ai_health_advice(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly AI health assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]

# 🩺 Streamlit UI
st.set_page_config(page_title="AI Health Assistant", page_icon="🤖", layout="centered")

st.title("🤖 AI-Powered Health Assistant")
st.write("Track your health and get AI-based wellness advice instantly!")

# --- Step 1: Collect user data ---
with st.form("user_info_form"):
    st.subheader("Enter your basic details:")
    name = st.text_input("Your Name")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    height = st.number_input("Height (in meters)", min_value=0.5, max_value=2.5, step=0.01)
    weight = st.number_input("Weight (in kilograms)", min_value=10.0, max_value=300.0, step=0.1)
    submitted = st.form_submit_button("Calculate BMI")

if submitted:
    if height > 0 and weight > 0:
        bmi, status = calculate_bmi(weight, height)
        st.success(f"**{name}**, your BMI is **{bmi}**, which means you are **{status}**.")
    else:
        st.warning("Please enter valid height and weight.")

# --- Step 2: AI Health Q&A ---
st.subheader("💬 Ask the AI Health Assistant")
question = st.text_area("Enter your question (e.g., How can I improve my sleep?)")

if st.button("Get Answer"):
    if question.strip():
        with st.spinner("Thinking... 🤔"):
            answer = ai_health_advice(question)
            st.write("### 🧠 AI Health Assistant says:")
            st.success(answer)
    else:
        st.warning("Please enter a question first.")

st.markdown("---")
st.caption("Created as a High School AI Project 💡 | Powered by OpenAI")
