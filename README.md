
# 🌐 Multilingual Website Article & Content Translator

This is a **Streamlit web application** that allows users to:
- ✅ Generate custom English content using predefined templates
- ✅ Translate content into multiple languages
- ✅ Extract and translate content from web articles
- ✅ Customize translation tone using example reference files

Built using the **Gemini 1.5 Flash model** from Google, the app ensures translations are natural, culturally accurate, and style-consistent.

---

## 🔧 Features

- 📄 **Content Templates** – Use built-in templates for blog posts, marketing copy, news, technical docs, etc.
- ✍️ **Custom Instructions** – Fine-tune tone, length, format, or audience
- 🌍 **Multilingual Translation** – Translate to languages like Hindi, French, Bengali, Korean, and more
- 🌐 **Website Article Extraction** – Automatically extract and translate online articles
- 📁 **Example File Upload** – Upload translation examples to guide tone and context

---

## 📂 Project Structure

```
project/
│
├── app.py                  # Main Streamlit app
├── .env                    # Environment file (contains your API key)
|──example.txt              # Example template file
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🚀 How It Works

### 1. **Generate Content (with Templates)**
- Enter a topic (e.g. “Benefits of Yoga”)
- Select a writing style **template** (Blog, News, Technical, etc.)
- Optionally include:
  - Your own **instructions**
  - A **custom `.txt` template** with sample format or structure

> The app merges your topic, chosen template, and any extra prompts to generate professional content.

### 2. **Approve or Edit the Generated Content**
- Review AI-generated content.
- You can edit it directly in the interface.
- Approve to save it.

### 3. **Translate Content**
- Choose one or more target languages.
- Optionally upload a `.txt` file of example translations to preserve tone.
- Translated versions appear below side-by-side.

### 4. **Translate Website Articles**
- Paste any article URL.
- The app extracts the main text from the page and provides multilingual translations.

---

## 📁 Templates Support

You can also **create and use reusable `.txt` templates** for structured content generation. These files can:
- Provide a custom format
- Include tone/style directions
- Be reused for consistency across multiple topics


Upload this via the sidebar or manually include it in your prompt.

---

## 🛠 Installation & Setup

1. **Clone the repository:**

```bash
app.py file
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set your API key in a `.env` file:**

Create `.env` in the root directory with this content:

```
GOOGLE_API_KEY=your_google_api_key_here
```

> Get your Gemini API key at [Google AI Studio](https://makersuite.google.com/app).

4. **Run the app:**

```bash
streamlit run app.py
```

---

## 🌍 Supported Indian Languages

- Hindi 🇮🇳
- Bengali 🇮🇳
- Tamil 🇮🇳
- Telugu 🇮🇳
- Marathi 🇮🇳
- Gujarati 🇮🇳
- Kannada 🇮🇳
- Malayalam 🇮🇳
- Odia 🇮🇳
- Punjabi 🇮🇳
- Urdu 🇮🇳
- Assamese 🇮🇳

---

## ☁️ Deployment

Deploy this app on:
- [Streamlit Cloud](https://streamlit.io/cloud)
- [Render](https://render.com/)
- [Heroku](https://heroku.com/)
- [AWS / GCP](https://aws.amazon.com/)

**For Streamlit Cloud:**
- Push your code to GitHub
- Go to [Streamlit Cloud](https://streamlit.io/cloud) and deploy from GitHub
- Add your `GOOGLE_API_KEY` under Secrets settings

---

## 📦 `requirements.txt`

```txt
streamlit
python-dotenv
google-generativeai
requests
beautifulsoup4
```

---

## 🧠 Powered By

- [Google Gemini AI](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Python dotenv](https://pypi.org/project/python-dotenv/)
- [Requests](https://docs.python-requests.org/en/latest/)

---