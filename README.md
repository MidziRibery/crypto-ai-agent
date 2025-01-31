# 🚀 Crypto AI Agent  
An **AI-powered crypto intelligence agent** that fetches real-time cryptocurrency tweets, summarizes key insights using OpenAI’s API, and stores the data in Firebase. This project helps traders and enthusiasts stay informed with **concise, real-time market updates**.

## 📌 Features
✅ Fetches latest crypto-related tweets 📢  
✅ Uses **AI-powered NLP** to summarize key insights 🤖  
✅ Stores processed data in **Firebase** 🔥  
✅ Web interface for easy access 🌐  

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask), OpenAI API, Firebase SDK  
- **Frontend:** React.js, TailwindCSS  
- **Database:** Firebase Firestore  
- **APIs Used:** Twitter API, OpenAI API  

---

## 🚀 Setup & Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/<your-username>/crypto-ai-agent.git
cd crypto-ai-agent
```

### **2️⃣ Backend Setup**
#### **Create Virtual Environment (Recommended)**
```bash
python -m venv chatbot-env
source chatbot-env/bin/activate  # Mac/Linux
chatbot-env\Scripts\activate     # Windows
```

#### **Install Backend Dependencies**
```bash
pip install -r backend/requirements.txt
```

#### **Set Up Environment Variables**
Create a `.env` file inside `backend/` and add:
```ini
OPENAI_API_KEY="your_openai_api_key"
TWITTER_API_KEY="your_twitter_api_key"
FIREBASE_CONFIG="your_firebase_credentials"
```

### **3️⃣ Frontend Setup**
```bash
cd frontend
npm install
npm run dev
```

---

## 💽 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/crypto-news` | Fetches latest cryptocurrency news and summaries |

---

## 🔐 Security Best Practices
🚨 **Ensure you never expose API keys!**  
✅ Use `.env` for sensitive credentials  
✅ Add `backend/firebase_key.json` and `.env` to `.gitignore`  
✅ **Rotate API keys periodically**  

---

## 🛠️ To-Do List
- [ ] Implement AI-powered sentiment analysis  
- [ ] Add advanced filtering for tweets  
- [ ] Improve UI for real-time data visualization  
- [ ] Optimize Firebase queries for faster data retrieval  
- [ ] Enhance authentication with OAuth or JWT  
- [ ] Develop a mobile-friendly UI version  

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repo 🍔  
2. Create a new branch: `git checkout -b feature-name`  
3. Commit your changes: `git commit -m "Added new feature"`  
4. Push and submit a **pull request**  

---

## 🐝 License
This project is licensed under the **MIT License**.  

---

## 👨‍💻 Author
Created by **MidziRibery**  
🔗 GitHub: [MidziRibery](https://github.com/MidziRibery)  

---

🚀 **Star this repo if you like it!** 🌟  

