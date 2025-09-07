import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


# loading datasets
movies = pd.read_csv("C:\\Users\\hp\\Desktop\\projects\\movierecommender\\hindi datasets\\hindi_movies_dataset.csv")
ratings = pd.read_csv("C:\\Users\\hp\\Desktop\\projects\\movierecommender\\hindi datasets\\hindi_user_ratings_dataset.csv")

# building user-item matrix
user_item_matrix = ratings.pivot(index="user_id", columns="movie_id", values="user_rating").fillna(0)


# Computing cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, 
                                  index=user_item_matrix.index, 
                                  columns=user_item_matrix.index)


def recommend_movies(user_id, n=5, genre_filter=None, min_rating=0):

    # recommending top n movies for a user using user-based collaborative filtering.

    if user_id not in user_item_matrix.index:
        raise ValueError(f"User {user_id} not found in dataset.")

    # finding similar users (excluding self)
    similar_users = user_similarity_df[user_id].drop(user_id).sort_values(ascending=False).index

    # getting ratings from similar users
    similar_ratings = ratings[ratings["user_id"].isin(similar_users)]
    avg_ratings = similar_ratings.groupby("movie_id")["user_rating"].mean().reset_index()
    avg_ratings.rename(columns={"user_rating": "predicted_rating"}, inplace=True)

    # excluding movies already rated by target user
    seen_movies = set(ratings[ratings["user_id"] == user_id]["movie_id"])
    recommendations = avg_ratings[~avg_ratings["movie_id"].isin(seen_movies)]

    # merge with movies metadata
    recommendations = recommendations.merge(movies, on="movie_id", how="left")

    # applying rating filter
    recommendations = recommendations[recommendations["predicted_rating"] >= min_rating]

    # applying genre filter
    if genre_filter:
        if isinstance(genre_filter, str):
            recommendations = recommendations[recommendations["genre"].str.contains(genre_filter, case=False, na=False)]
        elif isinstance(genre_filter, list):
            recommendations = recommendations[recommendations["genre"].apply(
                lambda g: any(gen.lower() in g.lower() for gen in genre_filter)
            )]

    # Sorting and returning top n movies
    return recommendations.sort_values(by="predicted_rating", ascending=False).head(n)[["title", "genre", "predicted_rating"]]

"""# example :
print("top 5 for user_1:")
print(recommend_movies(user_id="user_1", n=5))

print("\n only action movies:")
print(recommend_movies(user_id="user_1", n=5, genre_filter="Action"))

print("\n drama/comedy movies with predicted rating >= 4:")
print(recommend_movies(user_id="user_1", n=5, genre_filter=["romance"], min_rating=4))"""


