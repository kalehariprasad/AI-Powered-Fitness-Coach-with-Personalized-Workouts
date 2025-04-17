# 🏋️‍♀️ AI-Powered Personalized Workout Planner

This project is a web-based AI fitness assistant that generates personalized workout plans based on user preferences such as fitness level, goals, duration, and available equipment. It leverages **LangChain**, **Hugging Face's Mistral-7B**, and **Streamlit** to deliver step-by-step workouts — with a downloadable PDF output. The app is fully containerized using **Docker** and supports CI/CD via **GitHub Actions**.

---

## 🚀 Features

- 🔮 **AI-Generated Workout Plans** using Mistral-7B-Instruct via Hugging Face API  
- 🧠 **Prompt Engineering** using LangChain’s `PromptTemplate`  
- 🧾 **Downloadable PDF** with exercise details and user preferences  
- 🌐 **Streamlit UI** for interactive user inputs  
- 🐳 **Dockerized** for portable deployment  
- 🔁 **CI/CD Pipeline** with GitHub Actions + Docker Hub integration  

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| 🐍 Python 3.9 | Core application logic |
| 🤖 Hugging Face (Mistral-7B) | LLM API for workout generation |
| 🔗 LangChain | Prompt handling & LLM chaining |
| 📊 Streamlit | Frontend UI |
| 📄 FPDF | PDF generation of workout plans |
| 🐳 Docker | Containerization |
| 🔁 GitHub Actions | CI/CD Pipeline |

---

## 📸 Demo

🎥 [Watch Workout Planner Demo Video](https://drive.google.com/file/d/1WLKK4NxK0VtlLRMqyqX3KXWmGvaW7sIM/view?usp=sharing)




---

## 🧪 Local Development

### 🔧 Requirements

- Python 3.9+
- Hugging Face API Token (add to `.env` or Streamlit Secrets)
- Docker (optional, for containerized deployment)

### 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### ⚙️ Run with Streamlit

```bash
streamlit run streamlit.py
```
### 🐳 Run with Docker

```bash
docker build -t workout-planner .
```

```bash
docker run -p 8501:8501 workout-planner
```

### 🛡️ Environment Variables


| Variable                 | Purpose                        |
|--------------------------|--------------------------------|
| HUGGINGFACEHUB_API_TOKEN | Your Hugging Face API token    |



## 🔄 CI Pipeline
This project uses GitHub Actions to automate:

✅ Docker image build

🚀 Push to Docker Hub

🔐 Environment variable validation

🔐 GitHub Secrets Required:
- DOCKER_USERNAME

- DOCKER_PASSWORD

- HUGGINGFACEHUB_API_TOKEN


