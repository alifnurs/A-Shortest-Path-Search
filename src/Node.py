from collections import defaultdict
from math import *

# Node class
class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.neighbors = defaultdict(lambda: "No neighbors")
        self.parent = []
        
    def getDistanceBetween(self, otherNode):
        x = self.x - otherNode.x
        y = self.y - otherNode.y
        
        return sqrt(x ** 2 + y ** 2)
    
    def calculateHaversine(self, otherNode):
        
        earthRadius = 6371
        
        lat1 = radians(self.x)
        long1 = radians(self.y)
        lat2 = radians(otherNode.x)
        long2 = radians(otherNode.y)
        
        latDiff = lat2 - lat1
        longDiff = long2 - long1
        
        a = (sin(latDiff / 2)**2) + (cos(lat1) * cos(lat2) * sin(longDiff / 2)**2)
        c = 2 * asin(sqrt(a))
        
        return(c* earthRadius)
    
    def printNode(self):
        print("%s (%d, %d)" % (self.name, self.x, self.y))
        print("List of neighbors:")
        for key, value in self.neighbors.items():
            print(key.name, ":", value)
            
    def containsNeighbor(self,node):
        for key,value in self.neighbors:
            if (node.name==key.name):
                return True
        return False

    def addParent(self,parentNode):
        self.parent.append(parentNode)

    def sortNeighbors(self):
        self.neighbors = {k: v for k, v in sorted(self.neighbors.items(), key=lambda item: item[1])}

    def getParents(self):
        if (len(self.parent)!=0):
            return self.parent[0]
        else:
            return []
    def hasParents(self):
        return (len(self.parent)!=0)
    
    def removeAllParent(self):
        self.parent.clear()

    def sameName(self,Node):
        return (self.name==Node.name)