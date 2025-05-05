import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup

# # Load environment variables
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key="AIzaSyAqNcauLu380PuzMQkpRs8C8Cnx0KL5vbE")
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize session state
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = ""

if 'is_approved' not in st.session_state:
    st.session_state.is_approved = False

# Extract article content from a URL
def extract_main_article(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        main_content = ''
        for tag in ['article', 'main', 'div', 'section']:
            candidates = soup.find_all(tag)
            for candidate in candidates:
                text = candidate.get_text(separator=' ', strip=True)
                if len(text.split()) > 300:
                    main_content = text
                    break
            if main_content:
                break

        if not main_content:
            main_content = soup.get_text(separator=' ', strip=True)

        return main_content
    except Exception as e:
        return f"Error extracting article: {e}"

# Translate content using Gemini
def translate_content(content, target_language, examples):
    prompt = f"""
You are a professional translator.
Translate the following article into {target_language}.
Preserve tone, cultural nuances, and professional style. Use the style from the examples provided.

Examples:
{examples}

Article to translate:
{content}

Note: Only output the translated content.
"""
    try:
        response = model.generate_content(
            contents=[{"role": "user", "parts": [{"text": prompt}]}]
        )
        return response.text
    except Exception as e:
        return f"Error translating: {e}"

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Multilingual Website Translator", layout="wide")
st.title("Website Article Multilingual Translator")

# Sidebar example file uploader
st.sidebar.header("Upload Translation Style Examples (Optional)")
example_file = st.sidebar.file_uploader("Upload a 'example.txt' file", type="txt")
examples = example_file.read().decode('utf-8') if example_file else ""

# ---------- 1. Content Generation Section ----------
st.header("Content Generation (English)")

st.subheader("Content Creation Inputs")

topic = st.text_input("Enter a topic for content generation:")

style_presets = {
    "Blog Post": "Write it like a blog post with an informal tone and personal voice.",
    "News Article": "Structure it like a news article with a headline, lead, and factual tone.",
    "Marketing Copy": "Write persuasively with emotional appeal and strong call to action.",
    "Technical Documentation": "Use concise, clear, and structured technical language.",
    "Listicle": "Format as a list with numbered or bullet points and short explanations.",
    "Storytelling": "Narrate in a story format with a hook, buildup, and resolution."
}

selected_style = st.selectbox("Choose a writing style:", list(style_presets.keys()))

custom_prompt = st.text_area(
    "Optional: Add specific instructions (tone, length, audience, format, etc.):",
    placeholder="E.g. Include 3 real-life examples, make it SEO-optimized, etc.",
    height=100
)

if st.button("Generate Content"):
    if not topic.strip():
        st.error("Please enter a topic.")
    else:
        style_instruction = style_presets.get(selected_style, "")
        full_prompt = f"""
Generate content based on the following topic: {topic}

Style Guide:
{style_instruction}

Extra Instructions:
{custom_prompt if custom_prompt else "No additional instructions."}
"""
        with st.spinner("Generating content..."):
            try:
                response = model.generate_content(full_prompt)
                st.session_state.generated_content = response.text
                st.session_state.is_approved = False
            except Exception as e:
                st.error(f"Error: {e}")

if st.session_state.generated_content:
    content = st.text_area("Edit the generated content if needed:", st.session_state.generated_content, height=300)

    if st.button("Approve and Save"):
        st.session_state.generated_content = content
        st.session_state.is_approved = True
        with open("approved_articles.txt", "a", encoding="utf-8") as f:
            f.write("\n\n---\n\n" + content)
        st.success("Content approved and saved!")

# ---------- 2. Translation of Approved Generated Content ----------
if st.session_state.is_approved:
    st.header("Translate Approved Content")

    target_languages = st.multiselect("Select Indian languages:", [
        "Hindi", "Bengali", "Tamil", "Telugu", "Marathi", "Gujarati", "Kannada", "Malayalam", "Odia", "Punjabi", "Urdu", "Assamese"
    ], key="generated_translation")

    if st.button("Translate Content"):
        translations = {}
        progress = st.progress(0)

        for idx, lang in enumerate(target_languages):
            with st.spinner(f"Translating to {lang}..."):
                translated = translate_content(st.session_state.generated_content, lang, examples)
                translations[lang] = translated
            progress.progress((idx + 1) / len(target_languages))

        st.header("Translated Versions")
        cols = st.columns(2)
        for i, (lang, text) in enumerate(translations.items()):
            with cols[i % 2]:
                st.subheader(lang)
                st.markdown(f"<div style='text-align: justify;'>{text}</div>", unsafe_allow_html=True)

# ---------- 3. Website Article Translation (Original Logic) ----------
st.header(" Website Article Translator (Original Feature)")
url = st.text_input("Enter website link:")

target_languages = st.multiselect("Select Indian languages:", [
        "Hindi", "Bengali", "Tamil", "Telugu", "Marathi", "Gujarati", "Kannada", "Malayalam", "Odia", "Punjabi", "Urdu", "Assamese"
    ], key="generated_translation")

if st.button("Translate Website Article"):
    if not url:
        st.error("Please enter a URL!")
    else:
        with st.spinner("Extracting article..."):
            content = extract_main_article(url)

        if content.startswith("Error"):
            st.error(content)
        else:
            st.success("Article extracted successfully!")

            translations = {}
            progress = st.progress(0)

            for idx, lang in enumerate(target_languages_url):
                with st.spinner(f"Translating to {lang}..."):
                    translated = translate_content(content, lang, examples)
                    translations[lang] = translated
                progress.progress((idx + 1) / len(target_languages_url))

            st.header("Translated Versions")
            cols = st.columns(2)
            for i, (lang, text) in enumerate(translations.items()):
                with cols[i % 2]:
                    st.subheader(lang)
                    st.markdown(f"<div style='text-align: justify;'>{text}</div>", unsafe_allow_html=True)
