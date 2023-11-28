import sys
import os


def newDay(day):
    OLD = "X.py"

    with open(PATH + OLD) as f:
        old = f.read().strip()

    new = ""
    for line in old.split("\n"):
        if line == "DAY = X":
            new += "DAY = " + day
        else:
            new += line
        new += "\n"

    with open(PATH + day + ".py", "w") as f:
        f.write(new)

    with open(PATH + day + ".txt", "w") as f:
        f.write("")

    with open(PATH + day + "test.txt", "w") as f:
        f.write("")


def part2(day):
    assert not os.path.exists(PATH + day + "p2.py"), day + "p2.py already exists"
    with open(PATH + day + ".py") as f:
        old = f.read().strip()

    new = ""
    for line in old.split("\n"):
        if line == "PART = 1":
            new += "PART = 2"
        else:
            new += line
        new += "\n"

    with open(PATH + day + "p2.py", "w") as f:
        f.write(new)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        day = input("Day? ")
    else:
        day = sys.argv[1]

    PATH = "C:/Users/Samuel Tull/Documents/NotCambridge/Code/CodingPractice/Aoc20/"

    if not os.path.exists(PATH + day + ".py"):
        print(f"Copying day X to {day}")
        newDay(day)
    else:
        print(f"Copying {day}.py to {day}p2.py")
        part2(day)
