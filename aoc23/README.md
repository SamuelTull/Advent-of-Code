# Advent of Code 2023  
Solving each morning but cannot get up at 5AM for release.  
My (mostly) raw/unmodified solutions - sometimes comment/clean after submitting.  
Each solution prints the answer to p1 then p2, unless Xp1.py exists.  

## Lessons Learnt  
# Day 5  
Storing intervals as [first, last] much easier to think about than [first, length].  
Eg. when adding mid we get splits [first, mid], [mid+1, last] requiring no computation of lengths.   
The choice of inclusive vs half-open slices ([first, last] or [first, last+1]) does not really matter if consistent.  