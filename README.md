# Multi-Language-Movie-Recommendation-System
This project is a Flask-based web application that recommends movies in Hindi, Telugu, and English (Hollywood) using user-based collaborative filtering. The system analyzes user ratings, computes similarity between users with cosine similarity, and suggests personalized movies that match the user’s preferences.


Features :
 1.Personalized recommendations for each user
 2.Supports Hindi, Telugu, and Hollywood (English) movies
 3.Filter recommendations by genre and minimum rating
 4.Simple Flask web interface with input forms for user selection
 5.User-friendly display of top-N recommended movies


Tech Stack :
 1.Backend: Python, Flask
 2.Machine Learning: Pandas, Scikit-learn (Cosine Similarity)
 3.Frontend: HTML, Jinja2 Templates
 4.Datasets: Custom curated datasets for Hindi, Telugu, and English movies


Project Structure :
 Multi-Language-Movie-Recommendation-System/
 │── app.py
 │── hindirecommender.py
 │── telgue_movie_recommender.py
 │── english_movie_recommender.py
 │── requirements.txt
 │── README.md
 │── datasets/
 │   ├── hindi_movies_dataset.csv
 │   ├── hindi_user_ratings_dataset.csv
 │   ├── telugu_movies_dataset.csv
 │   ├── telugu_user_ratings_dataset.csv
 │   ├── english_movies_dataset.csv
 │   ├── english_user_ratings_dataset.csv
 │── templates/
    ├── index.html
    ├── filters.html
    ├── recommendation.html
 ├──static/      #some movies poster for design


How It Works :
1. Loads movie and ratings datasets for each language.  
2. Builds a user-item matrix and computes cosine similarity between users.  
3. Identifies similar users and generates recommendations.  
4. Applies filters (genre & rating) to refine results.  
5. Displays top n movie recommendations via a web interface.


