import copy
import operator

def make_tuple(state):
    a = ()
    for tower in state: 
        a = a + (tuple(tower),)
    return a

def dfs(current_state, end_state, stack, trace):
    print "new recursion call"
    if current_state == end_state:
        print "All disks moved"
        

    possible_end_states = get_possible_end_states(current_state)

    for state in possible_end_states:
        if make_tuple(state) not in trace:
            stack.append(state)
            trace.add(make_tuple(state))
            print state
            # print (trace)
            dfs(state, end_state, stack, trace)
        else:
            print("got in else %s", state)
            continue


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
    stack = []
    trace = set()
    stack.append(current_state)
    trace.add(make_tuple(current_state))

    dfs(current_state, end_state, stack, trace)

def num_steps():
    return

main()




