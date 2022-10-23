import sys
import re


class Node:
    def __init__(self,name):
        self.nodeName = name
        self.inputEdges = []
        self.outputEdges = []
        self.nodeValue = None
    
    def assignInputEdgeToNode(self, edge):
        self.inputEdges.append(edge)

    def assignOutputEdgeToNode(self, edge):
        self.outputEdges.append(edge)


class Edge:
    edgeFrom=None
    edgeTo=None
    value=None

    def __init__(self, edgeFrom, edgeTo):
        self.edgeFrom = edgeFrom
        self.edgeTo =edgeTo
    def __init__(self, edgeFrom, edgeTo, value):
        self.edgeFrom = edgeFrom
        self.edgeTo = edgeTo
        self.value = value

class Graph:
    def __init__(self):
        self.graphNodes = []
        self.graphEdges = []

    def setNodesFromList(self, list):
        for x in list:
            self.graphNodes.append(Node(x))

    def NodesToString(self):
        for x in self.graphNodes:
            print("node name:" + repr(x.nodeName))
            print("node input edges:")
            for y in x.inputEdges:
                print(repr(y.edgeFrom.nodeName) + " - " + repr(y.edgeTo.nodeName))
            
            print("node output edges:")
            for y in x.outputEdges:

                print(repr(y.edgeFrom.nodeName) + " - " + repr(y.edgeTo.nodeName))

    
    def EdgesToString(self):
        for  x in self.graphEdges:
            print(repr(x.edgeFrom.nodeName) + " -> " + repr(x.edgeTo.nodeName))
    

    def EdgeToString(self, x):
        return x.edgeFrom.nodeName + " -> " + x.edgeTo.nodeName

    def getNodeWithName(self, name):
        nodeToReturn = None
        for x in self.graphNodes:
            if x.nodeName == name:
                if  nodeToReturn == None:
                    nodeToReturn = x
                else:
                    print("Error: Multiple nodes with same name")
        if nodeToReturn == None: 
            print("node not found")
        return nodeToReturn
    
    def inputEdgeTuplesToGraphWithoutValue(self, edgeTuples):
        for x in edgeTuples:
            edgeFrom = self.getNodeWithName(x[0])
            edgeTo = self.getNodeWithName(x[1]) 
            self.graphEdges.append(Edge(edgeFrom, edgeTo, None))
    
    def assignEdgesToNodes(self):
        for x in self.graphEdges:
            print("Jmeno nodu: "+ repr(x.edgeFrom.nodeName) +"// Hrana: " + self.EdgeToString(x))
            self.getNodeWithName(x.edgeFrom.nodeName).outputEdges.append(x)
            self.getNodeWithName(x.edgeTo.nodeName).inputEdges.append(x)
    
    def mirrorEdges(self):
        mirroredEdges = []
        for x in self.graphEdges:
            #print(x.edgeFrom.nodeName, x.edgeTo.nodeName)
            mirroredEdges.append(Edge(x.edgeTo, x.edgeFrom, None))
    
        for  x in mirroredEdges:
            #print(repr(x.edgeFrom.nodeName) + " -> " + repr(x.edgeTo.nodeName))
            self.graphEdges.append(x)
            

    



         
    