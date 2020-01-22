import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("infile")
args = parser.parse_args()

infile = args.infile

data_df = pd.read_csv(infile)
print(data_df[data_df.killer.isin(["Arya Stark", "Jon Snow"])].killer.value_counts())
