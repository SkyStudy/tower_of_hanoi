import copy
import sys
from state import *
from util import *

def bfs(current_state, end_state, trace):
    queue = []
    queue.append(current_state)
    trace.add(make_state_tuple(current_state))
    node_visited_count = 0
    visited = []

    while queue:
        current = queue.pop(0)
        visited.append(current)
        node_visited_count += 1

        if current.towers == end_state.towers: 
            print
            print "We have reached end state!!"
            print
            print 'Number of nodes visited in search: ' + str(node_visited_count)
            print " - number of nodes visited in breadth first search"
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
                queue.append(state)

        print_queue(queue)
        print

