import sys;
import re

from structure import Edge;

def inputReadNodes(numberOfLines, regex, nodeSpliter):
    i=0    
    outputNodes=None
    for line in sys.stdin:
        if i == 0:
            line = line.strip("\r\n")
            groups = re.match(regex, line)
            if groups:
                nodes = groups.group(1).split(nodeSpliter)
                nodesStriped=[]
                for x in nodes:
                    x= x.strip("\r\n,")
                    nodesStriped.append(x)
                outputNodes=nodesStriped
            i=i+1
            continue
    
        if 0 < i < numberOfLines:
            line = line.strip("\r\n")
            nodes = line.split(nodeSpliter)
            for x in nodes:
                outputNodes.append(x)
            i=i+1
            break
    return outputNodes

def inputReadNodesLaunch():    
    for line in sys.stdin:
        line = line.strip()
        groups = re.match(r"^CPU:\s(.*)$", line)
        if groups:
            nodes = groups.group(1).split(", ")
            nodesStriped=[]
            for x in nodes:
                x= x.strip("\r")
                nodesStriped.append(x)
            nodes=nodesStriped
        break
    return nodes
                

def inputReadEdges():
    edges = {}
    for line in sys.stdin:
        line = line.strip("\r\n")
        doubleDotSplit = line.split(": ")
        edgeParts = doubleDotSplit[0]
        value = int(doubleDotSplit[1][:-1])
        edges[edgeParts] = value

    return edges

def inputReadTwoEdges(edgeSpliter):
    edges = []
    for line in sys.stdin:
        line = line.strip("\r\n")
        edgeParts = line.split(edgeSpliter)
        edges.append(edgeParts)

    return edges