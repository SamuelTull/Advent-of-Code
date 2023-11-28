import sys
from collections import defaultdict, deque

DAY = 19
PART = 1

data = str(DAY)
if True:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
Blueprints = []
for line in lines:
    blueprint = [int(line.split(" ")[i]) for i in [6, 12, 18, 21, 27, 30]]
    Blueprints.append(blueprint)
"""   
--------------------
1 minute to produce
Ore
Clay
Obsidian
Geode 
--------------------
blueprint:   
ore_cost_ore,
clay_cost_ore,
obsidian_cost_ore,
obsidian_cost_clay,
geode_cost_ore,
geode_cost_obsidian,
----------------------

if T == 0,1 no more produced 
if T ==2 only make geode
if T == 3 only make obs or geode

----------------------
"""
#! INDEX + 1


def newBest(T, robots, resources):
    for idx, seen in enumerate(SEEN[T][tuple(robots)]):
        if all(resources[i] <= seen[i] for i in range(4)):
            return False
        if all(resources[i] >= seen[i] for i in range(4)):
            SEEN[T][tuple(robots)][idx] = resources
            return True
    SEEN[T][tuple(robots)].append(resources)
    return True


blueID, blueprint = 1, Blueprints[0]
oreCost = {0: blueprint[0]}  # produces 0
clayCost = {0: blueprint[1]}  # produces 1
obsCost = {0: blueprint[2], 1: blueprint[3]}  # produces 2
geoCost = {0: blueprint[4], 2: blueprint[5]}  # produces 3


newT = 24
robots = [1, 0, 0, 0]
resources = [0, 0, 0, 0]

SEEN = {T: defaultdict(list) for T in range(25)}


