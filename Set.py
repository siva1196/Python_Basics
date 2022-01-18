# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Set are immutable
# Set are used to store multiple items in a single variable.
# Set are created using Curly brackets{}
# Set items are unordered, unchangeable, and not allow duplicate values
# A Set can contain different data types:
def main():
    
    mySet = {1,2,3,4,5}
    mySet2 = {3.7,"Siva", False, 5}
    
    # Access Set Items
# You cannot access items in a set by referring to an index or a key
    print(mySet2)
    for i in mySet:
        print(i)
    
    # Changing the List Item Value
    
#Set are unchangable. So we cant changing the items in Set. But we can add the items using Add method

    chSet = {1,2,3,4,5}
    chSet.add(6)    # Add the item in Set
    print("Add Method ",chSet)
    chSet2 = {7,8,9}
    chSet.update(chSet2)
    print("Update method",chSet)
    
    mySet1 = {1,2,3,"Siva",True}
    mySet2 = {"Dog", "Tiger", True}
    mySet3 = {1,2,3,"Siva",True}
    mySet4 = {1,2,3,"Siva",True}
    mySet5 = {1,2,3,"Siva",True}
    mySet6 = {1,2,3,"Siva",True}
    
    mySet1.remove("Siva")       # remove specified item in the set
    print("Remove Method ",mySet1)
    
    mySet2.discard(True)        # remove specified item in the set
    print("Discard Method ",mySet2)
    
    mySet3.pop()            # remove last item in the set
    print("Pop method ", mySet3)
    
    mySet4.clear()      # remove all the item in the set
    print("Clear Method ", mySet4)
    
    del mySet5          # remove the whole set
    #print("Del method ", mySet5)    # #this will raise an error because the set no longer exists
    
    # joining the Sets
    
    mySet1.update(mySet2)   # The update() method inserts the items in set2 into set1
    print("Update method ",mySet1)
    
    Set1 = mySet1.union(mySet3) # The union() method returns a new set with all items from both sets
    print("union Method ",Set1)
    
    Set2 = {"Dog", "Cat", "Rabbit"}
    Set3 = {"Dog", "Elephant", "Lion"}
    Set4 = {"Dog", "Elephant", "Tiger"}
    Set2.intersection_update(Set3)  # Keep the duplicates only in Set2
    print("Intersection_Update Method", Set2)
    Set5 = Set3.intersection(Set4)  # make the new set with duplicates only
    print("Intersection Method", Set5)
    
    #Keep the items that are not present in both sets
    
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    z = x.symmetric_difference(y)
    print("symmetric_difference Method",z)
    x.symmetric_difference_update(y)
    print("symmetric_difference_update Method",x)
    
if __name__ == "__main__":
    main()
