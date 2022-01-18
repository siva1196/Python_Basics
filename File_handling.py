import os # to remove the file OS module needed to import

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists

#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)
try:
    #File = open("Sample.txt")
    File = open("Sample1.txt","w")
    print("File Opened")
    File.write("Wrote1 the sentence") 
    #Read = File.read() # this will return the all content in the file
    #ReadChar = File.read(5) # this will return first 5 character
    ReadLine = File.readline() # this will return one sentence of the file
    #print(Read)
    #print(ReadChar)
    print(ReadLine)
    
except:
    File = open("Sample.txt","x")
    print("File Opened")
finally:
    File.close()
    os.remove("Sample1.txt")    # remove the file (deleting)
    print("File Closed")


    