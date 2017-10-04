def print_trace(state):
    path = []

    while state:
        path.insert(0, state.towers)
        state = state.parent

    for e in path:
        print str(e) + "->"

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

    for i in range(0,3):
        for j in range(0,3):
            if i==j:
                continue
            possible_end_state = current_state.get_next_state(i,j)

            if possible_end_state != None:
                possible_end_states.append(possible_end_state)

    return possible_end_states

