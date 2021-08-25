from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph
import lab_utils
import sys

def main():
	# connect to GraphSpace
	graphspace = GraphSpace('YOUR_EMAIL','YOUR_PASSWORD')
	nodes,edges,adj_list = lab_utils.get_graph()

    ## This line visualizes the graph, colors the terminals, and doesn't color any nodes.
	lab_utils.viz_graph(graphspace,nodes,edges,'Original Graph',{})

	## Step 1: Simulate a Random Walker

	## Step 2: Simulate a Personalized PageRank

	return


if __name__ == '__main__':
	main()
