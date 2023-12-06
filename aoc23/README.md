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
