'''
Define problem and start execution of search problems

Author: Tony Lindgren
'''

from missionaries_and_cannibals import MissionariesAndCannibals 
from eight_puzzle import EightPuzzle
from node_and_search import SearchAlgorithm

mc_initial = [[0, 0], 'r', [3, 3]] 
mc_goal = [[3, 3], 'l', [0, 0]] 

ep_initial = [7,2,4,5,0,6,8,3,1] 
ep_goal = [0,1,2,3,4,5,6,7,8] 

def main():
    #mc = MissionariesAndCannibals(mc_initial, mc_goal)
    ep = EightPuzzle(ep_initial, ep_initial)

    ep.pretty_print()

    '''
    sa = SearchAlgorithm(mc)
    print('BFS')
    bfs_gn = sa.bfs(statistics=True, verbose=False)

    print('DFS')
    dfs_gn = sa.dfs(statistics=True, verbose=False, max_depth=15, check_visited=True)

    print('IDS')
    ids_gn = sa.ids(statistics=True, verbose=False, max_depth=None, check_visited=True)'''

if __name__ == "__main__":
    main()