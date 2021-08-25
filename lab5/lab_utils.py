from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph
import sys
import time

## global variable of COVID-19 nodes.
COVID_NODES = ["E","M","N","NSP1","NSP10","NSP12","NSP13","NSP14","NSP15",\
"NSP16","NSP2","NSP3","NSP4","NSP5","NSP6","NSP7","NSP8","NSP9","ORF14",\
"ORF3A","ORF3B","ORF6","ORF7A","ORF7B","ORF8","ORF9B","S"]

'''
Get example undirected graph.
'''
def get_graph():
	nodes = set()
	edges = []
	with open('proximity-network.txt') as fin:
		for line in fin:
			row = line.strip().split()
			nodes.add(row[0])
			nodes.add(row[1])
			edges.append([row[0],row[1]])
	adj_list = {n:set() for n in nodes}
	for u,v in edges:
		adj_list[u].add(v)
		adj_list[v].add(u)

	print('%d nodes and %d edges' % (len(nodes),len(edges)))
	return nodes,edges,adj_list

'''
Posts a graph to GraphSpace. Inputs:
graphspace - GraphSpace client (what you passed your username & password in as)
nodes - list/set of nodes
edges - list of two-element edges (three-element lists if weighted, see below)
title - title of your graph.
node_colors - dictionary of HTML color codes (or colors) for every node.
Note: COVID-19 nodes are overwritten to be red diagonals.
'''
def viz_graph(graphspace,nodes,edges,title,node_colors):
	G = GSGraph()
	G.set_name(title + ' ' + str(time.time()))  ## this name is timestamped
	G.set_tags(['Lab 5']) ## tags help you organize your graphs

	for n in nodes:
		G.add_node(n,label=n)
		if n in COVID_NODES:  ## COVID nodes are always red diamonds.
			G.add_node_style(n,color=node_colors.get(n,'#FFFFFF'),shape='diamond',border_color='#FF0000',border_width=4,height=40,width=60)
		else:
			G.add_node_style(n,color=node_colors.get(n,'#FFFFFF'),shape='roundrectangle',height=30,width=60)
	for u,v in edges:
		G.add_edge(u,v)
		G.add_edge_style(u,v,width=2)

	post(G,graphspace)
	print('Done posting',title)
	return

'''
Posts the graph G to GraphSpace. Copied from Lab 2.
'''
def post(G,gs):
	try:
		graph = gs.update_graph(G)
	except:
		graph = gs.post_graph(G)
	return graph



'''
Returns the hexadecimal color code when given three channels
for red, green, and blue between 0 and 1.  Copied from Lab 3.
'''
def rgb_to_hex(red,green,blue): # pass in three values between 0 and 1
  maxHexValue= 255  ## max two-digit hex value (0-indexed)
  r = int(red*maxHexValue)    ## rescale red
  g = int(green*maxHexValue)  ## rescale green
  b = int(blue*maxHexValue)   ## rescale blue
  RR = format(r,'02x') ## two-digit hex representation
  GG = format(g,'02x') ## two-digit hex representation
  BB = format(b,'02x') ## two-digit hex representation
  return '#'+RR+GG+BB
