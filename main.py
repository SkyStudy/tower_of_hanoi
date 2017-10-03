from state import State
import sys

def main():
    state = State([[1,2,0],[0,0,3],[0,0,0]])
    #state2 = State([[1,2,0],[0,0,3],[0,0,0]])
    state3 = State([[1,2,0],[0,0,3],[0,0,0]])
    state4 = State([[1,2,0],[0,0,3],[0,0,0]])
    #state5 = State([[0,0,0],[0,0,0],[0,0,0]])
    state6 = State([[0,0,0],[0,0,0],[0,0,0]])

    state1 = State([[0,0,0],[0,0,0],[0,0,0]])

    new_state = state.get_next_state(1,2)
    #new_state2 = state2.get_next_state(1,0)
    new_state3 = state3.get_next_state(0,2)
    new_state4 = state4.get_next_state(0,1)
    #new_state5 = state5.get_next_state(1,0)
    #new_state6 = state6.get_next_state(1,2)
    print("state", state.towers)
    print new_state.towers
    #print("state", state.towers)
    #print new_state2.towers
    print("state", state.towers)
    print new_state3.towers
    print("state", state.towers)
    print new_state4.towers
    #print("state", state1.towers)
    #print new_state5.towers
    #print("state", state1.towers)
    #print new_state6.towers


main()


