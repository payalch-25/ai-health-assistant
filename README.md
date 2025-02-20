# Healthcare Assistant Chatbot 🤖

A Streamlit-based AI chatbot designed to provide preliminary medical information, symptom analysis, and appointment scheduling assistance. *Note:* This is not a substitute for professional medical care.

![Screenshot](image.png)

---

## Features ✨

- *Symptom Analysis*: Get basic information about common symptoms (e.g., fever, cough).
- *Medication Information*: Quick access to common drug usage guidelines.
- *Emergency Detection*: Automatic alerts for critical keywords (chest pain, difficulty breathing).
- *AI-Powered Responses*: Microsoft BioGPT-Large model for complex queries.
- *Appointment Scheduling*: Basic scheduling assistance framework.
- *Conversation History*: Maintains context during interaction.

## Installation ⚙️

1. *Clone Repository*

   bash
   git clone https://github.com/kayozxo/Health-Assistant.git
   cd Health-Assistant
   

2. *Install Dependencies*

   bash
   pip install -r requirements.txt
   

3. *Download NLTK Data*

   python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   

## Usage 🚀

1. *Run Application*

   bash
   streamlit run app.py
   

2. *Interaction Examples*:

   - "I have a fever and headache"
   - "What's the dosage for ibuprofen?"
   - "Book an appointment for next Tuesday"
   - Emergency phrases trigger alerts: "I'm experiencing chest pain"

3. *Interface Guide*:
   - Type medical queries in chat input
   - Conversation history persists during session
   - Emergency warnings appear as red alerts

## Configuration ⚙️

Modify MEDICAL_KB in app.py to:

- Add/update symptoms and responses
- Expand medication database
- Update emergency keywords

python
MEDICAL_KB = {
    "symptoms": {
        "new_symptom": "Response text..."
    },
    # ... other sections
}


## Model Details 🤖

- *Base Model*: [microsoft/BioGPT-Large](https://huggingface.co/microsoft/BiomedNLP-BioGPT-Large)
- *Hardware Recommendations*:
  - GPU recommended for faster inference
  - Minimum 16GB RAM for optimal performance

## Contributing 🤝

1. Fork the repository
2. Create feature branch (git checkout -b feature/improvement)
3. Commit changes
4. Push to branch
5. Open Pull Request

---

## Important Disclaimers ⚠️

- ❗ *Not a medical diagnostic tool*
- ❗ Always consult qualified healthcare professionals
- ❗ Emergency responses should be verified through official channels
- ❗ Medication information is for reference only

## Acknowledgments

- Microsoft Research for BioGPT-Large model
- Hugging Face Transformers library
- NLTK for text processing
- Streamlit for UI framework

---

For educational purposes only. Use at your own risk.