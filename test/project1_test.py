import sys
args = sys.argv

if len(args) == 1:
    src = "students.txt"
else:
    src = args[1]

with open(src, "r") as f:
    command = input()