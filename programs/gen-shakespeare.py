import gzip
import random

src_dst = {}
prev_word = ""

with gzip.open('../datasets/shakespeare/t8.shakespeare.txt.gz','rt', encoding='utf8') as infile:
    for line in infile:
        toks = line\
            .strip()\
            .lower()\
            .split()
        for tok in toks:
            if prev_word not in src_dst: src_dst[prev_word] = {}
            dst_dict = src_dst[prev_word]
            dst_freq = dst_dict.get(tok, 0) + 1
            src_dst[prev_word][tok] = dst_freq
            prev_word = tok

#Randomly pick a word from data
chosen_word = random.choice(list(src_dst.keys()))

#For each word, pick the following word with probability propotional to its frequency in the src_dst dictionary
for i in range(1000):
    distribution = src_dst[chosen_word]
    pop = list(distribution.keys())
    weights = list(distribution.values())
 
    next_word = random.choices(pop, weights=weights)[0]
    chosen_word = next_word

    print(next_word, end=' ')
    if(next_word.endswith(".")): print("")