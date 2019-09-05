import gzip
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ratings_file")
args = parser.parse_args()

ratings_file = args.ratings_file

counter = 0
sum_rating = 0
len_rating = 0

#userId,movieId,rating,timestamp
#with gzip.open('../datasets/the-movies-dataset/ratings_small.csv.gz','rt', encoding='utf8') as infile:
with gzip.open(ratings_file,'rt', encoding='utf8') as infile:
    for line in infile:
        counter += 1
        if(counter ==1): 
            continue
        cleaned_line = line.strip()
        #print(cleaned_line)
        rating = cleaned_line.split(",")[2]
        sum_rating += float(rating)
        len_rating += 1

print("Averaging rating: ",sum_rating/len_rating)