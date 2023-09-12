'''
Define problem and start execution of search problems

Author: Tony Lindgren
'''

from missionaries_and_cannibals import MissionariesAndCannibals 
from node_and_search import SearchAlgorithm

init_state = [[0, 0], 'r', [3, 3]] 
goal_state = [[3, 3], 'l', [0, 0]] 

def main():
    mc = MissionariesAndCannibals(init_state, goal_state)

    
    sa = SearchAlgorithm(mc)
    print('BFS')
    bfs_gn = sa.bfs(statistics=True, verbose=False)

    print('DFS')
    dfs_gn = sa.dfs(statistics=True, verbose=False, max_depth=15, check_visited=True)

    print('IDS')
    ids_gn = sa.ids(statistics=True, verbose=False, max_depth=None, check_visited=True)

if __name__ == "__main__":
    main()