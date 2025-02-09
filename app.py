import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

st.set_page_config(page_title="Healthcare Assistant Chatbot", page_icon="🤖")

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load a more appropriate model (requires torch installation)
MEDICAL_MODEL_NAME = "microsoft/BioGPT-Large"
chatbot = pipeline("text-generation", model=MEDICAL_MODEL_NAME, device=-1)  # Use GPU if available

# Initialize session state for conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Medical knowledge base (simplified example)
MEDICAL_KB = {
    "symptoms": {
        "fever": "A fever is often a sign of infection. Monitor your temperature and stay hydrated.",
        "cough": "Coughs can be viral or allergy-related. If persistent, consult a doctor.",
        "headache": "Headaches can have many causes. Rest and hydration may help. If severe, seek medical attention.",
    },
    "emergency_keywords": ["chest pain", "difficulty breathing", "severe bleeding", "stroke", "passed out"],
    "common_medications": {
        "paracetamol": "Used for pain relief and reducing fever. Typical dose: 500mg every 4-6 hours.",
        "ibuprofen": "NSAID for pain and inflammation. Take with food. Do not exceed 1200mg/day without consultation.",
    }
}

def contains_emergency(text):
    return any(keyword in text.lower() for keyword in MEDICAL_KB["emergency_keywords"])

def get_medical_response(user_input):
    user_input = user_input.lower()

    # Emergency response
    if contains_emergency(user_input):
        return "🆘 This sounds serious! Please call emergency services immediately or go to the nearest hospital.", True

    # Symptom checking
    symptom_match = next((symptom for symptom in MEDICAL_KB["symptoms"] if symptom in user_input), None)
    if symptom_match:
        return f"Regarding {symptom_match}: {MEDICAL_KB['symptoms'][symptom_match]} Always consult a professional for proper diagnosis.", False

    # Medication queries
    med_match = next((med for med in MEDICAL_KB["common_medications"] if med in user_input), None)
    if med_match:
        return f"Information about {med_match}: {MEDICAL_KB['common_medications'][med_match]} Always follow your doctor's instructions.", False

    # Appointment scheduling
    if re.search(r'appointment|schedule|book', user_input):
        return "I can help you schedule an appointment. Please specify preferred date and time.", False

    # Fallback to model with medical context
    prompt = f"Patient: {user_input}\nDoctor:"
    response = chatbot(
        prompt,
        truncation=True,
        max_length=150,
        num_return_sequences=1,
        repetition_penalty=1.2
    )[0]['generated_text']

    # Extract only the doctor's response
    return response.split("Doctor:")[-1].strip(), False

def main():
    st.title("🤖 Healthcare Assistant Chatbot")
    st.caption("Note: This is an AI assistant and cannot replace professional medical advice.")

    # Display conversation history
    for role, message in st.session_state.conversation:
        st.chat_message(role).write(message)

    # Get user input
    if user_input := st.chat_input("How can I assist you today?"):
        # Add user message to history
        st.session_state.conversation.append(("user", user_input))
        st.chat_message("user").write(user_input)

        # Get and display bot response
        response, is_emergency = get_medical_response(user_input)
        st.session_state.conversation.append(("assistant", response))
        st.chat_message("assistant").write(response)

        if is_emergency:
            st.error("EMERGENCY ALERT: Please seek immediate medical attention!")

if __name__ == "__main__":
    main()