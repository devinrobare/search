# search
Testing the speed of different searching algorithms

The was a project for school. We were required to implement 3 different searching algorithims and test their speed in different cases.
The 3 search types were linear, recursive binary, and jump search. 

Linear iterates through the list in order to find the target.

Recursive binary takes the midpoint between the highest index and the lowest index of a sorted list. If the target is lower, the midpoint becomes the new high index and the process is repeated.
If the target is higher than the midpoint, the midpoint becomes the new low index and the process repeats. This is repeated until the target is located or there are no more items in the list.

Jump search moves through a sorted list by "jumping" a certain number through the list index. In this project, it was the square root of the length of the list. 
Each jump, the number at that index is evaluated. If it's less than the target, the search jumps again. 
If it's more than the target, the search returns to the previous jump and uses a linear search to move through the index until the target is located or it is determined the target is not in the list.

I tested how each search compared when looking for a number at the beginning of a list, in the midle, at the end, and one that was not present in the list.
I used the random module to create a large list and the time.perf_counter() to calculate how long each search took for each case.

To make sure our recursive binary function was truly recursive, a recursion counter was used for testing, but I've commented that out. 
