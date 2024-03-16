#part1
class node:
    def __init__(self, d, nN):

        self.data= d
        self.nextNode = nN

#part2       
#DECLARE linkedList : ARRAY[0:9] of node
linkedList =[node(1,1),
             node(5,4),
             node(6,7),
             node(7,-1),
             node(2,2),
             node(0,6),
             node(0,8),
             node(56,3),
             node(0,9),
             node(0,-1)]
    
startPointer = 0
emptyList = 5
#part3

def outputNodes(linkedList, startPointer):
    currentPointer = startPointer

    while currentPointer!= -1:

        print(linkedList[currentPointer].data)
        currentPointer = linkedList[currentPointer].nextNode


# outputNodes(linkedList, startPointer)


def addNode(linkedList, startPointer, emptyList):
    if emptyList == -1:
        return False
    else:
        newItem = int(input("Enter a new value"))
        temp = linkedList[emptyList].nextNode

        linkedList[emptyList] = node(newItem, -1)
        currentPointer = startPointer
        while currentPointer != -1:
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode
        
        linkedList[previousPointer].nextNode = emptyList
        emptyList = temp

        return True
outputNodes(linkedList, startPointer)
if addNode(linkedList, startPointer, emptyList)==True:
    print("Number is added...")
else:
    print("number is not added...")
outputNodes(linkedList, startPointer)
    