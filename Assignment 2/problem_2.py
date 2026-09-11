# Simple File Writing

name = input("Enter your name: ")

with open("name.txt",'w') as f:
    f.write(name)
    # f.close() --> "with" file close automatically 
    print("Name saved successfully.") 