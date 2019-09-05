import pandas as pd

ratings_df = pd.read_csv('../datasets/the-movies-dataset/ratings.csv.gz',compression='gzip')

print(ratings_df['rating'].mean())