from state import State
import bfs
import dfs
import best_first_search
import sys

def main():
    state = State([[1,2,0],[0,0,3],[0,0,0]])
    state2 = State([[1,0,0],[0,2,3],[0,0,0]])
    state3 = State([[0,2,0],[0,0,3],[1,0,0]])
    state4 = State([[0,0,0],[1,2,3],[0,0,0]])
    state5 = State([[1,0,0],[0,2,0],[0,0,3]])
    state6 = State([[0,0,3],[1,2,0],[0,0,0]])

    tower = [[1,2],[3],[]]
    tower2 = [[1],[2,3],[]]
    tower3 = [[2],[3],[1]]
    tower4 = [[],[1,2,3],[]]
    tower5 = [[1],[2],[3]]
    tower6 = [[3],[1,2],[]]

    end_tower = [[],[],[1,2,3]]
    end_state = State([[0,0,0],[0,0,0],[1,2,3]])

    trace = set()



main()


