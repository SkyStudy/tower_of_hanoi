import copy
import sys
import dfs_bfs_util

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


# check if disk at top of from tower can move to to tower
# from_t (List) - tower from which disk move
# to_t (List) - tower to which disk move 
# returns boolean 
def can_move(from_t, to_t):
    if not from_t:
        return False

    # 1. if to_tower is empty
    # 2. if disk to move is smaller
    if not to_t or from_t[0] < to_t[0]:
        return True

    return False

def move(from_num, to_num, current_state):
    if can_move(current_state[from_num], current_state[to_num]) == False:
        return

    temp_state = copy.deepcopy(current_state)
    temp_state[to_num].insert(0, temp_state[from_num][0])
    temp_state[from_num].pop(0)
    end_state = temp_state
    return end_state

