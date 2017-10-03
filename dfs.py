import copy
import sys
from dfs_bfs_util import *

def dfs(current_state, end_state, trace, level, count):
    """ Depth First Search
        given current state and end state
        level - keeps track of recursion level
        count - number of nodes visited
    """
    print "level", level
    print "State: ", current_state

    if current_state == end_state:
        print "All disks moved"
        print count
        sys.exit()

    possible_end_states = get_possible_end_states(current_state)

    for state in possible_end_states:
        if make_tuple(state) not in trace:
            trace.add(make_tuple(state))

            temp_count = count
            count += dfs(state, end_state, trace, level+1, count+1)
            count -= temp_count
            count += 1
            
            print "level", level
            # printing current_state
            # for case when we go back to parent state
            print "State: ", current_state
        else:
            continue

    return count             



