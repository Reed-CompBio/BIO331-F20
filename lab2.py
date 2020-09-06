## Lab2 - Animal Social Network Visualization
from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph
import sys
import time

def main():

	## connect to GraphSpace (Task C)
	#graphspace = GraphSpace('YOUR EMAIL','YOUR PASSWORD')

	## post test graph (Task D)
	#post_test_graph(graphspace)

	## post dolphin graph (Tesk E)
	#post_dolphin_graph(graphspace)

	return # done with main() function

def post_test_graph(graphspace):
	## create a toy graph

	## create a GraphSpace object G with nodes & edges

	## post the GraphSpace object G
	# graph = post(G,graphspace)

	print('done posting test graph')
	return # done with post_test_graph()

def post_dolphin_graph(graphspace):
	## read dolphin edges and dolphin metadata

	## greate a GraphSpace object G with nodes & edges

	## post the GraphSpace object G
	#graph = post(G,graphspace)

	## when ready, share graph with the group
	#share(graph,graphspace)

	print('done posting dolphin graph')
	return # done with post_dolphin_graph()

## Post the graph G to GraphSpace.
## If the graph already exists, update it.
## Otherwise, add ("post") it.
def post(G,gs):
	try:
		graph = gs.update_graph(G)
	except:
		graph = gs.post_graph(G)
	return graph

## Share the graph variable returned by post() with the BIO331F20 group.
def share(graph,gs):
	gs.share_graph(graph=graph,group_name='BIO331F20')
	return

## Function to read a list of strings from a single-column input file.
## inputs: infile (string)
## returns: list of strings
def read_onecol(infile):
	elements = []
	with open(infile) as fin:
		for line in fin:
			elements.append(line.strip())
	return elements

## Function to read a list of lists from a tab-delimited multi-column input file.
## inputs: infile (string)
## returns: list of lists, where each element is
## a list of strings from each line in the file.
def read_multicols(infile):
	elements = []
	with open(infile) as fin:
		for line in fin:
			elements.append(line.strip().split('\t'))
	return elements

## Leave this at the bottom of the file.
if __name__ == '__main__':
	main()