Q = deque([[24, robots, resources]])
best = 0
while Q:
    [T, robots, resources] = Q.pop()
    if T <= 1:
        total = resources[-1] + T * robots[-1]  # geodes + 0/1 minute of collecting
        if total > best:
            best = total
            print(best, len(Q))
        continue

    # make all geode robots...
    MaxNewGeo = min(resources[0] // geoCost[0], resources[2] // geoCost[2])
    for newGeo in range(MaxNewGeo, -1, -1):
        MaxNewObs = (
            0
            if T == 2
            else min(
                (resources[0] - newGeo * geoCost[0]) // obsCost[0],
                (resources[1]) // obsCost[1],
            )
        )
        for newObs in range(MaxNewObs, -1, -1):
            MaxNewClay = (
                0
                if T <= 3
                else (resources[0] - newGeo * geoCost[0] - newObs * obsCost[0])
                // clayCost[0]
            )
            for newClay in range(MaxNewClay, -1, -1):
                MaxNewOre = (
                    0
                    if T <= 3
                    else (
                        resources[0]
                        - newGeo * geoCost[0]
                        - newObs * obsCost[0]
                        - newClay * clayCost[0]
                    )
                    // oreCost[0]
                )
                for newOre in range(MaxNewOre, -1, -1):
                    # fmt: off
                    newResources = [0,0,0,0] 
                    newResources[0] = resources[0] - newOre*oreCost[0] - newClay*clayCost[0] - newObs * obsCost[0] - newGeo * geoCost[0]
                    assert newResources[0] >= 0
                    newResources[0]  +=  robots[0]

                    newResources[1] = resources[1] - newObs * obsCost[1] 
                    assert newResources[1] >= 0
                    newResources[1] += robots[1]
                    
                    newResources[2] = resources[2] - newGeo * geoCost[2]
                    assert newResources[2] >= 0
                    newResources[2] += robots[2]

                    newResources[3] = resources[3] + robots[3]

                    newRobots = [robots[0] +newOre ,robots[1]+newClay,robots[2]+newObs,robots[3]+newGeo ]
                    #fmt : on
                    if newBest(T-1,newRobots,newResources):
                        Q.append([T-1, newRobots, newResources])

print(best)

# if we have reached T = t and
# have less

import sys
from collections import defaultdict, deque

PATH = "C:/Users/Samuel Tull/Documents/NotCambridge/Code/CodingPractice/aoc22/"
DAY = 19
PART = 1

data = str(DAY)
if True:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
Blueprints = {}
for idx in range(len(lines)):
    blueprint = [int(lines[idx].split(" ")[i]) for i in [6, 12, 18, 21, 27, 30]]
    oreCost = {0: blueprint[0], 1: 0, 2: 0, 3: 0}  # produces 0
    clayCost = {0: blueprint[1], 1: 0, 2: 0, 3: 0}  # produces 1
    obsCost = {0: blueprint[2], 1: blueprint[3], 2: 0, 3: 0}  # produces 2
    geoCost = {0: blueprint[4], 1: 0, 2: blueprint[5], 3: 0}  # produces 3
    Blueprints[idx + 1] = [oreCost, clayCost, obsCost, geoCost]


"""   
--------------------
1 minute to produce
Ore
Clay
Obsidian
Geode 
--------------------
blueprint:   
ore_cost_ore,
clay_cost_ore,
obsidian_cost_ore,
obsidian_cost_clay,
geode_cost_ore,
geode_cost_obsidian,
----------------------

if T == 0,1 no more produced 
if T ==2 only make geode
if T == 3 only make obs or geode

----------------------
"""
#! INDEX + 1


def newBest(T, robots, resources):
    for idx, seen in enumerate(SEEN[T][tuple(robots)]):
        if all(resources[i] < seen[i] for i in range(4)):
            return False
        if all(resources[i] >= seen[i] for i in range(4)):
            SEEN[T][tuple(robots)][idx] = resources
            return True
    SEEN[T][tuple(robots)].append(resources)
    return True


for idx in Blueprints:
    oreCost, clayCost, obsCost, geoCost = costs = Blueprints[idx]
    print("Blueprint", idx)
    print(lines[idx - 1])
    print(
        "OreCost", oreCost, "ClayCost", clayCost, "ObsCost", obsCost, "GeoCost", geoCost
    )

T = 24  # time left
robots = [1, 0, 0, 0]  # robots
resources = [0, 0, 0, 0]  # current resources
building = {
    r: 0 for r in range(4)
}  # robots that are being built this turn (already paid for)
goal = None  # what robot will be built next 0,1,2,3
Q = deque([[T, robots, resources, building, goal] for goal in range(4)])

SEEN = {T: defaultdict(list) for T in range(25)}
best = 0
# start of day -> building will be None
# fmt:off
Tt = 24
while Q:
    [T, robots, resources,building,goal] = this = Q.pop()
    if T< Tt:
        Tt = T
        print(T,len(Q))
    if T <= 1: # dont build anymore
        assert T == 1, f"T={T}"
        assert building == {r:0 for r in range(4)}, f"{building}"
        total = resources[-1] +  T * robots[-1]
        if total ==9:
            pass
        if total > best:
            best = total
            print(best,len(Q))

        continue
        
    
    if T > 1 and all(resources[r] >= costs[goal][r] for r in costs[goal]):
        # can afford to build now
        building[goal] += 1
        for newgoal in range(1):
            if robots[0] + building[0] < max(cost[0] for cost in costs):
                Q.append([T, robots, [resources[r] - costs[goal][r] for r in range(4)],building.copy(),newgoal])
        for newgoal in range(1,4):
            Q.append([T, robots, [resources[r] - costs[goal][r] for r in range(4)],building.copy(),newgoal])
    else:
        # can not afford to build now
        # harvest everything, add building, next day
        newRobots =  [robots[r] + building[r] for r in range(4)]
        newResources = [resources[r]+robots[r] for r in range(4)]
        if newBest(T-1,newRobots,newResources):
            Q.append([T-1, newRobots,newResources ,{r:0 for r in range(4)},goal])
      

print(best)

# if we have reached T = t and
# have less
