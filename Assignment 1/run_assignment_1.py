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
    mc = MissionariesAndCannibals(mc_initial, mc_goal)
    ep = EightPuzzle(ep_initial, ep_goal)

    mc_sa = SearchAlgorithm(mc)
    ep_sa = SearchAlgorithm(ep)

    #To activate the different experiments, just change the value of the IF statement

    #Experiment 1:
    if 0:
        print("Exp1: BFS vs DFS:\nBFS")
        mc_sa.bfs(statistics=True)
        print("DFS")
        mc_sa.dfs(statistics=True)

    #Experiment 2:
    if 0:
        print("Exp2: DFS without already visited check")
        mc_sa.dfs(statistics=True, check_visited=False, depth_limit=100)

    #Experiment 3:
    if 0:
        print("Exp3: BFS with/without check_visited\nWithout:")
        mc_sa.bfs(statistics=True, check_visited=False)
        print("With:")
        mc_sa.bfs(statistics=True, check_visited=True)

    #Experiment 4:
    if 0:
        print("Exp4: IDS")
        mc_sa.ids(statistics=True, depth_limit=25)

    #Experiment 5:
    if 0:
        print("Exp5: Greedy Search Heuristic comparison:\nh_0 (only cost):")
        ep_sa.greedy_search(heuristic=0, depth_limit=50, statistics=True)
        print("h_1 (Number of tiles out of place):")
        ep_sa.greedy_search(heuristic=1, depth_limit=50, statistics=True)
        print("h_2 (Manhattan distance):")
        ep_sa.greedy_search(heuristic=2, depth_limit=50, statistics=True)
    
    #Experiment 6:
    if 0:
        print("Exp6: A* Heuristic comparison:\nh_0 (only cost):")
        ep_sa.greedy_search(heuristic=0, depth_limit=100, statistics=True, a_star=True)
        print("h_1 (Number of tiles out of place):")
        ep_sa.greedy_search(heuristic=1, depth_limit=100, statistics=True, a_star=True)
        print("h_2 (Manhattan distance):")
        ep_sa.greedy_search(heuristic=2, depth_limit=100, statistics=True, a_star=True)


if __name__ == "__main__":
    main()