import copy
import sys
from state import *
from util import *

def dfs(current_state, end_state, trace, level, count):
    """ Depth First Search
        given current state and end state
        level - keeps track of recursion level
        count - number of nodes visited
    """
    print "level", level
    print "State: ", current_state.towers

    if current_state.towers == end_state.towers:
        print "All disks moved"
        print "Number of steps: " + str(count)
        sys.exit()

    possible_end_states = get_possible_end_states(current_state)

    for state in possible_end_states:
        if make_state_tuple(state) not in trace:
            trace.add(make_state_tuple(state))

            temp_count = count
            temp_level = level

            # add count for child nodes visited
            count += dfs(state, end_state, trace, temp_level+1, count+1)

            # in child nodes, count from parent nodes are double counted
            # when passed as argument of recursion function    
            count -= temp_count

            # increment count when we move to next child(in same level)
            count += 1

            print "level", level
            # printing current_state
            # for case when we go back to parent state
            print "State: ", current_state.towers
        else:
            continue

    return count             



