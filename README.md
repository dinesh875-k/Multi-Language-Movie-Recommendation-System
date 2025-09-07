# 🎬 Multi-Language Movie Recommendation System

This project is a **Flask-based web application** that recommends movies in **Hindi, Telugu, and English (Hollywood)** using **user-based collaborative filtering**.  
The system analyzes user ratings, computes similarity between users with **cosine similarity**, and suggests **personalized movies** that match the user’s preferences.  

---

## 🚀 Features
- Personalized recommendations for each user  
- Supports **Hindi, Telugu, and Hollywood (English)** movies  
- Filter recommendations by **genre** and **minimum rating**  
- Simple **Flask web interface** with input forms for user selection  
- User-friendly display of **Top-N recommended movies**  

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask  
- **Machine Learning:** Pandas, Scikit-learn (Cosine Similarity)  
- **Frontend:** HTML, Jinja2 Templates  
- **Datasets:** Custom curated datasets for Hindi, Telugu, and English movies  

---

## 📂 Project Structure
<img width="418" height="666" alt="image" src="https://github.com/user-attachments/assets/3369f66b-4810-4771-af4d-b796ecb462d9" />

  
---

## ⚡ How It Works
1. Loads **movie and ratings datasets** for each language.  
2. Builds a **user-item matrix** and computes **cosine similarity** between users.  
3. Identifies **similar users** and generates recommendations.  
4. Applies **filters (genre & rating)** to refine results.  
5. Displays **Top-N movie recommendations** via a **web interface**.  

---


