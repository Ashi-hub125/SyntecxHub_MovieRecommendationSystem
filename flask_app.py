from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load dataset
df = pd.read_csv("movie_recommendation_dataset.csv")

# Metadata cleaning
df['overview'] = df['overview'].fillna('').str.lower()
df['genres'] = df['genres'].fillna('').str.lower()
df['combined_features'] = df['genres'] + " " + df['overview']

# TF-IDF
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(df['combined_features'])

# Cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend_movies(title, top_n=5):
    if title not in df['title'].values:
        return "Movie not found in dataset"
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    return df[['title', 'genres']].iloc[movie_indices].to_dict(orient='records')

# Routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/recommend', methods=['GET'])
def recommend():
    movie_title = request.args.get('title')
    if not movie_title:
        return jsonify({"error": "Please provide a movie title"})
    recommendations = recommend_movies(movie_title)
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
