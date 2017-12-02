from state import *
from bfs import *
from dfs import *
from best_first_search import *

def main():
    sys.setrecursionlimit(150000)

    size = 7

    zero = [0] * size
    tower = range(1, size + 1)

    state = State([tower[:],zero[:],zero[:],zero[:]])
    # state2 = State([[1,0,0],[0,2,3],[0,0,0]])
    # state3 = State([[0,2,0],[0,0,3],[1,0,0]])
    # state4 = State([[0,0,0],[1,2,3],[0,0,0]])
    # state5 = State([[1,0,0],[0,2,0],[0,0,3]])
    # state6 = State([[0,0,3],[1,2,0],[0,0,0]])
    end_state = State([zero[:],zero[:],zero[:],tower[:]])

    trace = set()
    trace2 = set()
    trace3 = set()

    # bfs(state, end_state, trace)
    # best_first_search(state, end_state, trace2)
    dfs(state, end_state, trace3, 0, 1)

    

main()


