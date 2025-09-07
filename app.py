from flask import Flask, render_template, request
from hindirecommender import recommend_movies as hindi_recommender
from telgue_movie_recommender import recommend_movies as telugu_recommender
from english_movie_recommender import recommend_movies as hollywood_recommender

app = Flask(__name__)

recommenders = {
    "hindi": hindi_recommender,
    "telugu": telugu_recommender,
    "hollywood": hollywood_recommender
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/filters/<language>", methods=["GET", "POST"])
def filters(language):
    if request.method == "POST":
        user_id = request.form.get("user_id", "").strip()
        top_n = int(request.form.get("top_n", 5))
        min_rating = float(request.form.get("min_rating", 0))
        genre_input = request.form.get("genres", "")
        genres = [g.strip() for g in genre_input.split(",")] if genre_input else None

        recommender_fn = recommenders.get(language)
        if not recommender_fn:
            return f"No recommender found for {language}"

        try:
            df = recommender_fn(user_id=user_id, n=top_n, genre_filter=genres, min_rating=min_rating)
        except ValueError as e:
            return str(e)

        recommendations = df.to_dict(orient="records")
        return render_template("recommendation.html", movies=recommendations, language=language)

    return render_template("filters.html", language=language)

if __name__ == "__main__":
    app.run(debug=True)
