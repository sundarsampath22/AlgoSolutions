from collections import deque
from typing import List

#Given a target 4 wheel lock combination, and a list of deadends (combinations that 'break' the lock), return the minimum number of rotations to open the lock
#BFS algorithm to traverse valid next combinations (combinations that are not deadends) until either the target is reached or is deemed unreachable
class Solution:
    def open_lock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        visited = set(deadends)
        if "0000" in deadends:
            return -1
        visited.add("0000")
        queue.append("0000")
        num_moves = 0
        while queue:
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                if cur_node == target:
                    return num_moves
                for i in range(4):
                    next_node_forward = cur_node[0:i] + str((int(cur_node[i]) + 1) % 10) + cur_node[i+1:]
                    next_node_backward = cur_node[0:i] + str( (int(cur_node[i]) - 1) % 10) + cur_node[i+1:]
                    if next_node_forward not in deadends and next_node_forward not in visited:
                        queue.append(next_node_forward)
                        visited.add(next_node_forward)
                    if next_node_backward not in deadends and next_node_backward not in visited:
                        queue.append(next_node_backward)
                        visited.add(next_node_backward)
            num_moves += 1
        return -1