import streamlit as st
import nltk
from nltk.corpus import wordnet
import speech_recognition as sr

# Initialisation de NLTK
nltk.download("wordnet")
nltk.download("punkt")

# Fonction pour le chatbot
def chatbot(message):
    # Vous pouvez personnaliser cette fonction en ajoutant votre propre logique de réponse.
    # Dans cet exemple, le chatbot renvoie simplement le message d'entrée avec "Réponse: " devant.
    return "Réponse: " + message

# Fonction pour la reconnaissance vocale
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Parlez maintenant...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="fr-FR")
            st.write("Vous avez dit: " + text)
            return text
        except sr.UnknownValueError:
            st.write("Désolé, je n'ai pas compris votre message vocal.")
            return ""
        except sr.RequestError as e:
            st.write("Erreur lors de la demande de reconnaissance vocale: {0}".format(e))
            return ""

# Interface utilisateur Streamlit
st.title("Chatbot avec Reconnaissance Vocale")

message = st.text_input("Entrez votre message:")
if st.button("Envoyer"):
    response = chatbot(message)
    st.write(response)

if st.button("Parler (Reconnaissance Vocale)"):
    spoken_text = speech_to_text()
    if spoken_text:
        response = chatbot(spoken_text)
        st.write(response)
