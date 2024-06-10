import matplotlib.pyplot as plt
import networkx as nx
from Utils import *
from Node import *
 
class Graph:
    def __init__(self, filename):
        self.nodeList = []
        
      
        numOfNodes = getNodeNumber(filename)
       
        nameArray = getArrayFromFile(0, numOfNodes, filename)
        xArray = getArrayFromFile(1, numOfNodes, filename)
        yArray = getArrayFromFile(2, numOfNodes, filename)
   
        for i in range (0, (numOfNodes)):
            self.nodeList.append(Node(nameArray[i], float(xArray[i]), float(yArray[i])))
      
        self.setNeighbors(filename)
    
    def setNeighbors(self, filename):
        adjMatrix = getAdjMatrix(filename)
        
        for i in range(len(self.nodeList)):
            dictOfNeighbors = defaultdict(lambda: "No Nodes")
            weightRow = adjMatrix[i]
            for j in range(len(weightRow)):
                if(weightRow[j] == 1):
                    weight = self.nodeList[i].calculateHaversine(self.nodeList[j])
                    dictOfNeighbors[self.nodeList[j]] = weight
            self.nodeList[i].neighbors = dictOfNeighbors
    
    def searchByName(self, name):
        for node in self.nodeList:
            if(node.name == name):
                return node
    
    def checkGraph(self):
        for i in range (0, len(self.nodeList)):
            print("Node %d: " % (i + 1))
            self.nodeList[i].printNode()
            print()
            
    def visualize(self, pathList):
        graph = nx.Graph()
        path = toAdjacencyList(pathList)
        
        for node in self.nodeList:
            graph.add_node(node.name)
            
            for key, value in node.neighbors.items():
             
                if(checkIfInEdges(node.name, key.name, path)):
                    graph.add_edge(node.name, key.name, color = 'r', weight = round(value, 2))
                elif(not graph.has_edge(node.name, key.name)):
                    graph.add_edge(node.name, key.name, color = 'b', weight = round(value, 2))
   
        pos=nx.spring_layout(graph)
    
        edges,colors = zip(*nx.get_edge_attributes(graph, 'color').items())
        nx.draw(graph, pos, edgelist=edges, edge_color=colors, with_labels = True, font_weight = 'bold')
        edge_weight = nx.get_edge_attributes(graph, 'weight') 
        nx.draw_networkx_edge_labels(graph, pos, edge_labels = edge_weight)
        print("Successfully visualize the graph. Close the NetworkX Visualization to continue!")
        plt.show()
        
    def isNodeInGraphByName(self,nodeName):
        for n in self.nodeList:
            if (n.name==nodeName):
                return True
        return False
    
    def searchNodeByNode(self,Node):
    
        for n in self.nodeList:
            if (n.name==Node.name):
                return n
            
    def getPoints(self):
      
        points = []
        for node in self.nodeList:
            nodePoint = []
            nodePoint.append(node.x)
            nodePoint.append(node.y)
            nodePoint.append(node.name)
            points.append(nodePoint)
        return points
    
    def showAllPlaces(self):
   
        print("List of available places: ")
        for node in self.nodeList:
            print(node.name)
        print()

    def removeAllNodeParent(self):
  
        for item in self.nodeList:
            item.removeAllParent()