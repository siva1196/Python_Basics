# Lists are Mutable
# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets[]
# List items are ordered, changeable, and allow duplicate values
# A list can contain different data types:
def main():
    
    myList = [1,2,3,4,5]
    myList2 = [3.7,"Siva", False, 5]
    
    # Access List Items
    print(myList[0:])
    print(myList[:4])
    print(myList[2:4])
    print(myList[-5:-1])
    
    # Changing the List Item Value
    myList[4] = 6
    print(myList)
    myList[1:3] = [7,8]     # changing the item into the list
    print(myList)
    myList.insert(3, 10)    # Inserting the item into the list
    print(myList)
    
    # Adding Items in the List 
    
    myList.append("King") # it add the item in the list at the last
    print(myList)
    myList.extend(myList2)  # adding the two lists
    print(myList)
    
    # Remove the items from the list
    myList.remove(1)    # remove the mentioned items from the list
    print(myList)
    myList2.remove("Siva")  # remove the mentioned items from the list
    print(myList2)
    del myList[0]   # remove the mentioned index items from the list
    print(myList)
    myList.pop(3)   # remove the mentioned index items from the list
    print(myList)
    myList.pop()    # remove the last items from the list
    print(myList)
    myList.clear()  # remove the all the items from the list
    print(myList)
    
    # Sorting the list
    numList = [6,8,2,4,0,1,10]
    numList2 = [10,79,46,9,89]
    numList.sort() # Sort the list by ascending order
    print(numList)
    numList2.sort(reverse = True) # Sort the list by descending order
    print(numList2)
    
    # Copying the list
    copyList = numList.copy()   # copying the list from another list
    copyList2 = list(numList2)  # copying the list from another list
    print(copyList)
    print(copyList2)
    
if __name__ == "__main__":
    main()
