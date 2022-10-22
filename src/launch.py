import inputRead
from structure import Graph, Node, Edge

g = Graph()
#pridani vsech uzlu ktere jsme nasli v cyklu do objektu graf. Pridavame vsechno najednou na konci cteni.
for x in inputRead.inputReadNodesLaunch():
    g.graphNodes.append(Node(x))

for x,y in inputRead.inputReadEdges().items():
    edgeParts = x.split(" - ")
    edgeFrom = g.getNodeWithName(edgeParts[0])
    edgeTo = g.getNodeWithName(edgeParts[1])
    g.graphEdges.append(Edge(edgeFrom, edgeTo, y))

for x in g.graphEdges:
    print("hrana:"+repr(x.edgeFrom.nodeName))
    print("hrana:"+repr(x.edgeTo.nodeName))
    print("hodnota:"+repr(x.value))

    g.getNodeWithName(x.edgeFrom.nodeName).outputEdges.append(x)
    g.getNodeWithName(x.edgeTo.nodeName).inputEdges.append(x)

for x in g.graphNodes:
    print("jmeno uzlu " + x.nodeName)
    print("vstup: " + repr(x.inputEdges))
    print("vystup: " + repr(x.outputEdges))

