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