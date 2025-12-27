#!/usr/bin/env python3

def min_rooms(N ,rooms):
    rooms.sort(reverse=True)
    total_aucupied = 0
    room_count = 0
    for r in rooms:
        total_aucupied += r
        room_count += 1
        if total_aucupied >= N:
            return room_count


if __name__ == "__main__":
    N = 12
    rooms = [5,8,2,3]
    result = min_rooms(N ,rooms)
    print(result)


