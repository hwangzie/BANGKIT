import sys

log_file = sys.argv[0]  
with open(log_file) as file:
    for line in file:
        print(line.strip())