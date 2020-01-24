data_file_location = "../datasets/deaths-in-gameofthrones/game-of-thrones-deaths-data.csv"

season_d = dict()

#Open file
file = open(data_file_location, encoding='utf8')

#Go through each line in file
for line in file:
  tokens = line.split(',') #separate line into columns
  s = tokens[1]
  if s not in season_d: season_d[s] = 1
  else: season_d[s] += 1

file.close()

print(season_d)