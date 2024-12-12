import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def get_book_recommendations(book_id, books, ratings):
    book_ratings = ratings[ratings['book_id'] == book_id]
    similar_books = books[books['id'] != book_id]
    
    similarities = cosine_similarity(book_ratings[['rating']], similar_books[['rating']])
    recommended_books = similar_books.iloc[similarities.argsort()[0][-5:]]
    
    return recommended_books
