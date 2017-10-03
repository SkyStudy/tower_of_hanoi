import copy
import sys
import math
from state import State


# Make Tuple out of State 
# - this is for pushing 
# @param - state (State)
# @return - a (Tuple)
def make_tuple(state):
    a = ()
    for tower in state.towers: 
        a = a + (tuple(tower),)
    return a

# Get possible end states fron current state
# @param - current_state (State)
# @return - possible_end_states (State[])
def get_possible_end_states(current_state):
    possible_end_states = []

    for i in range(0,3):
        for j in range(0,3):
            if i==j:
                continue
            possible_end_state = current_state.get_next_state(i,j)

            if possible_end_state != None:
                possible_end_states.append(possible_end_state)

    return possible_end_states

# def calc_cost():
#     cost = calc_g() + calc_h()
#     return cost

# Returns heuristic distance from current state to end state
def calc_h(current_state, end_state):
    current_array = current_state.towers
    end_array = end_state.towers
    cum = 0
    for i in range(0, len(current_array)):
        for j in range(0, len(current_array[0])):
            cum += (current_array[i][j] - end_array[i][j])**2
    heu_dist = math.sqrt(cum)
    return heu_dist

def best_first_search(current_state, end_state, trace):
    prqueue = []
    prqueue.append(current_state)
    trace.add(make_tuple(current_state))
    node_visited_count = 0
    while prqueue:
        initial = prqueue.pop(0)
        node_visited_count+= 1
        print('Number of nodes visited: ' + str(node_visited_count))

        if initial.towers == end_state.towers: 
            print("All disks removed", initial)
            sys.exit()

        possible_end_states = get_possible_end_states(initial)
        possible_end_states = sort_by_cost(possible_end_states, end_state)


        for state in possible_end_states:   
            # If these moves were not visited, 
            # we add these states to visited(trace) and add them to queue
            if make_tuple(state) not in trace:
                trace.add(make_tuple(state))
                prqueue.append(state)
        print ("queue: ",prqueue)

def sort_by_cost(states, end_state):
    for state in states:
        state.cost = calc_h(state, end_state)

    sorted_states = states.sort(key=lambda state: state.cost)

    return sorted_states

def main(): 
    current_state = [[1,2,3],[0,0,0],[]]
    end_state = [[],[],[1,2,3]]
    queue = []
    states = []
    trace = set()
    trace.add(make_tuple(current_state))

    bfs(current_state, end_state, trace)


# main()
