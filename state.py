import sys
import copy

class State:

    def __init__(self, towers):
        # towers = 2d array of size 3
        # [[],[],[]]
        self.towers = towers
        self.parent = None
        self.cost = 0

    def can_move(self, from_index, to_index):
        from_tower = self.towers[from_index]
        to_tower = self.towers[to_index]

        if self.is_empty(from_tower) is True:
            return False
            
        if self.top(from_tower) < self.top(to_tower) or self.is_empty(to_tower):
            return True

        return False

    def is_empty(self, tower):
        return all(v == 0 for v in tower)

    def top(self, tower):
        for disk in tower:
            if disk != 0:
                return disk
        return 0 
        # returns none if next state is not available
    def get_next_state(self, from_index, to_index):

        if self.can_move(from_index, to_index) == False:
            return

        next_state = copy.deepcopy(State(self.towers))

        from_tower = next_state.towers[from_index]
        to_tower = next_state.towers[to_index]

        top_from_index = self.top(from_tower)-1
        top_to_index = self.top(to_tower)-1

        # set to_tower value
        next_state.towers[to_index][top_from_index] = self.top(from_tower) 

        # set from_tower value
        next_state.towers[from_index][top_from_index] = 0

        return next_state    
