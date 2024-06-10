def getNodeNumber(filename):
    
    source = open(filename)
    initNumber = [0]; 

    for position, line in enumerate(source):
        if position in initNumber:
            numOfNodes = int(line) 
    return numOfNodes

def getArrayFromFile(column, number, filename):
    
    source = open(filename)
    arr = []

    for i, line in enumerate(source):
        if i >= 1 and i <= number:
            arr.append((line.replace('\n','')).split(' ')[column])
    return arr

def getAdjMatrix(filename):  
    adjMatrix = []
    
    source = open(filename)
    numOfNodes = getNodeNumber(filename)
    
    for position, line in enumerate(source):
        line = line.replace('\n','').split(' ')
        row = []
        if(position >= numOfNodes + 1):
            for weight in line:
                row.append(int(weight)) 
            adjMatrix.append(row) 
    
    return adjMatrix

def containsNode(arr,Node):
    for item in arr:
        if (item.name==Node.name and item.x==Node.x and item.y==Node.y):
            return True
    return False

def isNeighbors(node1,node2):
    for key,value in node1.neighbors.items():
        if (key.name==node2.name and key.x==node2.x and key.y==node2.y):
            return True
    return False

def getMinimumAStarNode(myGraph, myNode, endNode,currentValue):
    curMinNode = myNode; 
    count = 999999; 
    for key,value in myNode.neighbors.items():
        currentNode = myGraph.searchNodeByNode(key)
        curCount = value + currentNode.calculateHaversine(endNode)+currentValue; 
        if (curCount<count): 
            count = curCount
            curMinNode = currentNode
    
    return curMinNode

def is_in_queue(x,q):
    
    for items in q.queue:
        if (items[1].name==x.name):
            return True
    return False

def findInQueue(x,q):
    
    for items in q.queue:
        if(items[1].name==x.name):
            return items[1]
    return None

def toAdjacencyList(pathList):
    edges = []
    for i in range(len(pathList)):
        if(i != (len(pathList) - 1)):
            edge = []
            edge.append(pathList[i].name)
            edge.append(pathList[i + 1].name)
            edges.append(edge)
    return edges

def checkIfInEdges(node1, node2, edges):
    for i in range(len(edges)):
        if(edges[i][0] == node1 and edges[i][1] == node2 or 
           edges[i][0] == node2 and edges[i][1] == node1):
            return True
    return False