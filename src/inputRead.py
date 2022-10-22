import sys;
import re

from structure import Edge;

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