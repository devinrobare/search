import random
import time
import math
from sys import setrecursionlimit
#from recursioncounter import RecursionCounter

'''Implement the following search algorithms as predicate (boolean) functions. By definition,
this means they return True only if the start_target is in the list, False otherwise. Assume the
start_target type is integer, and the list contains only integers. Use of "lyst" as an identifier is NOT
a typo since "list" is a Python type. For all algorithms, the list must be sorted'''



def linear_search(lyst, target):
    if isinstance(target, int) and all(isinstance(x, int) for x in lyst):
        for i in range(len(lyst)):
            if lyst[i] == target:
                return(True)
        else:
            return(False)
    else:
        raise ValueError("Target and lyst elements must be integers!") 
        

def recursive_binary_search(lyst, target):
    if isinstance(target, int) and all(isinstance(x, int) for x in lyst):
        low_index = lyst[0]
        high_index = lyst[-1]
        return recursive_binary_search_helper(lyst, low_index, high_index, target)
    else:
        raise ValueError("Target and lyst elements must be integers!")



def recursive_binary_search_helper(lyst, low_index, high_index, target):
    #RecursionCounter()
    if len(lyst) == 0:
        return False
    if len(lyst) == 1 and lyst[0] != target:
        return False
    low_index = lyst[0]
    high_index = lyst[-1]
    midpoint = (len(lyst) // 2)
    if target == lyst[midpoint]:
        return True
    elif lyst[midpoint] < low_index or lyst[midpoint] > high_index:
        return False
    elif target < lyst[midpoint]:
        lyst = lyst[0:midpoint]
        return recursive_binary_search_helper(lyst, low_index, high_index, target)
    elif target > lyst[midpoint]:
        lyst = lyst[midpoint:]
        return recursive_binary_search_helper(lyst, low_index, high_index, target)
    else:
        return False


def jump_search(lyst, target):
    if isinstance(target, int) and all(isinstance(x, int) for x in lyst):
        target = int(target)
        jump = int(math.sqrt(len(lyst)))
        last_jump = 0
        if lyst[jump] == target:
            return(True)
        elif lyst[jump] != target:
            while lyst[int(min(jump, len(lyst))-1)] < target:
                last_jump = jump
                jump += int(math.sqrt(len(lyst)))
            if jump >= len(lyst):
                for i in range(last_jump - int(math.sqrt(len(lyst))), len(lyst)):
                    if lyst[i] == target:
                        return(True)
                else: 
                    return(False)
            elif lyst[jump] > target:
                for i in range(last_jump, jump):
                    if lyst[i] == target:
                        return(True)
                else: 
                    return(False)
            else:
                return(False)
        else:
            return(False)
    else:
        raise ValueError("Target and lyst elements must be integers!")    


'''Create a non-interactive main function that runs each each search, times each run, and
reports the results to the console. * Use large array size, typically in the range 1,000,000 -
10,000,000 values'''

        
def main():

    '''Use the functions in the random module for generating lists of numbers.

    random.seed(seed_value): The seed can be any integer value, but should be the same
    each time so that you can duplicate results for testing and debugging.

    random.sample(population, k): generates k-length random sequence drawn from
    population without replacement. Example: sample(range(10000000), k=60)
    Use a built-in sort function to sort the list after it is generated.
    '''
    print("Creating a sorted array of 1000000")
    print("Finished creating a sorted array of 1000000\n")
    random.seed(3)
    lyst = random.sample(range(10000000), k=1000000)
    lyst = sorted(lyst)
    setrecursionlimit(10**6)

    '''print(lyst[-2])
    print(lyst[3])
    print(lyst[500550])'''

    '''For all 3 algorithms, report the following results:
    1. the first element of the sorted array
    2. a number at the middle of the sorted array
    3. a number at the end of the sorted array
    4. a number NOT in the array (try -1)'''

    #search for a start number
    start_target = 12  
    lin_start_timer = time.perf_counter()
    lin_start =linear_search(lyst, start_target)
    lin_start_time = time.perf_counter() - lin_start_timer

    rec_start_timer = time.perf_counter()
    rec_start = recursive_binary_search(lyst, start_target)
    rec_start_time = time.perf_counter() - rec_start_timer

    jum_start_timer = time.perf_counter()
    jum_start = jump_search(lyst, start_target)
    jum_start_time = time.perf_counter() - jum_start_timer

    #search for a middle number
    mid_target = 5007039
    lin_mid_timer = time.perf_counter()
    lin_mid = linear_search(lyst, mid_target)
    lin_mid_time = time.perf_counter() - lin_mid_timer

    rec_mid_timer = time.perf_counter()
    rec_mid = recursive_binary_search(lyst, mid_target)
    rec_mid_time = time.perf_counter() - rec_mid_timer

    jum_mid_timer = time.perf_counter()
    jum_mid = jump_search(lyst, mid_target)
    jum_mid_time = time.perf_counter() - jum_mid_timer

    #search for a end number
    end_target = 9999996
    lin_end_timer = time.perf_counter()
    lin_end = linear_search(lyst, end_target)
    lin_end_time = time.perf_counter() - lin_end_timer

    rec_end_timer = time.perf_counter()
    rec_end = recursive_binary_search(lyst, end_target)
    rec_end_time = time.perf_counter() - rec_end_timer

    jum_end_timer = time.perf_counter()
    jum_end = jump_search(lyst, end_target)
    jum_end_time = time.perf_counter() - jum_end_timer

    #search for a number not on the list
    not_target = -1
    lin_not_timer = time.perf_counter()
    lin_not = linear_search(lyst, not_target)
    lin_not_time = time.perf_counter() - lin_not_timer

    rec_not_timer = time.perf_counter()
    rec_not = recursive_binary_search(lyst, not_target)
    rec_not_time = time.perf_counter() - rec_not_timer

    jum_not_timer = time.perf_counter()
    jum_not = jump_search(lyst, not_target)
    jum_not_time = time.perf_counter() - jum_not_timer

    '''Use the time.perf_counter() 
    Your timing results should be to at least 2 significant digits.'''

    print(f"Searching for a number at the start of the array"
    f"\n\tlinear_search() returned {lin_start} in {lin_start_time:.7f} seconds" 
    f"\n\trecursive_binary_search() returned {rec_start} in {rec_start_time:.7f} seconds" 
    f"\n\tjump_search() returned {jum_start} in {jum_start_time:.7f} seconds")
    
    print(f"\nSearching for a number in the middle of the array"
    f"\n\tlinear_search() returned {lin_mid} in {lin_mid_time:.7f} seconds"
    f"\n\trecursive_binary_search() returned {rec_mid} in {rec_mid_time:.7f} seconds"
    f"\n\tjump_search() returned {jum_mid} in {jum_mid_time:.7f} seconds")

    print(f"\nSearching for a number at the end of the array"
    f"\n\tlinear_search() returned {lin_end} in {lin_end_time:.7f} seconds"
    f"\n\trecursive_binary_search() returned {rec_end} in {rec_end_time:.7f} seconds"
    f"\n\tjump_search() returned {jum_end} in {jum_end_time:.7f} seconds")

    print(f"\nSearching for a number in the middle of the array"
    f"\n\tlinear_search() returned {lin_not} in {lin_not_time:.7f} seconds"
    f"\n\trecursive_binary_search() returned {rec_not} in {rec_not_time:.7f} seconds"
    f"\n\tjump_search() returned {jum_not} in {jum_not_time:.7f} seconds")

    '''All searches need to validate the “type” of data passed in. The start_target must be an integer and
    the elements of lyst must also be integers. If not, the search should raise a ValueError
    exception.

    linear_search(lyst, "cat")
    recursive_binary_search(lyst, "cat")
    jump_search(lyst, "cat")'''



if __name__ == "__main__":
    main()
    
