import sys
import os


def newDay(day):
    with open("X.py") as f:
        old = f.read().strip()

    new = ""
    for line in old.split("\n"):
        if line == "DAY = X":
            new += "DAY = " + day
        else:
            new += line
        new += "\n"

    with open(day + ".py", "w") as f:
        f.write(new)

    with open(day + ".txt", "w") as f:
        f.write("")

    with open(day + "test.txt", "w") as f:
        f.write("")


def part2(day):
    assert not os.path.exists(day + "p2.py"), day + "p2.py already exists"
    with open(day + ".py") as f:
        old = f.read().strip()

    new = ""
    for line in old.split("\n"):
        if line == "PART = 1":
            new += "PART = 2"
        else:
            new += line
        new += "\n"

    with open(day + "p2.py", "w") as f:
        f.write(new)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        day = input("Day? ")
    else:
        day = sys.argv[1]

    if not os.path.exists(day + ".py"):
        print(f"Copying day X to {day}")
        newDay(day)
    else:
        print(f"Copying {day}.py to {day}p2.py")
        part2(day)
