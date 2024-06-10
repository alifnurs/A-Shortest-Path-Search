
from flask import Flask, render_template
from queue import PriorityQueue
from Graph import *

def printqueue(q):
    for items in q.queue:
        if (not items[1].hasParents()):
            print("No items in the queue!")
        else:
            print (str(items[0])+ " node " + items[1].name+ " with parent " + items[1].getParents().name)

def AStarSearch(graph, goalName, startName):
    solution = PriorityQueue()
    with solution.mutex:
        solution.queue.clear() 

    graph.removeAllNodeParent() 

    solution2 = [] 
    
    goalNode = graph.searchByName(goalName) #
    startNode = graph.searchByName(startName) 
    solution.put((0, startNode))
    i = -1
    while(not is_in_queue(goalNode, solution) and i<len(solution.queue)):
        i+=1
        if (i>=len(solution.queue)): 
            break
        curNode = solution.queue[i]

        for j in range (0,i):
            for key,value in solution.queue[j][1].neighbors.items():
                if (not is_in_queue(key, solution)):
                    key.addParent((solution.queue[j])[1])
                    solution.put((key.calculateHaversine(goalNode)+ value+key.getDistanceBetween(goalNode), key))

        for key,value in curNode[1].neighbors.items():
            if (not is_in_queue(key, solution)):
                key.addParent(curNode[1])
                solution.put((key.calculateHaversine(goalNode)+ value, key)) 
        
        solution.queue.sort()

    if (i>=len(solution.queue)):
        return []
            
    finalGoalNode = findInQueue(goalNode,solution)  

    while(finalGoalNode.hasParents()):
        solution2.append(finalGoalNode)
        finalGoalNode = findInQueue(finalGoalNode.getParents(),solution)
    solution2.append(finalGoalNode)
    solution2.reverse()
        
    return solution2

def getGraphFromFile():
    foundFile = False
    
    while(not foundFile):
        try:
            filename = input("Masukkan nama file lokasi yang ingin kamu gunakan : ")
            graph = Graph(filename)
            foundFile = True
        except:
            print("File tidak ditemukan !!! \n")
    
    return graph

def visualize(graph, miscList):
    check = int(input("Pilih (1) untuk visualisasi dengan NetworkX, (2) dengan HERE Maps API, dan 3 untuk menggunakan keduanya : "))
    if(check == 1):
        graph.visualize(miscList)
    elif(check == 2):
        print("Akses link local untuk melihat visualisasi dengan HERE Map API")
        print("CTRL-C untuk restart!\n")
        app.run(debug = False)
    elif(check == 3):
        graph.visualize(miscList)
        print("Akses link local untuk melihat visualisasi dengan HERE Map API")
        print("CTRL-C untuk restart!\n")
        app.run(debug = False)
    else:
        print("Input tidak valid ! membatalkan Visualisasi!")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def map():
    points = graph.getPoints()
    
    solution = AStarSearch(graph, goalName, startName)
    
 
    path = []
    for node in solution:
        sols = []
        sols.append(node.x)
        sols.append(node.y)
        sols.append(node.name)
        path.append(sols)
        
  
    return render_template('map.html', points = points, path = path)


graph = getGraphFromFile()


graph.visualize([])

while(True):
    
   
    print()
    choice = int(input("Masukkan (1) untuk memulai A*, (2) untuk memasukkan ulang file lokasi, (3) untuk keluar program : "))
    
   
    if(choice == 1):
        print("Memulai proses!!!\n")
        graph.showAllPlaces()
        startName = input("Masukkan Lokasi Awal : ") 
        goalName = input("Masukkan Lokasi Tujuan : ")  

        if (not graph.isNodeInGraphByName(startName) or (not graph.isNodeInGraphByName(goalName))):
            print("Maaf, lokasi yang kamu cari tidak ada !!!")
        elif(startName == goalName):
            print("Lokasi yang kamu masukkan sama!!!, tolong masukkan lokasi yang berbeda !!")
        else:
            solution = AStarSearch(graph, goalName, startName) 

            if (len(solution) == 0): 
                print ("Tidak ada rute yang ditemukan !!!")
            else:
            
                print("Rute telah ditemukan !!!")
                print("Jarak terdekat dari ", startName, "ke ", goalName, " adalah :")
                for nodes in solution[:-1]:
                    print(nodes.name, end = " => ")
                print(solution[-1].name)
                print()
                
                visualize(graph, solution)
                
 
    elif(choice == 2):
        graph = getGraphFromFile()

    elif(choice == 3):
        print("Thank you! !_!")
        exit()
   
    else:
        print("Inputan salah !!! tolong masukkan dengan benar....")
        
