#!/usr/bin/env python3

def min_rooms(N, rooms):
    print("Initial rooms:", rooms)
    
    rooms.sort(reverse=True)
    print("Sorted rooms (desc):", rooms)

    total = 0
    count = 0

    for r in rooms:
        print("\nTaking room with capacity:", r)

        total += r
        count += 1

        print("Current total capacity:", total)
        print("Rooms used so far:", count)

        if total >= N:
            print("\nReached required capacity!")
            return count

    print("\nNot enough capacity even with all rooms")
    return -1


if __name__ == "__main__":
    N = 10
    rooms = [2, 5, 8, 1]

    result = min_rooms(N, rooms)
    print("\nFinal result:", result)

