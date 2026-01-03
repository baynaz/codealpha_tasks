# streamlit_translation_app.py
import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS # Google Text-to-Speech Python library
import tempfile

translator = Translator()

st.set_page_config(page_title="Language Translator", layout="centered")
st.title("🌐 Language Translator")

# --- User Input ---
text_to_translate = st.text_area("Enter text to translate:", height=150)

# Language selection
languages = list(LANGUAGES.values())
source_lang = st.selectbox("Source Language", ["auto"] + languages, index=0)
target_lang = st.selectbox("Target Language", languages, index=21)  # default English

# Translate button
if st.button("Translate"):
    if not text_to_translate.strip():
        st.warning("Please enter some text to translate!")
    else:
        # Map language names to codes
        lang_code_map = {v: k for k, v in LANGUAGES.items()}
        src_code = "auto" if source_lang == "auto" else lang_code_map[source_lang]
        tgt_code = lang_code_map[target_lang]

        # Translate
        try:
            result = translator.translate(text_to_translate, src=src_code, dest=tgt_code)
            translated_text = result.text
            st.success("Translation Complete")
            st.text_area("Translated Text:", translated_text, height=150)

            # --- Optional: Text-to-Speech ---
            if st.button("Play Translation"):
                tts = gTTS(translated_text, lang=tgt_code)
                with tempfile.NamedTemporaryFile(delete=True) as fp:
                    tts.save(f"{fp.name}.mp3")
                    st.audio(f"{fp.name}.mp3", format="audio/mp3")

        except Exception as e:
            st.error(f"Translation failed: {e}")
###########################################################################commands
# pip install streamlit googletrans==4.0.0-rc1 gtts
#streamlit run streamlit_translation_app.py

