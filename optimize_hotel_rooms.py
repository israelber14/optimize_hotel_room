#!/usr/bin/env python3
### ⚙️ Algorithm Steps

##Sort the list of room capacities in **descending order** (largest to smallest).
## Iterate and Sum:** Iterate through the sorted list, keeping track of the running `total` capacity and the `count` of rooms used.
## Check Condition:**
## If $total \ge N$, return the current `count`.
##Failure:** If the entire list is traversed and $total < N$, return -1
def min_rooms(N , rooms):
    rooms.sort(reverse=True)
    total = 0 
    count = 0 

    for r in rooms:
        total += r
        count += 1
        if total >= N:
            return count

    return -1

if __name__ == "__main__":
    # Example usage
    N = 10
    rooms = [2, 5, 8, 1]
    result = min_rooms(N, rooms)
    print("Minimum number of rooms needed:", result)
