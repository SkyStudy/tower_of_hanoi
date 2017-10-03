import copy
import sys
from dfs_bfs_util import *

def bfs(current_state, end_state, trace):
    queue = []
    queue.append(current_state)
    trace.add(make_tuple(current_state))
    node_visited_count = 0
    while queue:
        initial = queue.pop(0)
        node_visited_count+= 1
        print('Number of nodes visited: ' + str(node_visited_count))

        if initial == end_state: 
            print("All disks removed", initial)
            sys.exit()

        possible_end_states = get_possible_end_states(initial)

        for state in possible_end_states:   
            # If these moves were not visited, 
            # we add these states to visited(trace) and add them to queue
            if make_tuple(state) not in trace:
                trace.add(make_tuple(state))
                queue.append(state)
        print ("queue: ",queue)



