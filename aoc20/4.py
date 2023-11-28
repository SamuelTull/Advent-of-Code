import sys
from collections import defaultdict

DAY = 4
PART = 2
data = str(DAY)
if len(sys.argv) > 1:
    if sys.argv[1] in ["0", "test"]:
        data = str(DAY) + "test"
    else:
        data = str(DAY) + sys.argv[1]

with open(data + ".txt") as f:
    data = f.read().strip()

groups = data.split("\n\n")

p1 = 0
p2 = 0
for group in groups:
    lines = group.split("\n")
    lst = {}
    for line in lines:
        infos = line.split()
        for info in infos:
            i, num = info.split(":")
            lst[i] = num.strip()
    if all(x in lst for x in {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}):
        p1 += 1
    if not all(x in lst for x in {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}):
        continue
    if not 1920 <= int(lst["byr"]) <= 2002:
        continue
    if not 2010 <= int(lst["iyr"]) <= 2020:
        continue
    if not 2020 <= int(lst["eyr"]) <= 2030:
        continue
    num, unit = lst["hgt"][:-2], lst["hgt"][-2:]
    if not unit in ["cm", "in"]:
        continue
    if unit == "cm" and not 150 <= float(num) <= 193:
        continue
    if unit == "in" and not 59 <= float(num) <= 76:
        continue
    if lst["hcl"][0] != "#":
        continue
    if lst["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        continue
    passID = lst["pid"]
    if len(passID) != 9:
        continue
    if not all(i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] for i in passID):
        continue
    p2 += 1
print("P1", p1)
print("P2", p2)
