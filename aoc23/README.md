# Advent of Code 2023  
Solving each morning but cannot get up at 5AM for release.  
My (mostly) raw/unmodified solutions - sometimes comment/clean after submitting.  
Each solution prints the answer to p1 then p2, unless Xp1.py exists.  

## Lessons Learnt 
### Day 3 
Searching intersections between setA and each of [setI, setJ, setK, ...].  
Better to store setB = &(I,J,K... ) for fewer comparisons 
### Day 5  
Storing intervals as [first, last] much easier to think about than [first, length].  
Eg. when adding mid we get splits [first, mid], [mid+1, last] requiring no computation of lengths.   
The choice of inclusive vs half-open slices ([first, last] or [first, last+1]) does not really matter if consistent.  
### Day 6
Turns out using brute force from p1 works for p2 (luckily solving quadratic was quick).  
If we want to count the numbers m < x < M:  
    int(M) - int(m) and floor(M) - ceil(m) + 1 are both incorrect if M/m are integers.  
    Correct to find (ceil(M) - 1) - (floor(m)+ 1) + 1, or the hacky int(M-1e-10)-int(m)  
### Day 7 
Had code for comparing poker hands already, but took longer to remove logic (flushes/ best pair/ highest card etc) than it would have done to write from scratch.  
Sort calls the key function exactly once per item.  
### Day 8
Thought I had a good optimisation - pre calculated the jumps from ..Z to ,,Z for each ..Z and starting at each 0<= i < len(instructions). Then could keep jumping past the current min until we reach a point where all states are at the same distance.  
Turns out this takes far too long and the input was designed so that LCM of A->Z works.  
This definitely doesnt work on a generic input. 
Turns out the distance x ..A to ..Z %N = 0 in every case. This is the clue I guess.  
Checking that after x more steps we are back at the same ..Z would convince us that LCM is the answer.  
### Day 12
Brute force is okay for p1 as easy to think of.  
DP helps to reduce cases.  
Tried 3 versions of DP:  
-- 12_DP_splicing: removing the "." or streak of "#" at start.  
-- 12_DP: keep track of the current index, index in the instructions, and current streak of "#".   
-- 12: Slight optimisation - doesnt count current streak - jumps ahead to end of block.  
Own cache and tuple(list) is easier than working out how to keep as str/tuple for functools.  
### Day 17   
Originally was tracking nodes with (r,c,d,cnt). Where cnt is the amount of steps taken in direction d. (see 17p1.py).  
However increases the number of open nodes by 4x! 
Better to add each poss number of steps to Q and only track new d. So state is (r,c,d).    
### Day 18 
Coordinate compression + flood fill from outside was not giving correct value.  
Decided to get some help and learnt about shoelace and pick's theorem which made it extremely simple.  
### Day 23 
BFS/DFS small difference as have to explore all paths.  
Saving states and only exploring if we reach a state in longer time doesnt speed up - most of the time if we reach it later, it will be longer d so # explored paths barely changes, and smaller than cost of comparison.  
Only solutions I have seen that are faster use dfs functions with recursion and backtracking, not sure why faster than Qs as should explore same number of paths. 
### Day 24
Becuase of how the rows are designed, and we know there is a solution we dont need to consider all rows.  Instead I consider them 2 at a time, in pairs.  
Using a fixed dx,dy we find R1, R2 for two distinct pairs (Ri is the valid rock position/velocity for pair i).   
If R1 and R2 are different then one of dx,dy is wrong.  
If they are equal then we assume we have found the valid R for all trajectories.  
I believe this is sufficient because it is extremely unlikely otherwise- there is very small possibility of the wrong dx,dy giving a valid solution that works for all lines[0-4] but fails on another. Ths is due to the problem having one valid solution, and the fact we are only exploring the integers. I am not 100% sure if I left it forever, would it find a wrong solution.  