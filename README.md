# QuestBot – AI-Powered Text Adventure Game

**QuestBot** is an interactive, text-based adventure game that leverages **Natural Language Processing (NLP)**, **Unsupervised Learning**, and **Reinforcement Learning (RL)** to provide a dynamic and adaptive gameplay experience. Players type commands in natural language, and the AI understands, responds, and adapts the story based on the player’s behavior.  

---

## 🔹 Features

- **Supervised Learning (NLP)**
  - Understands player commands (attack, explore, pick, trade, etc.)  
  - Uses trained models to map text input to structured actions  

- **Unsupervised Learning**
  - Clusters players by behavior patterns (e.g., Aggressive, Explorer, Collector)  
  - Adapts gameplay based on player cluster  

- **Reinforcement Learning**
  - Adaptive AI Dungeon Master that evolves the game world  
  - Learns to maximize engagement and challenge based on player actions  

- **Backend + Frontend Integration**
  - Python FastAPI/Flask backend serves ML models and game logic  
  - React frontend for chat-style gameplay interface  

- **Data Persistence**
  - Stores player sessions, progress, and clustering data in a database  

---

## 🔹 Tech Stack

- **Backend**: Python, FastAPI / Flask  
- **Frontend**: React (Vite)  
- **NLP & ML**: scikit-learn, HuggingFace Transformers, NumPy, Pandas  
- **Reinforcement Learning**: Q-Learning / Deep Q-Network (PyTorch optional)  
- **Database**: PostgreSQL / SQLite  
- **Deployment**: Docker (optional)  

---

## 🔹 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/NarraAI.git
cd NarraAI
