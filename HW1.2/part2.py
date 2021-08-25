## Module 1 Part 2
## Animal Network Visualization
## Fall 2020

def main():
	"""
	Main function for reading, posting, and annotating animal social networks.
	"""

	return

def read_matrix(filename):
	"""
	Reads a graph provided as a tab-delimited matrix.
	"""

	return ## nodes and edges

def read_info(filename):
	"""
	Reads the badger information.
	"""

	return ## you choose what variables are returned.

def post(G,gs_server,gs_group=None):
	"""
	Posts the GraphSpace object G to the GraphSpace server gs_server.
	First tries to update the graph; if this returns an error then
	a new graph is posted.  If gs_group is specified, the graph
	will be shared with the gs_group.

	:param: G -- GraphSpace graph object
	:param: gs_server -- GraphSpace server connection
	:param: gs_group -- GraphSpace group (string, optional)
	:returns: graph identifier.
	"""
	try:
		graph = gs_server.update_graph(G)
	except:
		graph = gs_server.post_graph(G)
	if gs_group:
		gs_server.share_graph(graph=graph,group_name=gs_group)
	return graph

"""
 Leave this is at the bottom of the file. Once all functions are loaded, then
 main() is called UNLESS you are importing this file into another script.
 See https://docs.python.org/3/library/__main__.html
"""
if __name__ == '__main__':
	main()
