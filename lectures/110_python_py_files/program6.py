
import argparse

# Create the argument parser
parser = argparse.ArgumentParser(description="Scores sales transactions to predict returns.")

# Add an argument
parser.add_argument("BATCH_DATE", type=str, help="The date of sales transactions")

# Parse the arguments
args = parser.parse_args()

# Print the argument
print(f"This program is run on {args.BATCH_DATE}")
