""" 
https://leetcode.com/problems/keys-and-rooms/ 

Using DFS traversal as a solution to this problem.
"""


from typing import List

def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    # all the visited rooms so far.
    visited = {0: True}

    # Using a stack to do DFS.
    stack = [0]

    # Loop as long as we have an element in the stack.
    while len(stack) != 0:
        # Get all the keys in the current room.
        keys = rooms[stack.pop()]

        # Loop over the keys in the current room 
        # to see what rooms can be visited.
        for key in keys:
            # If we haven't visited a room with this key, then:
            # 1) add it to visited set
            # 2) visit that room (add to stack)
            if key not in visited:
                visited[key] = True
                stack.append(key)

    # If length of visited set is same as length of rooms, 
    # then we have visited all the rooms.
    return len(visited) == len(rooms)

inp = [[1],[2],[3],[]]
assert canVisitAllRooms(inp), f"failed input {inp}"

inp = [[1,3],[3,0,1],[2],[0]]
assert not canVisitAllRooms(inp), f"failed input {inp}"