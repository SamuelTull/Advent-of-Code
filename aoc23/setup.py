import sys
import os
import shutil


if len(sys.argv) == 1:
    day = input("Day? ")
else:
    day = sys.argv[1]

if not os.path.exists(f"{day}.py"):
    print(f"Copying day X to {day}")
    with open("X.py") as X, open(f"{day}.py", "w") as f:
        f.write(X.read().replace("X", day))
    open(f"{day}.txt", "w").close()
    open(f"{day}test.txt", "w").close()
else:
    assert not os.path.exists(f"{day}p1.py"), f"{day}p1.py already exists"
    print(f"Backup {day}.py to {day}p1.py")
    shutil.copy(f"{day}.py", f"{day}p1.py")
