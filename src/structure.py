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
                
            
    