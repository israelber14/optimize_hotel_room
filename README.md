## 🚀 Minimal Room Allocation Challenge

### 🎯 Goal

Given a required capacity $N$ and a list of room capacities, find the **minimum number of rooms** required to host at least $N$ people.

If the total capacity of all available rooms is less than $N$, return -1.

### 💡 Core Logic: The Greedy Strategy

To minimize the number of rooms chosen, we must prioritize the rooms that contribute the most to the total capacity.

**The Strategy:** Always select the room with the **largest capacity** first.

This is a classic **Greedy Algorithm** problem because the cost of selecting any room is fixed (1 room), and we only seek to minimize the count of items needed to reach a target sum.

### ⚙️ Algorithm Steps

1.  **Sort:** Sort the list of room capacities in **descending order** (largest to smallest).
2.  **Iterate and Sum:** Iterate through the sorted list, keeping track of the running `total` capacity and the `count` of rooms used.
3.  **Check Condition:**
    * If $total \ge N$, return the current `count`.
4.  **Failure:** If the entire list is traversed and $total < N$, return -1.

### 🔍 Example

| **Parameter** | **Value** |
| :--- | :--- |
| **$N$ (Required Guests)** | 10 |
| **`rooms` (Available Capacities)** | `[2, 5, 8, 1]` |

**Execution:**
1.  **Sorted Rooms:** `[8, 5, 2, 1]`
2.  **Step 1:** Pick 8. `total = 8`, `count = 1`. ($8 < 10$)
3.  **Step 2:** Pick 5. `total = 13`, `count = 2`. ($13 \ge 10$)
4.  **Result:** Return **2**.

### 💻 Implementation (Python)

```python
def min_rooms(N: int, rooms: list[int]) -> int:
    """
    Finds the minimum number of rooms needed to host N people.
    Applies a greedy approach by sorting the rooms in descending order.
    """
    # 1. Sort rooms in descending order (Greedy choice)
    rooms.sort(reverse=True)
    
    total_capacity = 0
    room_count = 0

    # 2. Iterate and check condition
    for capacity in rooms:
        total_capacity += capacity
        room_count += 1
        
        # 3. Success condition
        if total_capacity >= N:
            return room_count

    # 4. Failure condition
    return -1
