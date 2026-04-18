#3.a 
LinkedList = []
FirstNode = -1
FirstEmpty = 0
for i in range (0, 19):
    LinkedList.append([-1, i+1])
LinkedList.append([-1,-1])

#3.b 
def InsertData():
    global LinkedList
    global FirstNode
    global FirstEmpty
    for x in range (5):
         if FirstEmpty != -1:  
            nextEmpty = LinkedList[FirstEmpty][1] 
            LinkedList[FirstEmpty][0] = int(input("Value: ")) 
            LinkedList[FirstEmpty][1] = FirstNode 
            FirstNode = FirstEmpty 
            FirstEmpty = nextEmpty 
         else:
            break
        
#3.c.i 
def OutputLinkedList():
    global LinkedList
    global FirstNode
    global FirstEmpty
    currentpointer = FirstNode
    while currentpointer != -1:
        print(LinkedList[currentpointer][0])
        currentpointer = LinkedList[currentpointer][1]
        
#3.c.ii 
InsertData()
OutputLinkedList()


        