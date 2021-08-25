from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph
import lab_utils
import sys
import random

def main():
	# connect to GraphSpace
	graphspace = GraphSpace('aritz@reed.edu','platypus')
	nodes,edges,adj_list = lab_utils.get_graph()

    ## This line visualizes the graph, colors the terminals, and doesn't color any nodes.
	lab_utils.viz_graph(graphspace,nodes,edges,'Original Graph',{})

	## Step 1: Simulate a Random Walker
	rand_walk(nodes,edges,adj_list,graphspace)

	## Step 2: Simulate a Personalized PageRank
	pers_pagerank(nodes,edges,adj_list,graphspace,0.2)
	pers_pagerank(nodes,edges,adj_list,graphspace,0.8)

	return

def rand_walk(nodes,edges,adj_list,graphspace):
	counts = {n:0 for n in nodes}
	current = random.choice(list(nodes))
	for t in range(100000):
		counts[current]+=1
		current = random.choice(list(adj_list[current]))
	max_count = max(counts.values())
	node_colors = {}
	for n in nodes:
		d = counts[n]/max_count
		node_colors[n] = lab_utils.rgb_to_hex(1-d,0.7,1-d)
	lab_utils.viz_graph(graphspace,nodes,edges,'Random Walk',node_colors)

def pers_pagerank(nodes,edges,adj_list,graphspace,q):
	covid_nodes = lab_utils.COVID_NODES

	counts = {n:0 for n in nodes}
	current = random.choice(covid_nodes)
	for t in range(100000):
		counts[current]+=1
		val = random.random()
		if val < q:
			current = random.choice(list(adj_list[current]))
		else:
			current = random.choice(covid_nodes)
	max_count = max(counts.values())
	node_colors = {}
	for n in nodes:
		d = counts[n]/max_count
		node_colors[n] = lab_utils.rgb_to_hex(1-d,0.7,1-d)
	lab_utils.viz_graph(graphspace,nodes,edges,'Personalized PageRank (q=%.2f)' % (q),node_colors)

if __name__ == '__main__':
	main()
