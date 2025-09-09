### Movie Recommendation System

A content-based movie recommendation system built using **Python** and popular data science libraries. The system analyzes movie metadata such as genres, keywords, cast, and crew to find and suggest movies with similar attributes. It uses **cosine similarity** to calculate the similarity between movies, providing a simple yet effective way to discover new films.

-----

### ✨ Features

  * **Content-Based Filtering:** Recommends movies based on shared characteristics rather than user behavior.
  * **Metadata Analysis:** Extracts and processes key information like cast, crew (specifically the director), genres, and keywords.
  * **Vectorization:** Converts textual metadata into numerical vectors using `CountVectorizer`.
  * **Similarity Calculation:** Computes movie similarity using the **cosine similarity** metric.
  * **Simple Interface:** Provides a function to input a movie title and receive a list of top recommendations.

-----

### 💻 Tech Stack

  * **Jupyter Notebook:** The primary environment for development and demonstration.
  * **Pandas:** Used for data manipulation and analysis.
  * **Scikit-learn:** Provides tools for text vectorization (`CountVectorizer`) and similarity calculation (`cosine_similarity`).
  * **ast:** Used to safely parse string representations of lists and dictionaries.

-----

### ⚙️ Getting Started

Follow these steps to set up the project and run the notebook.

#### **1. Clone the repository**

```bash
git clone https://github.com/sujith-ox/movie_recommendation_system.git
cd movie_recommendation_system
```

#### **2. Install Dependencies**

It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can install the required libraries manually:

```bash
pip install pandas scikit-learn
```

#### **3. Run the Notebook**

Start the Jupyter Notebook server in your terminal.

```bash
jupyter notebook
```

A browser window will open. Navigate to `movie_recommendation_system.ipynb` to view and run the code.

-----

### 📊 How It Works

The system operates in these key steps:

1.  **Data Loading:** It loads two datasets (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`) and merges them.
2.  **Feature Extraction:** It extracts and cleans relevant data from JSON-like strings in columns like `genres`, `keywords`, `cast`, and `crew`.
3.  **Vectorization:** It creates a matrix where each row represents a movie and each column represents a word from its metadata.
4.  **Similarity Calculation:** It calculates the cosine similarity between every movie's vector, resulting in a similarity matrix.
5.  **Recommendation:** When a movie title is provided, the system finds its index in the matrix and returns the titles of the most similar movies based on their similarity scores.
