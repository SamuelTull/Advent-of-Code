import sys
from collections import defaultdict

PATH = "C:/Users/Samuel Tull/Documents/NotCambridge/Code/CodingPractice/aoc20/"
DAY = X
PART = 1

data = PATH + str(DAY)
if False:  # change for test data debugging
    data = PATH + str(DAY) + "test"
if len(sys.argv) > 1:
    data = PATH + str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
# groups = data.split("\n\n")
# grid = [[x for x in line.strip()] for line in data.split("\n")]
# lines = [int(x) for x in lines]
# lines = [x.replace("-", ",").split(",") for x in lines]
# lines = [x.split(" ") for x in lines]
