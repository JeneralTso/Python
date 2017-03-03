'''
Jenny Tso
Python Course: Drill (Item 48/68)

Write your own version of the sorted() method in Python.
This method should take a list as an argument and return 
a list that is sorted in ascending order.
Print out each sorted list to the shell.

(Using an inserting sort, as they are apparently
the fastest option for working with shorter lists.)

'''

print("Sorting Method Drill \n")

def smallListSort(smList):
   for i in range(1,len(smList)):

     value = smList[i]

     while (i > 0) and (smList[i-1]) > value:
         smList[i]=smList[i-1]
         i = i - 1

     smList[i] = value

smList = [67,45,2,13,1,998]
smallListSort(smList)
print(smList)

smList = [89,23,33,45,10,12,45,45,45]
smallListSort(smList)
print(smList)
