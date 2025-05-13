# Report-Scanner – Smart Medical Report Analyzer

**Report Scanner** is an AI-powered web application designed to analyze medical reports and provide intelligent, human-like diagnoses. Built with modern web technologies and AI integration, it simplifies healthcare report interpretation for doctors, patients, and researchers.

---

## 🚀 Features

- 📄 Upload `.txt` medical reports  
- 🧠 AI-powered diagnosis extraction  
- 🎯 Highlights key information and symptoms  
- 🖼️ Clean, responsive UI with Tailwind CSS  
- ⚠️ Error handling for unsupported files  
- 📦 Easily extendable for PDF, image, or EHR formats  

---

## 💻 Tech Stack

- **Frontend:** HTML5, Tailwind CSS  
- **Backend:** Python, Flask  
- **AI Integration:** LangChain, Groq/GPT models  
- **Template Engine:** Jinja2  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

```
├── app.py                  # Main Flask backend
├── Utils/
├── └── agents.py          
├── templates/
│   └── index.html          # UI for upload and result display
├── Main.py
├── uploads/                # Temporary storage for uploaded files
└── README.md
```

---

## 🧪 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/SHIVANSH-A/Report-Scanner.git
   cd Report-Scanner
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask app**
   ```bash
   python app.py
   ```

4. **Visit in browser**
   ```
   http://127.0.0.1:5000
   ```
---

