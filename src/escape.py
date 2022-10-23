import inputRead
from structure import Graph, Node, Edge

g = Graph()

nodes = inputRead.inputReadNodes(2,"^Sections\:\s(.*)$",", ")
g.setNodesFromList(nodes)
edges = inputRead.inputReadTwoEdges(" - ")

g.inputEdgeTuplesToGraphWithoutValue(edges)
g.mirrorEdges()
g.assignEdgesToNodes()
print("///////////")
#g.NodesToString()





