import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

DAY = 23
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

#############
# ...........#
###A#C#B#A###
# D#D#B#C#
#########
#############
# .B.B.....A.#
###A#C#.#.###
# D#D#.#C#
#########
#############
# .A.......A.#
###.#B#C#.###
# D#B#C#D#
#########
#############
# ...........#
###A#B#C#A###
# A#B#C#D#
#########

# A 2238 =  15
# B 6534 = 180
# c 64 =  1000
# D 89 = 17000

# 18195 too high

#############
# ...........#
###A#C#B#A###
# D#C#B#A#
# D#B#A#C#
# D#D#B#C#
#########

#############
# BB.B......A#
###A#C#.#A###
# D#C#.#A#
# D#B#.#C#
# D#D#.#C#
#########

#############
# BB.B.A...AA#
###A#.#C#.###
# D#.#C#.#
# D#B#C#.#
# D#D#C#.#
#########


#############
# ...........#
###A#C#B#A###
# D#C#B#A#
# D#B#A#C#
# D#D#B#C#
#########
