# 🗨️ Simple Chatbot using LLM with Groq Inference

This is a simple chatbot application powered by **Mixtral-8x7b-32768** — a cutting-edge language model. The chatbot uses **Groq** for ultra-fast AI inference, enabling rapid and efficient responses.

## 🌟 What is Groq?

Groq is a specialized inference platform designed to run large AI models (like Mixtral, LLaMA, etc.) much faster and more efficiently than traditional GPUs (like NVIDIA) or CPUs.

### Key Use Cases

- **Large Language Models (LLMs)** — Run models like Mixtral with ultra-low latency.
- **Real-time AI Applications**, including:
  - AI-powered chatbots and customer support assistants.
  - Voice assistants.
  - AI search engines.

---

## 📥 How to Set Up & Run

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/sharanya39/Chatbot.git
cd Chatbot
```

### 2️⃣ Get Your Groq API Key
- Visit: **[Groq Console - API Keys](https://console.groq.com)**
- Generate a new API key.
- Keep the key safe, as you will need it to run this project.

### 3️⃣ Create a `.env` File
In the same folder where `app.py` is located, create a file named `.env`. Add the following line to the `.env` file:
```sh
GROQ_API_KEY=your-groq-api-key-here
```
Replace `your-groq-api-key-here` with your actual key.

### 4️⃣ Install Required Libraries
Run the following command to install all necessary dependencies:
```sh
pip install -r requirements.txt
```
This will install:
- `Streamlit`
- `Langchain`
- `Langchain-community`
- `Langchain-groq`
- `OpenAI`
- `python-dotenv`
- Other required packages

### 5️⃣ Run the Application
After ensuring there are no errors during installation, you can start the chatbot by running:
```sh
streamlit run app.py
```
This will open a webpage in your browser (localhost) where you can interact with the chatbot.

---

## 🚀 How It Works

- The chatbot is powered by **Mixtral-8x7b-32768**, known for its high performance and multi-expert architecture.
- **Groq's inference engine** ensures ultra-fast responses.
- The **Streamlit UI** provides a simple interface for asking questions and receiving responses in real-time.

### ✅ Example Interaction
```plaintext
User: Ask any question from the document?
Bot: Sure! What would you like to ask?
```

Enjoy building with **Groq and Mixtral**! 🚀
