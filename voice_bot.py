import openai
import pyttsx3

# Replace with your OpenAI API key
openai.api_key = "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"

# Text-to-Speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed
engine.setProperty('volume', 1)  # Volume

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Chat with GPT
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use gpt-4 if available
        messages=[
            {"role": "system", "content": "You are a helpful voice assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    reply = response['choices'][0]['message']['content']
    return reply

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        speak("Goodbye!")
        break
    reply = chat_with_gpt(user_input)
    print("Assistant:", reply)
    speak(reply)
