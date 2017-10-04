import sys
import math
from state import *
from util import *

def calc_h(current_state, end_state):
    """
       Returns heuristic distance (Euclidean) 
       from current state to end state
    """
    current_array = current_state.towers
    end_array = end_state.towers
    cum = 0
    for i in range(0, len(current_array)):
        for j in range(0, len(current_array[0])):
            cum += (current_array[i][j] - end_array[i][j])**2
    heu_dist = math.sqrt(cum)
    return heu_dist


def best_first_search(initial_state, end_state, trace):
    """
        Best first search         
    """
    prqueue = []
    prqueue.append(initial_state)
    trace.add(make_state_tuple(initial_state))
    node_visited_count = 0
    visited = []

    while prqueue:
        current = prqueue.pop(0)
        visited.append(current)
        node_visited_count += 1

        if current.towers == end_state.towers: 
            print
            print "We have reached end state!!"
            print
            print 'Number of nodes visited in search: ' + str(node_visited_count)
            print " - number of nodes in best first search"
            print " - this is not equal to number of nodes in optimal path"
            print 
            print "Nodes visited in search: "
            print
            print_visited(visited)
            print
            print "Optimal path"
            print 
            print_optimal_path(current)
            sys.exit()

        possible_end_states = get_possible_end_states(current)

        for state in possible_end_states:
            # If these moves were not visited, 
            # we add these states to visited(trace) and add them to queue
            if make_state_tuple(state) not in trace:
                trace.add(make_state_tuple(state))
                state.parent = current
                prqueue.append(state)

            # calc g
            state.cost += 1
            # calc h
            state.cost += calc_h(state, end_state)
        
        prqueue.sort(key=lambda state: state.cost)

        a = "Prqueue: "
        for element in prqueue:
            a += str(element.towers) + ", "

        print a

