import copy
import sys

def make_tuple(state):
    """Make Tuple for given state
       [[][][]] -> (()()()) 
    """
    a = ()
    for tower in state: 
        a = a + (tuple(tower),)
    return a

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

def get_possible_end_states(state):
    """ Get possible end states given state
        - check 6 possible future states (2 states for each peg)
    """
    possible_end_states = []

    for i in range(0,3):
        for j in range(0,3):
            if i==j:
                continue
            possible_end_state = move(i,j,state)

            if possible_end_state != None:
                possible_end_states.append(possible_end_state)

    return possible_end_states

def can_move(from_t, to_t):
    """Check if disk at top of from tower can move to to tower
       from_t (List) - tower from which disk move
       to_t (List) - tower to which disk move 
       returns boolean 
    """
    if not from_t:
        return False

    # 1. if to_tower is empty
    # 2. if disk to move is smaller
    if not to_t or from_t[0] < to_t[0]:
        return True

    return False

def move(from_num, to_num, current_state):
    """Move disk from tower to tower 
       after checking if move is possible()
    """
    if can_move(current_state[from_num], current_state[to_num]) == False:
        return

    temp_state = copy.deepcopy(current_state)
    temp_state[to_num].insert(0, temp_state[from_num][0])
    temp_state[from_num].pop(0)
    end_state = temp_state
    return end_state





