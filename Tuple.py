# Tuple are immutable
# Tuple are used to store multiple items in a single variable.
# Tuple are created using round brackets()
# Tuple items are ordered, unchangeable, and allow duplicate values
# A Tuple can contain different data types:
def main():
    
    myTuple = (1,2,3,4,5)
    myTuple2 = (3.7,"Siva", False, 5)
    
    # Access Tuple Items
    print(myTuple[0:])
    print(myTuple[:4])
    print(myTuple[2:4])
    print(myTuple[-5:-1])
    
    # Changing the List Item Value
    
#Tuple are unchangable. So we cant the add, append or changing the items in Tuple. So we can change the tuple into List then we can change the values and then convert into Tuple

    chTuple = (1,2,3,4,5)
    chList = list(chTuple)
    chList.append(6)
    chList[1] = "Siva"
    chTuple = tuple(chList)
    print(chTuple)

    
if __name__ == "__main__":
    main()
