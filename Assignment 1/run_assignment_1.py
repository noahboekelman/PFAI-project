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
    bfs_gn = sa.bfs(statistics=True, verbose=True)

    print('DFS')
    dfs_gn = sa.dfs(statistics=True, verbose=True, max_depth=12)

    print('IDFS')
    idfs_gn = sa.idfs(statistics=True)

if __name__ == "__main__":
    main()