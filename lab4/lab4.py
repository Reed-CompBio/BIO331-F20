from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph
import lab_utils
import sys

def main():
	# connect to GraphSpace
	graphspace = GraphSpace('YOUR_EMAIL','YOUR_PASSWORD')
	nodes,edges,terminals,adj_list = lab_utils.get_graph()

    ## This line visualizes the graph, colors the terminals, and doesn't color any edges.
	lab_utils.viz_graph(graphspace,nodes,edges,terminals,[],'Original Graph')

	## Step 1. Compute Metric Closure of Graph

	## Step 2. Compute Min Spanning Tree (MST) on Metric Closure

	## Step 3. Expand MST Edges

    return


if __name__ == '__main__':
	main()
