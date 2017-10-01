import copy
import sys

def make_tuple(state):
    a = ()
    for tower in state: 
        a = a + (tuple(tower),)
    return a

states = [[[1,2],[3],[]],[[1,2],[3],[]]]

def make_tuple_3d(states):
    a = set()
    for state in states:
        a.add(make_tuple(state))
    return a

def dfs(current_state, end_state, trace, level):
    print "level", level
    print "State: ", current_state

    if current_state == end_state:
        print "All disks moved"
        sys.exit()

    possible_end_states = get_possible_end_states(current_state)
    if make_tuple_3d(possible_end_states).intersection(trace) == make_tuple_3d(possible_end_states):
        # print "level", level
        # print "State: ", current_state

        # print("testing")
        return

    for state in possible_end_states:
        if make_tuple(state) not in trace:
            trace.add(make_tuple(state))
            dfs(state, end_state, trace, level+1)
        else:
            continue

    print "level", level
    print "State: ", current_state
    return             

def get_possible_end_states(current_state):
    possible_end_states = []

    for i in range(0,3):
        for j in range(0,3):
            if i==j:
                continue
            possible_end_state = move(i,j,current_state)

            if possible_end_state != None:
                possible_end_states.append(possible_end_state)

    return possible_end_states


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

current_state = [[1,2,3], [], []]
some_state = [[1,2],[3],[]]
some_state1 = [[],[3],[1,2]]


def main(): 
    current_state = [[1,2,3],[],[]]
    end_state = [[],[],[1,2,3]]
    trace = set()
    trace.add(make_tuple(current_state))

    dfs(current_state, end_state, trace, 1)

def num_steps():
    return

main()




