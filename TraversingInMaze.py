import math
import re

def load_testcases(filename):
    #creating the dictonary for the test cases with each 
    testcases = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        maze = ''
        
        for line in lines:
            try:
                line = line.strip()
                if 'Input' in line:
                    continue
                elif 'maze' in line:
                    mazeId = line.split(')')[0].strip()
                    maze = line.split('=')[1].strip()
                elif 'start' in line:
                    maze = eval(maze)
                    start = eval(line.split('=')[1].strip())
                elif 'destination' in line:
                    destination = eval(line.split('=')[1].strip())
                    testcases[mazeId] = {}
                    testcases[mazeId]['input']= maze
                    testcases[mazeId]['start'] = start
                    testcases[mazeId]['destination'] = destination
               
                else:
                    maze += line
            except:
                if mazeId in testcases.keys():
                    del testcases[mazeId]
            
    return testcases


class MinHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, index):
        return (index - 1) // 2
        
    def left_child(self, index):
        return 2 * index + 1
        
    def right_child(self, index):
        return 2 * index + 2
        
    def has_parent(self, index):
        return self.parent(index) >= 0
        
    def has_left_child(self, index):
        return self.left_child(index) < len(self.heap)
        
    def has_right_child(self, index):
        return self.right_child(index) < len(self.heap)
        
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def heapify_up(self, index):
        while (self.has_parent(index) and
               self.heap[index] < self.heap[self.parent(index)]):
            parent_index = self.parent(index)
            self.swap(index, parent_index)
            index = parent_index
        
    def heapify_down(self, index):
        while self.has_left_child(index):
            smallest_child_index = self.left_child(index)
            
            if (self.has_right_child(index) and
                self.heap[self.right_child(index)] < self.heap[smallest_child_index]):
                smallest_child_index = self.right_child(index)
                
            if self.heap[index] < self.heap[smallest_child_index]:
                break
            
            self.swap(index, smallest_child_index)
            index = smallest_child_index
        
    def push(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)
        
    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty.")
            
        self.swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        self.heapify_down(0)
        
        return item
        
    def peek(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty.")
            
        return self.heap[0]
        
    def is_empty(self):
        return len(self.heap) == 0
        
    def size(self):
        return len(self.heap)


def getShortestPath(maze,start,destination):
    
    #get the number of rows and columns from the input maze
    rows = len(maze)
    columns = len(maze[0])
    
    #initialize a 2D array as the size of the maze for the distances and make all values to infinity
    distances = [[float('inf')] * columns for _ in range(rows)]
    
    #update the distance for the start position to be 0
    distances[start[0]][start[1]] = 0
    #update the previous column to some value
    previous = [[0] * columns for _ in range(rows)]
    #initialize the vector to keep track of the visited nodes
    visitedNode = []
    
    #create an object of type MinHeap()
    heap = MinHeap()
    #push the start to the heap with the distance
    heap.push((0,start))
    
    #possible movements from any node (left, right, up, down )
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #run the loop unitll the heap  is empty
    while heap:
        
        #get the node from the heap with least distance
        currentCost, currentNode = heap.pop()
        
        #add the current node to the visitednode list
        visitedNode.append(currentNode)
        
        #break out from the loop when the current node is destination node
        if currentNode == destination:
            break
        
        #get the neighbouring nodes from the current node by all possible movements from the current node
        for mx,my in movements:
            x = mx+currentNode[0]
            y = my+currentNode[1]
            
            if 0 <= x < rows and 0 <= y < columns:
                # Calculate the cost to move to the neighboring cell
                new_cost = currentCost + maze[x][y]

                # Update the distance if the new cost is smaller
                if new_cost < distances[x][y]:
                    distances[x][y] = new_cost

                    # Add the neighboring cell to the min heap
                    heap.push((new_cost, (x, y)))
                    
                    #add the current node as the previous node, to back track the path
                    previous[x][y] = [currentNode[0],currentNode[1]]
           
    path = []    
    current = destination
    #add the destination node to the path and backtrack the previous nodes from it
    path.append(tuple(current))
    
    #repeat the loop untill current node is the start node
    while current != start:
        currentPrevious = tuple(previous[current[0]][current[1]])
        path.append(currentPrevious)
        current = currentPrevious

    # Reverse the path to get it from start to destination
    path = path[::-1]
    return path
        
    
testcases = load_testcases("input.txt")
outputs = ['Sample Output']
t =  ") Shortest path: "
for mazeId, testcase in testcases.items():
    maze = testcases[mazeId]['input']
    start = testcases[mazeId]['start']
    destination = testcases[mazeId]['destination']
    # output = testcases[testId]['output']
    shortestPath = getShortestPath(maze,start,destination)
    shortestPath = f'{mazeId}) Shortest path: {shortestPath}'
    outputs.append(shortestPath)

with open('output.txt', 'w') as file:
    # Write each element of the list as a separate line
    file.writelines(output + '\n' for output in outputs)
    

