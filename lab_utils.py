from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph
import sys
import time

'''
Get example undirected graph.
'''
def get_graph():
	nodes = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
	terminals = ['b','d','i','k']
	edges = [['a','b'],['a','c'],['b','c'],['b','e'],['b','d'],
		['d','e'],['e','c'],['c','h'],['e','g'],['c','g'],['g','f'],
		['h','k'],['g','k'],['k','j'],['j','i'],['h','i'],['i','l'],
		['l','j'],['l','m']]
	adj_list = {n:set() for n in nodes}
	for u,v in edges:
		adj_list[u].add(v)
		adj_list[v].add(u)

	print('%d nodes, %d terminals, and %d edges' % (len(nodes),len(terminals),len(edges)))
	return nodes,edges,terminals,adj_list

'''
Given a source node u and a target node v and a dictionary pi of predecessors,
returns the shortest path from u to v.  If there are multiple paths, only
one is returned.  Returned path is a list of nodes.
'''
def get_path(u,v,pi):
	current = v # start at the END of the path.
	path = [] # empty path
	while current != u: # if we're not at the START of the path...
		path = [current] + path ## add element to beginning of path
		current = pi[current] ## update current to be the predecessor.
	path = [u] + path ## add first node to beginning of path
	return path

'''
Min spanning tree function. This function is intentionally obtuse,
wait for the asynchronous activity to learn more about this.
'''
def min_spanning_tree(nodes,weighted_edges):
	F = []
	edges = []
	for n in nodes:
		F.append([n])
	for u,v,w in sorted(weighted_edges, key=lambda x:x[2]):
		T1 = 0
		T2 = 0
		for i in range(len(F)):
			if u in F[i]:
				T1=i
			if v in F[i]:
				T2=i
		if T1!=T2:
			edges.append([u,v])
			T3 = F[T1] + F[T2]
			if T1 < T2:
				F[T1] = T3
				F.pop(T2)
			else:
				F[T2] = T3
				F.pop(T1)
	return edges

'''
Posts a graph to GraphSpace. Inputs:
graphspace - GraphSpace client (what you passed your username & password in as)
nodes - list/set of nodes
edges - list of two-element edges (three-element lists if weighted, see below)
terminals - list/set of terminal nodes (subset of nodes)
tree - list of tree edges (subset of edges)
title - title of your graph.
weighted - weighted (default False). If True, then edges are three-element lists.
'''
def viz_graph(graphspace,nodes,edges,terminals,tree,title,weighted=False):
	nonterminal_color = '#FFFFFF'
	terminal_color = '#63ADA1'
	node_shape = 'roundrectangle'

	nontree_edge_color = '#000000'
	tree_edge_color = '#63ADA1'

	G = GSGraph()
	G.set_name(title + ' ' + str(time.time()))  ## this name is timestamped
	G.set_tags(['Lab 4']) ## tags help you organize your graphs

	for n in nodes:
		G.add_node(n,label=n)
		if n in terminals:
			G.add_node_style(n,color=terminal_color,shape=node_shape,height=30,width=30)
		else:
			G.add_node_style(n,color=nonterminal_color,shape=node_shape,height=30,width=30)
	if weighted:
		for u,v,w in edges:
			G.add_edge(u,v,popup='weight %d' % (w))
			if [u,v,w] in tree or [v,u,w] in tree:
				G.add_edge_style(u,v,color=tree_edge_color,width=w)
			else:
				G.add_edge_style(u,v,color=nontree_edge_color,width=w)
	else:
		for u,v in edges:
			G.add_edge(u,v)
			if [u,v] in tree or [v,u] in tree:
				G.add_edge_style(u,v,color=tree_edge_color,width=4)
			else:
				G.add_edge_style(u,v,color=nontree_edge_color,width=2)

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
