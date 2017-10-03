import copy

def make_tuple(state):
    """
        Make Tuple for given state
            - ex) [[][][]] -> (()()()) 
            @param: state (State)
    """
    a = ()
    for tower in state: 
        a = a + (tuple(tower),)
    return a

def can_move(from_t, to_t):
    """
        Check if disk at top of from tower can move to to tower
            @param: from_t (List) - tower from which disk move
            @param: to_t (List) - tower to which disk move 
            returns boolean 
    """

    # if from tower is empty
    if not from_t:
        return False

    # if disk to move is smaller
    if not to_t or from_t[0] < to_t[0]:
        return True

    return False


def move(from_num, to_num, current_state):
    """
        Move disk from tower to tower 
        after checking if move is possible()
            @param: from_num (Number)
            @param: to_num (Number)
            @param: current_state (2d list)
            return state(2d list)
    """
    if can_move(current_state[from_num], current_state[to_num]) == False:
        return

    temp_state = copy.deepcopy(current_state)
    temp_state[to_num].insert(0, temp_state[from_num][0])
    temp_state[from_num].pop(0)
    end_state = temp_state
    return end_state

def get_possible_end_states(state):
    """ 
        Get possible end states for given state
        - check 6 possible future states (2 states for each peg)
        - if future state is already in trace(visted before),
          we exclude it
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