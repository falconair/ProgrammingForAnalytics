# This program is used to demonstrate the debugger, shouldn't be used for anything else!
import gzip
import random

src_dst = {}
prev_word = ""

with gzip.open('../datasets/shakespeare/shakespeare.txt.gz','rt') as infile:
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

#Get words and thier distributions
def get_word_dist(dist):
    pop     = list(dist.keys())
    weights = list(distribution.values())
    return pop, weights

#For each word, pick the following word with probability propotional to its frequency in the src_dst dictionary
for i in range(100):
    distribution = src_dst[chosen_word]
    pop, weights = get_word_dist(distribution)
 
    next_word = random.choices(pop, weights=weights)[0]
    chosen_word = next_word

    print(next_word, end=' ')
    if(next_word.endswith(".")): print("")
