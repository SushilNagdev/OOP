# myList =[[0,0],[0,0],[0,0],[0,0],[0,0]]

# for index in range(5):
#     marks1 = int(input("Enter Test-1 marks: "))
#     marks2 = int(input("Enter Test-2 marks: "))
#     myList[index][0] = marks1
#     myList[index][1] = marks2

# print(myList)


myData = [    
              ["Minhas", 5000],
              
              ["Sushil", 4000],
              
              ["Sunil", 2000],
              
              ["No", 345],
              
              ["yes", 2345]
         ]
    
    
for x in range(0,4):
    for y in range[x+1,5]:
        if myData[x][1]<myData[y][1]:

            tempName = myData[x][0]
            tempScore = myData[x][1]

            myData[x][0] = myData[y][0]
            myData[x][1] = myData[y][1]

            myData[y][0] = tempName
            myData[y][1] = tempScore

for index in range(0,5):
    print(myData[index][0], myData[index][1])



