## 🎬Movie Recommendation system 
## Project Description

- Content-based movie recommendation system using TMDB dataset.

- Provides movie recommendations based on genres and overview.

- Built with Python and interactive Flask API.

## Features

- TF-IDF + Cosine Similarity for content-based recommendations.

- Handles multi-genre movies and missing metadata.

- Interactive front-end with input box and recommendations display.

- Visualization of movie genres using bar chart and pie chart.

## Dataset Details

- TMDB-style dataset with 600 rows.

**Important columns:**

- title → Movie name

- genres → Movie genres (pipe-separated)

- overview → Movie description

- popularity → Popularity score

- vote_average → Average rating

vote_count → Number of ratings

## Visualization Types

- Bar chart → Number of movies per genre.

- Pie chart → Percentage distribution of movies by genre.

## Main Libraries / Technologies Used

- Python 3

- Flask → API and front-end integration

- Pandas → Data loading and cleaning

- scikit-learn → TF-IDF vectorization, cosine similarity

- Matplotlib → Visualizations (bar and pie charts)

- HTML + CSS → Front-end interface

## Performance / Evaluation

- Content-based filtering evaluated qualitatively using sample queries.

- Top N recommended movies compared manually for relevance.
- Cosine similarity provides similarity ranking between movies.
