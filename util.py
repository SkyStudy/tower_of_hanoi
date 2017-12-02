def print_visited(visited):
    result = ""

    for e in visited: 
        result += str(e.towers) + " -> "

    print result

def print_queue(queue):
    result = ""

    for e in queue: 
        result += str(e.towers) + " ,"

    print "Queue: " + "[ " + result +  " ]"

def print_optimal_path(state):
    result = ""
    path = []

    while state:
        path.insert(0, state.towers)
        state = state.parent

    for e in path:
        result += str(e) + " -> "

    print "Start: " + result + " End"

def make_state_tuple(state):
    """
        Make Tuple out of State 
            @param - state (State)
            @return - a (Tuple)
    """
    a = ()
    for tower in state.towers: 
        a = a + (tuple(tower),)
    return a

def get_possible_end_states(current_state):
    """
        Get possible end states fron current state
            @param - current_state (State)
            @return - possible_end_states (State[])
    """
    possible_end_states = []

    for i in range(0,4):
        for j in range(0,4):
            if i==j:
                continue
            possible_end_state = current_state.get_next_state(i,j)

            if possible_end_state != None:
                possible_end_states.append(possible_end_state)

    return possible_end_states

