data = open("in.txt").read().strip()
lines = [x.split(" ") for x in data.split("\n")]
"""
score = {"X": 1, "Y": 2, "Z": 3}
win = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}
s = 0
for line in lines:
    s += score[line[1]] + win[line[0]][line[1]]

print(s)
"""
score = {"R": 1, "P": 2, "S": 3}
win = {"X": 0, "Y": 3, "Z": 6}
play = {
    "A": {"X": "S", "Y": "R", "Z": "P"},
    "B": {"X": "R", "Y": "P", "Z": "S"},
    "C": {"X": "P", "Y": "S", "Z": "R"},
}
s = 0
for line in lines:
    p = play[line[0]][line[1]]
    s += score[p] + win[line[1]]
print(s)
