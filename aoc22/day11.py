#
# lambda old,op = eval(op)


# with open("test.txt") as f:
with open("in.txt") as f:
    data = f.read().strip()
lines = data.split("\n\n")  # each line element of list
lines = [[x.replace(",", "").strip().split(" ") for x in x.split("\n")] for x in lines]

op_map = {
    "old": "old",
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
}
monkeys = []
for _, starting, operation, test, true_, false_ in lines:
    monkey = {"items": [], "op": [], "inspections": 0}
    for x in starting[2:]:
        monkey["items"].append(int(x))
    for x in operation[3:]:
        monkey["op"].append(op_map[x] if x in op_map else int(x))
    monkey["test"] = int(test[-1])
    monkey["true"] = int(true_[-1])
    monkey["false"] = int(false_[-1])
    monkeys.append(monkey)


def solution(rounds, P2=False, mult=1):
    for r in range(rounds):
        for monkey in monkeys:
            while monkey["items"]:
                monkey["inspections"] += 1
                x = monkey["items"].pop(0)
                y = x if monkey["op"][2] == "old" else monkey["op"][2]
                if P2:
                    z = (monkey["op"][1](x, y)) % mult
                else:
                    z = (monkey["op"][1](x, y)) // 3
                throw = monkey["true"] if z % monkey["test"] == 0 else monkey["false"]
                monkeys[throw]["items"].append(z)

    insp = sorted([monkey["inspections"] for monkey in monkeys], reverse=True)
    return insp[0] * insp[1]


P2 = True
if not P2:
    print("p1", solution(20))
else:
    mult = 1
    for monkey in monkeys:
        mult *= monkey["test"]
    print("p2", solution(10_000, True, mult))
