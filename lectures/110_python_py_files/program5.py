
import sys

if len(sys.argv) < 2:
    print("Error: Missing BATCH_DATE. Please run as 'python program5.py <BATCH_DATE>`")
    sys.exit(1)

BATCH_DATE = sys.argv[1] #<= Here is the magic
print(f"This program is run on {BATCH_DATE}")
