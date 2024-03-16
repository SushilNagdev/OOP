#june21 q3
class TreasureChest:

    #PRIVATE question : STRING
    #PRIVATE answer   : INTEGER
    #PRIVATE points   : INTEGER

    def __init__(self, q, a, p) :
        
        self.__question = q
        self.__answer   =int(a) 
        self.__points   =int(p) 

    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self, ans):
        if ans== int(self.__answer):
            return True
        else:
            return False
        
    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(self.__points)//2
        elif attempts==3 or attempts == 4:
            return int(self.__points)//4
        else:
            return 0
        

arrayTreasure = [""]*5
def readData():
    global arrayTreasure
    index = 0
    myFile = open("TreasureChestData.txt")

    line1 = myFile.readline()

    while line1 !="":
        line2 =  myFile.readline()
        line3 =  myFile.readline()

        arrayTreasure[index] = TreasureChest(line1, line2, line3)

        index = index+1
        
        line1 = myFile.readline()
    myFile.close()

readData()
qNo = int(input("Enter a question between 1 and 5:"))
print(arrayTreasure[qNo-1].getQuestion())

attempts = 1
correct = False
while correct ==False:
    ans = int(input("Enter your answer: "))
    if arrayTreasure[qNo-1].checkAnswer(ans) == True:
        correct = True
    else:
        attempts = attempts +1
print(arrayTreasure[qNo-1].getPoints(attempts))