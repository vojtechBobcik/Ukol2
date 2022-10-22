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
    g.getNodeWithName(x.edgeFrom.nodeName).outputEdges.append(x)
    g.getNodeWithName(x.edgeTo.nodeName).inputEdges.append(x)

def sortEdgesByValue(x):
    return x.value

g.graphEdges.sort(key=sortEdgesByValue)

processedNodes = []
spanningTreeEdges = []
for x in g.graphEdges:
    print(x.value, x.edgeFrom.nodeName, x.edgeTo.nodeName)
    if x.edgeFrom in processedNodes and x.edgeTo in processedNodes:
        continue

    if x.edgeFrom not in processedNodes and x.edgeTo not in processedNodes:

        processedNodes.append(x.edgeFrom)
        processedNodes.append(x.edgeTo)
        spanningTreeEdges.append(x)
        continue

    if x.edgeFrom not in processedNodes:

        processedNodes.append(x.edgeFrom)
        spanningTreeEdges.append(x)
        continue

    if x.edgeTo not in processedNodes:
        processedNodes.append(x.edgeTo)
        spanningTreeEdges.append(x)
        continue
    
print("Output:")
for x in spanningTreeEdges:
    print(repr(x.edgeFrom.nodeName) + " - " + repr(x.edgeTo.nodeName))


