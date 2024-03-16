#june 21 q1&q2
#q2


##part1
# DECLARE arraydata : ARRAY[0:9] OF INTEGER
arraydata=[10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

##part2
def linearsearch(num):



    global arraydata

    index =0
    while index <10:
         
         if num == arraydata[index]:
              return True
         else:
              index = index+1
    return False


#part3
x = int(input("enter a value to search"))
y=linearsearch(x)

if y == True:

    print("Number is found...")

else:
     
     print("Number Not found....")


def bubbleSort():
     
    global arraydata
    temp=0
    for x in range(0,9):
         for y in range(0,9):
              if arraydata[y]<arraydata[y+1]:
                   temp = arraydata[y]
                   arraydata[y] = arraydata[y+1]
                   arraydata[y+1] = temp
bubbleSort()
print(arraydata)


     



    

